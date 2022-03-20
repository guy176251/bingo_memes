import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useTiles } from "context/tiles";
import { useState } from "react";
import { Button, Col, FormControl, Row } from "react-bootstrap";
import { useParams } from "react-router-dom";

const styles = {
    gutter: "g-3",
    subGutter: "g-2",
    tilePadding: "py-2 pe-3",
    tileLook: "bg-light rounded",
    tileIndexLook: "text-center border-end h-100",
    tileClickedLook: "bg-secondary text-white rounded",
    indicatorLook: "text-center p-1",
    showOnDesktop: "d-none d-lg-block",
};

export default function TileInfoComponent() {
    const { tiles, search, setSearch } = useTiles();
    const { cardId } = useParams();
    const [minimize, setMinimize] = useState(false);

    if (!tiles) {
        return null;
    }

    const indicators = (
        <Row className={`row-cols-5 ${styles.subGutter}`}>
            {tiles.map((tile) => (
                <Col>
                    <div
                        className={[
                            styles.indicatorLook,
                            tile.clicked ? styles.tileClickedLook : styles.tileLook,
                        ].join(" ")}
                    >
                        {tile.index}
                    </div>
                </Col>
            ))}
        </Row>
    );

    const searchBar = (
        <FormControl
            placeholder="Search Tiles"
            value={search}
            onChange={(e) => {
                e.preventDefault();
                setSearch(e.target.value);
            }}
            onClick={() => window.scrollTo(0, 0)}
        />
    );

    const gridButton = (
        <Button
            variant={minimize ? "success" : "danger"}
            onClick={() => setMinimize(!minimize)}
        >
            Grid
            <FontAwesomeIcon icon={minimize ? faEye : faEyeSlash} className="ms-2" />
        </Button>
    );

    return cardId ? (
        <Row className={styles.gutter}>
            <Col xs={12} className={minimize ? styles.showOnDesktop : ""}>
                {indicators}
            </Col>
            <Col xs={12}>
                <Row className={styles.gutter}>
                    <Col xs={4} className="d-lg-none">
                        {gridButton}
                    </Col>
                    <Col xs={8} lg={12}>
                        {searchBar}
                    </Col>
                </Row>
            </Col>
        </Row>
    ) : null;
}
