import React,{ Component} from 'react';
import {Form} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import Nav from '../Navbar/navbar';
import '../Auth/register.css'

class Register extends Component{
    render(){
        return(
            <div className="container">
            <div className="navbar">
                <Nav/>
            </div>
            <div className="row">
                <div className="col-md-4">
                <center><h4>Let us take care of your model!</h4></center>
                <Form>
                    <Form.Group>
                        <Form.Label>
                            Full Name
                        </Form.Label>
                        <Form.Control type="text" placeholder="Enter full name" />
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Institution Name
                        </Form.Label>
                        <Form.Control type="text" placeholder="Enter your institution name" />
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Email address
                        </Form.Label>
                        <Form.Control type="email" placeholder="Enter registered Email" />
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Password
                        </Form.Label>
                        <Form.Control type="password" placeholder="Password" />
                    </Form.Group>

                        <Form.Text muted>
                            Already have an account?<span><Link to="/login">Sign In here</Link></span> 
                        </Form.Text>
                
                </Form>                    

                </div>
            </div>
            </div>
        )
    }
}
export default Register;