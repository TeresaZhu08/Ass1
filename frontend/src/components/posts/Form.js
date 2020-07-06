import React, { Component } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addPosts } from '../../actions/posts';

export class Form extends Component {
    state = {
        title: '',
        content: '',
    };

    static propTypes = {
        addPosts: PropTypes.func.isRequired,
    };

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    onSubmit = (e) => {
        e.preventDefault();
        const { title, content } = this.state;
        const post = { title, content };
        this.props.addPosts(post);
        this.setState({
            title: '',
            content: '',
        });
    };

    render() {
        return (
            <div className="card card-body mt-4 mb-4">
        <h2>Add Post</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Content</label>
            <input
              className="form-control"
              type="text"
              name="content"
              onChange={this.onChange}
              value={content}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addPosts })(Form);

