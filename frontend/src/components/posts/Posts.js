import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getPosts, deletePosts } from "../../actions/posts";

export class Posts extends Component {
    static propTypes = {
        posts: PropTypes.array.isRequired,
        getPosts: PropTypes.func.isRequired,
        deletePosts: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getPosts();
    };

    render() {
        return (
            <Fragment>
                <h2>Posts</h2>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Title</th>
                            <th>Content</th>
                        </tr>
                    </thead>
                    <tbody>
                        { this.props.posts.map( (post) => (
                            <tr key={post.id}>
                                <td>{post.id}</td>
                                <td>{post.title}</td>
                                <td>{post.content}</td>
                                <td>
                                    <button className="btn btn-danger btn-sm"
                                            onClick={this.props.deletePosts.bind(this, post.id)}>
                                        {" "}
                                        Delete
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </Fragment>
        );
    }
}

const mapStateToProps = state => ({
    posts: state.posts.posts
});

export default connect(mapStateToProps, { getPosts, deletePosts })(Posts);