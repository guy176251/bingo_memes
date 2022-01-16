import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { Outlet, Link } from "react-router-dom";
import { TestComponent } from "../components/test";

export function TestHome() {
    const navItems = [
        ["/home", "Home"],
        ["/one", "One"],
        ["/two", "Two"],
        ["/three", "Three"],
        ["/one/nested", "Nested One"],
    ];

    return (
        <>
            <Navbar variant="dark" bg="dark">
                <Container>
                    <Navbar.Brand>Test</Navbar.Brand>
                    <Navbar.Collapse>
                        <Nav>
                            {navItems.map(([link, title]) => (
                                <Nav.Link as={Link} to={link}>
                                    {title}
                                </Nav.Link>
                            ))}
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <Container>
                <Outlet />
            </Container>
        </>
    );
}

export function TestChild({ name = "Home" }: { name?: string }) {
    return (
        <>
            <h1>{name}</h1>
            <TestComponent key={name} />
            <Outlet />
        </>
    );
}
