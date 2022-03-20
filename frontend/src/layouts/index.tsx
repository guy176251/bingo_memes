import TileInfoComponent from "components/tile/navbar";
import { Col, Container, Nav, Navbar, Row } from "react-bootstrap";
import { Link, Outlet } from "react-router-dom";

const bgColor = "dark";
const styles = {
    gutter: "g-4",
    padding: "py-2",
    showOnDesktop: "d-none d-lg-block",
    showOnMobile: "d-lg-none",
    navBg: bgColor,
    navVariant: "dark" as "dark" | "light" | undefined,
    tilePadding: "pb-3 pt-2",
    tileBg: `bg-${bgColor}`,
    tileLook: "rounded-bottom shadow",
};

export default function MainLayout() {
    return (
        <>
            <div className="sticky-top">
                <Navbar variant={styles.navVariant} bg={styles.navBg} sticky="top">
                    <Container>
                        <Navbar.Brand as={Link} to="/">
                            Bingo Memes
                        </Navbar.Brand>
                        <Navbar.Collapse>
                            <Nav>
                                <Nav.Item>
                                    <Nav.Link as={Link} to="/cards">
                                        Cards
                                    </Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link as={Link} to="/test">
                                        Test Page
                                    </Nav.Link>
                                </Nav.Item>
                            </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
                <div
                    className={[
                        styles.tileBg,
                        styles.tileLook,
                        styles.tilePadding,
                        styles.showOnMobile,
                    ].join(" ")}
                >
                    <Container>
                        <Row className={styles.gutter}>
                            <Col xs={12} lg={6}>
                                <TileInfoComponent />
                            </Col>
                        </Row>
                    </Container>
                </div>
            </div>
            <Container>
                <Row className={[styles.gutter, styles.padding].join(" ")}>
                    <Col xs={12} lg={8}>
                        <Outlet />
                    </Col>
                    <Col xs={4} className={styles.showOnDesktop}>
                        <div className="rounded bg-light h-100 p-3">
                            Sidebar with various shit inside
                        </div>
                    </Col>
                </Row>
            </Container>
        </>
    );
}
