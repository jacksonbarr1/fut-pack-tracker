import React from 'react';
import { Nav, Container, Navbar} from 'react-bootstrap'
import {Link} from "react-router-dom";

function NavBar() {
    return (
        <Navbar expand="lg" id="navbar" className="bg-body-secondary">
            <Container>
                <Navbar.Brand as={Link} to="/packs">FUT Pack Tracker</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link as={Link} to="/packs">My Packs</Nav.Link>
                        <Nav.Link as={Link} to="/statistics">Statistics</Nav.Link>
                        <Nav.Link as={Link} to="/settings">Settings</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavBar;