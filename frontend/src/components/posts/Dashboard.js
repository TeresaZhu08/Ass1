import React, {Fragment} from 'react';
import Form from "./Form";
import Leads from "./Posts";

export default function Dashboard() {
    return (
        <Fragment>
            <Form />
            <Leads />
        </Fragment>
    )
}