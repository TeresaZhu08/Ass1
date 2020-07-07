import axios from 'axios';

import {GET_POSTS, DELETE_POSTS, ADD_POSTS } from "./types";

// GET POSTS
export const getPosts = () => dispatch => {
    axios
        .get('/api/leads/')
        .then((res) => {
            dispatch({
                type: GET_POSTS,
                payload: res.data
            });
        })
        .catch(err => console.log(err));
        //.catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

// DELETE POSTS
export const deletePosts = id => dispatch => {
    axios
        .delete('/api/leads/${id}/')
        .then((res) => {
           // dispatch(createMessage({ deletePosts: 'Post Deleted' }));
            dispatch({
                type: DELETE_POSTS,
                payload: id,
            });
        })
        .catch(err => console.log(err));
};

// ADD POSTS
export const addPosts = (post) => dispatch => {
    axios
        .post('/api/leads/', post)
        .then((res) => {
           // dispatch(createMessage({ addPosts: 'Post Added' }));
             dispatch({
                 type: ADD_POSTS,
                 payload: res.data,
            });
        })
        .catch(err => console.log(err));
        //.catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};