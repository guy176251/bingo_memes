import { Nav, Navbar } from "react-bootstrap";
import { Link } from "react-router-dom";
import { sortMethodItems } from "./const";

interface Props {
    currentSort: string;
}

const baseUrl = "?sort=";
const baseColor = "dark";
const secondColor = "primary";
const styles = {
    padding: "px-2",
    shape: "rounded",
    itemColor: `bg-white text-${baseColor}`,
    itemActiveColor: `bg-${secondColor} text-white`,
    itemPadding: "me-2 px-3 py-1",
    itemShape: "rounded-pill",
    navBg: baseColor,
};

export default function CardSortComponent({ currentSort }: Props) {
    return (
        <Navbar bg={styles.navBg} className={[styles.shape].join(" ")}>
            <Nav className={styles.padding}>
                {sortMethodItems.map(([method, label]) => (
                    <Nav.Item> 
                        <Nav.Link
                            as={Link}
                            to={`${baseUrl}${method}`}
                            eventKey={method}
                            className={[
                                styles.itemShape,
                                styles.itemPadding,
                                currentSort === method
                                    ? styles.itemActiveColor
                                    : styles.itemColor,
                            ].join(" ")}
                        >
                            {label}
                        </Nav.Link>
                    </Nav.Item>
                ))}
            </Nav>
        </Navbar>
    );
}
