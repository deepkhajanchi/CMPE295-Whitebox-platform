import React,{ Component} from 'react';
import Form from 'react-bootstrap/Form';
import {Link} from "react-router-dom";
import PasswordMask from 'react-password-mask';
import Nav from '../Navbar/navbar';
import '../Auth/login.css';

class Login extends Component{
    render(){
        return(
            <div className="container">
                <div className="navbar">
                    <Nav/>
                </div>
            <div className="row">

                <div className="col-md-4">
                <center><h4>Get your model tested now!</h4></center>
                <Form className="loginform">
                    <Form.Group>
                        <Form.Label>
                            Email address
                        </Form.Label>
                        <Form.Control type="email" placeholder="Enter Email" />
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Password
                        </Form.Label>
                        <Form.Control type="password" placeholder="Enter Password" />
                    </Form.Group>

                        <Form.Text muted>
                            New here?<span><Link to='/register'>Get Started now!</Link></span>
                        </Form.Text>
            
                </Form>
                </div>
            </div>
            </div>
            
        )
    }
}
export default Login;