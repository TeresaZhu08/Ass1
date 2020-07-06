import React, { Component, Fragment } from 'react';
import { withAlert } from "react-alert";
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

export class alerts extends Component {

    static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
    };

        componentDidUpdate(prevProps) {
            const { error, alert, message } = this.props;
            if (error !== prevProps.error) {
                if (error.msg.title) alert.error(`Title: ${error.msg.title.join()}`);
                if (error.msg.content) alert.error(`Content: ${error.msg.content.join()}`);
            }

            if (message !== prevProps.message) {
                if (message.deletePosts) alert.success(message.deletePosts);
                if (message.addPosts) alert.success(message.addPosts);
            }
        }

    render() {
        return <Fragment />;
    }
}

const mapStateToProps = (state) => ({
  error: state.errors,
  message: state.messages,
});

export default connect(mapStateToProps)(withAlert()(alerts));