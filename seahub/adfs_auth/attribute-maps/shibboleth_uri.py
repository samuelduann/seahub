EDUPERSON_OID = "urn:oid:1.3.6.1.4.1.5923.1.1.1."
X500ATTR = "urn:oid:2.5.4."
NOREDUPERSON_OID = "urn:oid:1.3.6.1.4.1.2428.90.1."
NETSCAPE_LDAP = "urn:oid:2.16.840.1.113730.3.1."
UCL_DIR_PILOT = "urn:oid:0.9.2342.19200300.100.1."
PKCS_9 = "urn:oid:1.2.840.113549.1.9."
UMICH = "urn:oid:1.3.6.1.4.1.250.1.57."

MAP = {
    "identifier": "urn:mace:shibboleth:1.0:attributeNamespace:uri",
    "fro": {
        f"{EDUPERSON_OID}2": "eduPersonNickname",
        f"{EDUPERSON_OID}9": "eduPersonScopedAffiliation",
        f"{EDUPERSON_OID}11": "eduPersonAssurance",
        f"{EDUPERSON_OID}10": "eduPersonTargetedID",
        f"{EDUPERSON_OID}4": "eduPersonOrgUnitDN",
        f"{NOREDUPERSON_OID}6": "norEduOrgAcronym",
        f"{NOREDUPERSON_OID}7": "norEduOrgUniqueIdentifier",
        f"{NOREDUPERSON_OID}4": "norEduPersonLIN",
        f"{EDUPERSON_OID}1": "eduPersonAffiliation",
        f"{NOREDUPERSON_OID}2": "norEduOrgUnitUniqueNumber",
        f"{NETSCAPE_LDAP}40": "userSMIMECertificate",
        f"{NOREDUPERSON_OID}1": "norEduOrgUniqueNumber",
        f"{NETSCAPE_LDAP}241": "displayName",
        f"{UCL_DIR_PILOT}37": "associatedDomain",
        f"{EDUPERSON_OID}6": "eduPersonPrincipalName",
        f"{NOREDUPERSON_OID}8": "norEduOrgUnitUniqueIdentifier",
        f"{NOREDUPERSON_OID}9": "federationFeideSchemaVersion",
        f"{X500ATTR}53": "deltaRevocationList",
        f"{X500ATTR}52": "supportedAlgorithms",
        f"{X500ATTR}51": "houseIdentifier",
        f"{X500ATTR}50": "uniqueMember",
        f"{X500ATTR}19": "physicalDeliveryOfficeName",
        f"{X500ATTR}18": "postOfficeBox",
        f"{X500ATTR}17": "postalCode",
        f"{X500ATTR}16": "postalAddress",
        f"{X500ATTR}15": "businessCategory",
        f"{X500ATTR}14": "searchGuide",
        f"{EDUPERSON_OID}5": "eduPersonPrimaryAffiliation",
        f"{X500ATTR}12": "title",
        f"{X500ATTR}11": "ou",
        f"{X500ATTR}10": "o",
        f"{X500ATTR}37": "cACertificate",
        f"{X500ATTR}36": "userCertificate",
        f"{X500ATTR}31": "member",
        f"{X500ATTR}30": "supportedApplicationContext",
        f"{X500ATTR}33": "roleOccupant",
        f"{X500ATTR}32": "owner",
        f"{NETSCAPE_LDAP}1": "carLicense",
        f"{PKCS_9}1": "email",
        f"{NETSCAPE_LDAP}3": "employeeNumber",
        f"{NETSCAPE_LDAP}2": "departmentNumber",
        f"{X500ATTR}39": "certificateRevocationList",
        f"{X500ATTR}38": "authorityRevocationList",
        f"{NETSCAPE_LDAP}216": "userPKCS12",
        f"{EDUPERSON_OID}8": "eduPersonPrimaryOrgUnitDN",
        f"{X500ATTR}9": "street",
        f"{X500ATTR}8": "st",
        f"{NETSCAPE_LDAP}39": "preferredLanguage",
        f"{EDUPERSON_OID}7": "eduPersonEntitlement",
        f"{X500ATTR}2": "knowledgeInformation",
        f"{X500ATTR}7": "l",
        f"{X500ATTR}6": "c",
        f"{X500ATTR}5": "serialNumber",
        f"{X500ATTR}4": "sn",
        f"{UCL_DIR_PILOT}60": "jpegPhoto",
        f"{X500ATTR}65": "pseudonym",
        f"{NOREDUPERSON_OID}5": "norEduPersonNIN",
        f"{UCL_DIR_PILOT}3": "mail",
        f"{UCL_DIR_PILOT}25": "dc",
        f"{X500ATTR}40": "crossCertificatePair",
        f"{X500ATTR}42": "givenName",
        f"{X500ATTR}43": "initials",
        f"{X500ATTR}44": "generationQualifier",
        f"{X500ATTR}45": "x500UniqueIdentifier",
        f"{X500ATTR}46": "dnQualifier",
        f"{X500ATTR}47": "enhancedSearchGuide",
        f"{X500ATTR}48": "protocolInformation",
        f"{X500ATTR}54": "dmdName",
        f"{NETSCAPE_LDAP}4": "employeeType",
        f"{X500ATTR}22": "teletexTerminalIdentifier",
        f"{X500ATTR}23": "facsimileTelephoneNumber",
        f"{X500ATTR}20": "telephoneNumber",
        f"{X500ATTR}21": "telexNumber",
        f"{X500ATTR}26": "registeredAddress",
        f"{X500ATTR}27": "destinationIndicator",
        f"{X500ATTR}24": "x121Address",
        f"{X500ATTR}25": "internationaliSDNNumber",
        f"{X500ATTR}28": "preferredDeliveryMethod",
        f"{X500ATTR}29": "presentationAddress",
        f"{EDUPERSON_OID}3": "eduPersonOrgDN",
        f"{NOREDUPERSON_OID}3": "norEduPersonBirthDate",
    },
    "to": {
        "roleOccupant": f"{X500ATTR}33",
        "gn": f"{X500ATTR}42",
        "norEduPersonNIN": f"{NOREDUPERSON_OID}5",
        "title": f"{X500ATTR}12",
        "facsimileTelephoneNumber": f"{X500ATTR}23",
        "mail": f"{UCL_DIR_PILOT}3",
        "postOfficeBox": f"{X500ATTR}18",
        "fax": f"{X500ATTR}23",
        "telephoneNumber": f"{X500ATTR}20",
        "norEduPersonBirthDate": f"{NOREDUPERSON_OID}3",
        "rfc822Mailbox": f"{UCL_DIR_PILOT}3",
        "dc": f"{UCL_DIR_PILOT}25",
        "countryName": f"{X500ATTR}6",
        "emailAddress": f"{PKCS_9}1",
        "employeeNumber": f"{NETSCAPE_LDAP}3",
        "organizationName": f"{X500ATTR}10",
        "eduPersonAssurance": f"{EDUPERSON_OID}11",
        "norEduOrgAcronym": f"{NOREDUPERSON_OID}6",
        "registeredAddress": f"{X500ATTR}26",
        "physicalDeliveryOfficeName": f"{X500ATTR}19",
        "associatedDomain": f"{UCL_DIR_PILOT}37",
        "l": f"{X500ATTR}7",
        "stateOrProvinceName": f"{X500ATTR}8",
        "federationFeideSchemaVersion": f"{NOREDUPERSON_OID}9",
        "pkcs9email": f"{PKCS_9}1",
        "givenName": f"{X500ATTR}42",
        "x500UniqueIdentifier": f"{X500ATTR}45",
        "eduPersonNickname": f"{EDUPERSON_OID}2",
        "houseIdentifier": f"{X500ATTR}51",
        "street": f"{X500ATTR}9",
        "supportedAlgorithms": f"{X500ATTR}52",
        "preferredLanguage": f"{NETSCAPE_LDAP}39",
        "postalAddress": f"{X500ATTR}16",
        "email": f"{PKCS_9}1",
        "norEduOrgUnitUniqueIdentifier": f"{NOREDUPERSON_OID}8",
        "eduPersonPrimaryOrgUnitDN": f"{EDUPERSON_OID}8",
        "c": f"{X500ATTR}6",
        "teletexTerminalIdentifier": f"{X500ATTR}22",
        "o": f"{X500ATTR}10",
        "cACertificate": f"{X500ATTR}37",
        "telexNumber": f"{X500ATTR}21",
        "ou": f"{X500ATTR}11",
        "initials": f"{X500ATTR}43",
        "eduPersonOrgUnitDN": f"{EDUPERSON_OID}4",
        "deltaRevocationList": f"{X500ATTR}53",
        "norEduPersonLIN": f"{NOREDUPERSON_OID}4",
        "supportedApplicationContext": f"{X500ATTR}30",
        "eduPersonEntitlement": f"{EDUPERSON_OID}7",
        "generationQualifier": f"{X500ATTR}44",
        "eduPersonAffiliation": f"{EDUPERSON_OID}1",
        "eduPersonPrincipalName": f"{EDUPERSON_OID}6",
        "localityName": f"{X500ATTR}7",
        "owner": f"{X500ATTR}32",
        "norEduOrgUnitUniqueNumber": f"{NOREDUPERSON_OID}2",
        "searchGuide": f"{X500ATTR}14",
        "certificateRevocationList": f"{X500ATTR}39",
        "organizationalUnitName": f"{X500ATTR}11",
        "userCertificate": f"{X500ATTR}36",
        "preferredDeliveryMethod": f"{X500ATTR}28",
        "internationaliSDNNumber": f"{X500ATTR}25",
        "uniqueMember": f"{X500ATTR}50",
        "departmentNumber": f"{NETSCAPE_LDAP}2",
        "enhancedSearchGuide": f"{X500ATTR}47",
        "userPKCS12": f"{NETSCAPE_LDAP}216",
        "eduPersonTargetedID": f"{EDUPERSON_OID}10",
        "norEduOrgUniqueNumber": f"{NOREDUPERSON_OID}1",
        "x121Address": f"{X500ATTR}24",
        "destinationIndicator": f"{X500ATTR}27",
        "eduPersonPrimaryAffiliation": f"{EDUPERSON_OID}5",
        "surname": f"{X500ATTR}4",
        "jpegPhoto": f"{UCL_DIR_PILOT}60",
        "eduPersonScopedAffiliation": f"{EDUPERSON_OID}9",
        "protocolInformation": f"{X500ATTR}48",
        "knowledgeInformation": f"{X500ATTR}2",
        "employeeType": f"{NETSCAPE_LDAP}4",
        "userSMIMECertificate": f"{NETSCAPE_LDAP}40",
        "member": f"{X500ATTR}31",
        "streetAddress": f"{X500ATTR}9",
        "dmdName": f"{X500ATTR}54",
        "postalCode": f"{X500ATTR}17",
        "pseudonym": f"{X500ATTR}65",
        "dnQualifier": f"{X500ATTR}46",
        "crossCertificatePair": f"{X500ATTR}40",
        "eduPersonOrgDN": f"{EDUPERSON_OID}3",
        "authorityRevocationList": f"{X500ATTR}38",
        "displayName": f"{NETSCAPE_LDAP}241",
        "businessCategory": f"{X500ATTR}15",
        "serialNumber": f"{X500ATTR}5",
        "norEduOrgUniqueIdentifier": f"{NOREDUPERSON_OID}7",
        "st": f"{X500ATTR}8",
        "carLicense": f"{NETSCAPE_LDAP}1",
        "presentationAddress": f"{X500ATTR}29",
        "sn": f"{X500ATTR}4",
        "domainComponent": f"{UCL_DIR_PILOT}25",
    },
}
