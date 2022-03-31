import react from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'

const NavBar = () => {
    return (
        <>
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand>Meeting Note Analyzer</Navbar.Brand>
                <Nav className="me-auto">
                <Nav.Link href="http://localhost:3000/">Record</Nav.Link>
                <Nav.Link href="http://127.0.0.1:8000/audio">Analyze</Nav.Link>
                {/* <Nav.Link href="#pricing">Pricing</Nav.Link> */}
                </Nav>
                </Container>
            </Navbar>
        </>
    )
}

export default NavBar; 