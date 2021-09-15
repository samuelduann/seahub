# Copyright (c) 2012-2017 Seafile Ltd.
import json
import logging
import os
import requests
import email.utils

from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from seaserv import seafile_api
from seahub.onlyoffice.settings import VERIFY_ONLYOFFICE_CERTIFICATE
from seahub.onlyoffice.utils import generate_onlyoffice_cache_key, get_onlyoffice_dict
from seahub.onlyoffice.converter_utils import get_file_name_without_ext, \
        get_file_ext, get_file_type, get_internal_extension, get_file_path_without_mame
from seahub.onlyoffice.converter import get_converter_uri
from seahub.utils import gen_inner_file_upload_url, is_pro_version
from seahub.utils.file_op import if_locked_by_online_office


# Get an instance of a logger
logger = logging.getLogger('onlyoffice')


@csrf_exempt
def onlyoffice_editor_callback(request):
    """ Callback func of OnlyOffice.

    The document editing service informs the document storage service about status of the document editing using the callbackUrl from JavaScript API. The document editing service use the POST request with the information in body.

    https://api.onlyoffice.com/editors/callback
    """

    if request.method != 'POST':
        logger.error('Request method if not POST.')
        # The document storage service must return the following response.
        # otherwise the document editor will display an error message.
        return HttpResponse('{"error": 0}')

    # body info of POST rquest when open file on browser
    # {u'actions': [{u'type': 1, u'userid': u'uid-1527736776860'}],
    #  u'key': u'8062bdccf9b4cf809ae3',
    #  u'status': 1,
    #  u'users': [u'uid-1527736776860']}

    # body info of POST rquest when close file's web page (save file)
    # {u'actions': [{u'type': 0, u'userid': u'uid-1527736951523'}],
    # u'changesurl': u'...',
    # u'history': {u'changes': [{u'created': u'2018-05-31 03:17:17',
    #                            u'user': {u'id': u'uid-1527736577058',
    #                                      u'name': u'lian'}},
    #                           {u'created': u'2018-05-31 03:23:55',
    #                            u'user': {u'id': u'uid-1527736951523',
    #                                      u'name': u'lian'}}],
    #              u'serverVersion': u'5.1.4'},
    # u'key': u'61484dec693009f3d506',
    # u'lastsave': u'2018-05-31T03:23:55.767Z',
    # u'notmodified': False,
    # u'status': 2,
    # u'url': u'...',
    # u'users': [u'uid-1527736951523']}

    # Defines the status of the document. Can have the following values:
    # 0 - no document with the key identifier could be found,
    # 1 - document is being edited,
    # 2 - document is ready for saving,
    # 3 - document saving error has occurred,
    # 4 - document is closed with no changes,
    # 6 - document is being edited, but the current document state is saved,
    # 7 - error has occurred while force saving the document.

    # Status 1 is received every user connection to or disconnection from document co-editing.
    #
    # Status 2 (3) is received 10 seconds after the document is closed for editing with the identifier of the user who was the last to send the changes to the document editing service.
    #
    # Status 4 is received after the document is closed for editing with no changes by the last user.
    #
    # Status 6 (7) is received when the force saving request is performed.

    post_data = json.loads(request.body)
    status = int(post_data.get('status', -1))

    if status == 1:
        logger.info('status {}'.format(status))
        return HttpResponse('{"error": 0}')

    if status not in (2, 4, 6):
        logger.error('status {}: invalid status'.format(status))
        return HttpResponse('{"error": 0}')

    # get file basic info
    doc_key = post_data.get('key')
    doc_info_from_cache = cache.get("ONLYOFFICE_%s" % doc_key)
    if not doc_info_from_cache:
        logger.error('status {}: can not get doc_info from cache by doc_key {}'.format(status, doc_key))
        return HttpResponse('{"error": 0}')

    doc_info = json.loads(doc_info_from_cache)

    repo_id = doc_info['repo_id']
    file_path = doc_info['file_path']
    username = doc_info['username']

    logger.info('status {}: get doc_info {} from cache by doc_key {}'.format(status, doc_info, doc_key))

    cache_key = generate_onlyoffice_cache_key(repo_id, file_path)

    # save file
    if status in (2, 6):

        # Defines the link to the edited document to be saved with the document storage service.
        # The link is present when the status value is equal to 2 or 3 only.
        url = post_data.get('url')
        onlyoffice_resp = requests.get(url, verify=VERIFY_ONLYOFFICE_CERTIFICATE)
        if not onlyoffice_resp:
            logger.error('[OnlyOffice] No response from file content url.')
            return HttpResponse('{"error": 0}')

        fake_obj_id = {'online_office_update': True}
        update_token = seafile_api.get_fileserver_access_token(repo_id,
                                                               json.dumps(fake_obj_id),
                                                               'update',
                                                               username)

        if not update_token:
            logger.error('[OnlyOffice] No fileserver access token.')
            return HttpResponse('{"error": 0}')

        # get file content
        files = {
            'file': onlyoffice_resp.content,
            'file_name': os.path.basename(file_path),
            'target_file': file_path,
        }

        # update file
        update_url = gen_inner_file_upload_url('update-api', update_token)
        requests.post(update_url, files=files)

        # 2 - document is ready for saving,
        if status == 2:

            logger.info('status {}: delete cache_key {} from cache'.format(status, cache_key))
            cache.delete(cache_key)

            logger.info('status {}: delete doc_key {} from cache'.format(status, doc_key))
            cache.delete("ONLYOFFICE_%s" % doc_key)

            if is_pro_version() and if_locked_by_online_office(repo_id, file_path):
                logger.info('status {}: unlock {} in repo_id {}'.format(status, file_path, repo_id))
                seafile_api.unlock_file(repo_id, file_path)

    # 4 - document is closed with no changes,
    if status == 4:

        logger.info('status {}: delete cache_key {} from cache'.format(status, cache_key))
        cache.delete(cache_key)

        logger.info('status {}: delete doc_key {} from cache'.format(status, doc_key))
        cache.delete("ONLYOFFICE_%s" % doc_key)

        if is_pro_version() and if_locked_by_online_office(repo_id, file_path):
            logger.info('status {}: unlock {} in repo_id {}'.format(status, file_path, repo_id))
            seafile_api.unlock_file(repo_id, file_path)

    return HttpResponse('{"error": 0}')


@csrf_exempt
def onlyoffice_convert(request):

    if request.method != 'POST':
        logger.error('Request method if not POST.')
        return render(request, '404.html')

    body = json.loads(request.body)

    username = body.get('username')
    file_uri = body.get('fileUri')
    file_pass = body.get('filePass') or None
    repo_id = body.get('repo_id')
    folder_name = get_file_path_without_mame(file_uri) + '/'
    file_ext = get_file_ext(file_uri)
    file_type = get_file_type(file_uri)
    new_ext = get_internal_extension(file_type)

    if not new_ext:
        logger.error('[OnlyOffice] Could not generate internal extension.')
        return HttpResponse(status=500)

    doc_dic = get_onlyoffice_dict(request, username, repo_id, file_uri)

    download_uri = doc_dic["doc_url"]
    key = doc_dic["doc_key"]

    new_uri = get_converter_uri(download_uri, file_ext, new_ext,
                               key, False, file_pass)

    if not new_uri:
        logger.error('[OnlyOffice] No response from file converter.')
        return HttpResponse(status=500)

    onlyoffice_resp = requests.get(new_uri, verify=VERIFY_ONLYOFFICE_CERTIFICATE)

    if not onlyoffice_resp:
        logger.error('[OnlyOffice] No response from file content url.')
        return HttpResponse(status=500)

    fake_obj_id = {'parent_dir': folder_name}

    upload_token = seafile_api.get_fileserver_access_token(repo_id,
                                                           json.dumps(fake_obj_id),
                                                           'upload-link',
                                                           username)

    if not upload_token:
        logger.error('[OnlyOffice] No fileserver access token.')
        return HttpResponse(status=500)

    file_name = get_file_name_without_ext(file_uri) + new_ext

    files = {
        'file': (file_name, onlyoffice_resp.content),
        'parent_dir': folder_name,
    }

    upload_url = gen_inner_file_upload_url('upload-api', upload_token)

    def rewrite_request(prepared_request):

        old_content = 'filename*=' + email.utils.encode_rfc2231(file_name, 'utf-8')
        old_content = old_content.encode()

        new_content = 'filename="{}"\r\n\r\n'.format(file_name)
        new_content = new_content.encode()

        prepared_request.body = prepared_request.body.replace(old_content, new_content)

        return prepared_request

    try:
        file_name.encode('ascii')
    except UnicodeEncodeError:
        requests.post(upload_url, files=files, auth=rewrite_request)
    else:
        requests.post(upload_url, files=files)

    return HttpResponse(status=200)
