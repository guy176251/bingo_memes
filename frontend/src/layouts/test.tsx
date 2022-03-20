import Container from "react-bootstrap/Container";
//import Row from "react-bootstrap/Row";
//import Col from "react-bootstrap/Col";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { Outlet, Link } from "react-router-dom";
import { TestCardComponent, TestComponent } from "../components/test";
//import CardPlaceholderComponent from "components/card/placeholder";

export function TestHome() {
    const navItems = [
        ["/", "Home"],
        ["one", "One"],
        ["two", "Two"],
        ["three", "Three"],
        ["one/nested", "Nested One"],
        ["placeholder", "Placeholder"],
    ];

    return (
        <>
            <Navbar variant="dark" bg="primary">
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
                <div className="my-2">
                    {Array(4)
                        .fill(0)
                        .map((_, index) => (
                            <Link
                                className="btn btn-primary me-2"
                                to={`card/${index + 1}`}
                            >
                                Card {index + 1}
                            </Link>
                        ))}
                </div>
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

export function TestCardMainLayout() {
    return <Outlet />;
}

export function TestCardDetailLayout() {
    return <TestCardComponent />;
}
