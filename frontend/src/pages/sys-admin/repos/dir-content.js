import React, { Fragment } from 'react';
import PropTypes from 'prop-types';
import { Link } from '@gatsbyjs/reach-router';
import moment from 'moment';
import { gettext } from '../../../utils/constants';
import { Utils } from '../../../utils/utils';
import Loading from '../../../components/loading';

class DirentItem extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isOpIconShown: false
    };
  }

  handleMouseOver = () => {
    this.setState({
      isOpIconShown: true
    });
  };

  handleMouseOut = () => {
    this.setState({
      isOpIconShown: false
    });
  };

  openFolder = () => {
    this.props.openFolder(this.props.dirent);
  };

  deleteDirent = (e) => {
    e.preventDefault();
    this.props.deleteDirent(this.props.dirent);
  };

  downloadDirent = (e) => {
    e.preventDefault();
    this.props.downloadDirent(this.props.dirent);
  };

  render () {
    let { isOpIconShown } = this.state;
    let { dirent, fromSystemRepo } = this.props;
    let iconUrl = Utils.getDirentIcon(dirent);

    return (
      <Fragment>
        <tr onMouseEnter={this.handleMouseOver} onMouseLeave={this.handleMouseOut}>
          <td className="text-center"><img src={iconUrl} width="24" alt='' /></td>
          <td>
            {dirent.is_file ?
              dirent.name :
              <Link to="#" onClick={this.openFolder}>{dirent.name}</Link>
            }
          </td>
          <td>
            {isOpIconShown && fromSystemRepo &&
              <a href="#" className="op-icon sf2-icon-delete" title={gettext('Delete')} onClick={this.deleteDirent}></a>
            }
            {isOpIconShown && dirent.is_file &&
            <a href="#" className="op-icon sf2-icon-download" title={gettext('Download')} onClick={this.downloadDirent}></a>
            }
          </td>
          <td>{dirent.size}</td>
          <td>{moment(dirent.mtime).fromNow()}</td>
        </tr>
      </Fragment>
    );
  }
}

DirentItem.propTypes = {
  dirent: PropTypes.object.isRequired,
  fromSystemRepo: PropTypes.bool.isRequired,
  deleteDirent: PropTypes.func.isRequired,
  openFolder: PropTypes.func.isRequired,
  downloadDirent: PropTypes.func.isRequired,
};

class DirContent extends React.Component {

  render() {
    let { loading, errorMsg, direntList } = this.props;

    if (loading) {
      return <Loading />;
    }

    if (errorMsg) {
      return <p className="error text-center mt-4">{errorMsg}</p>;
    }

    return (
      <Fragment>
        <table className="table-hover">
          <thead>
            <tr>
              <th width="5%">{/*icon*/}</th>
              <th width="55%">{gettext('Name')}</th>
              <th width="10%">{/*operation*/}</th>
              <th width="15%">{gettext('Size')}</th>
              <th width="15%">{gettext('Last Update')}</th>
            </tr>
          </thead>
          <tbody>
            {direntList.map((dirent, index) => {
              return <DirentItem
                key={index}
                dirent={dirent}
                openFolder={this.props.openFolder}
                deleteDirent={this.props.deleteDirent}
                downloadDirent={this.props.downloadDirent}
                fromSystemRepo={this.props.fromSystemRepo}
              />;
            })}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

DirContent.propTypes = {
  loading: PropTypes.bool.isRequired,
  errorMsg: PropTypes.string.isRequired,
  openFolder: PropTypes.func.isRequired,
  direntList: PropTypes.array.isRequired,
  fromSystemRepo: PropTypes.bool.isRequired,
  deleteDirent: PropTypes.func.isRequired,
  downloadDirent: PropTypes.func.isRequired,
};

export default DirContent;
