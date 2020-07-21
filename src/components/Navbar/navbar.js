import React, { Component } from 'react';
import {Navbar, Nav, NavDropdown} from 'react-bootstrap';

class nav extends Component{
    render(){
        return(
            <div>
                <Navbar collapseOnSelect expand="lg" fixed="top" bg="dark" variant="dark">
                    <Navbar.Brand href="/login">Welcome to the Whitebox!</Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="mr-auto">
                        
                    </Nav>
                    <Nav>
                        <Nav.Link href="#Introduction">Introduction</Nav.Link>
                        <Nav.Link href="#outcome">Our mission</Nav.Link>
                        <Nav.Link href="#aboutus">About us</Nav.Link>
                        <Nav.Link href="#contactus">Contact us</Nav.Link>
                    </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </div>
        )
    }
}
export default nav;