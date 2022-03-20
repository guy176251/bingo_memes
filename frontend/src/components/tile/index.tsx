import { useTiles } from "context/tiles";
import { useEffect } from "react";
import { Col, Container, Modal, Row } from "react-bootstrap";
import { Components } from "types/apiclient";

interface Props {
    card: Components.Schemas.CardDetailSchema;
}

const styles = {
    gutter: "g-3",
    subGutter: "g-2",
    tilePadding: "py-2 pe-3",
    tileLook: "bg-light rounded",
    tileIndexLook: "text-center border-end h-100",
    tileClickedLook: "bg-secondary text-white rounded",
};

export default function TileComponent({ card }: Props) {
    const { tiles, searchedTiles, clickTile, solution, resetTiles, setTilesFromCard } =
        useTiles();


    useEffect(() => {
        setTilesFromCard(card);
    }, []);

    return (
        <>
            {tiles && searchedTiles && (
                <>
                    <Row className={styles.gutter}>
                        {/* Tiles */}
                        <Col xs={12}>
                            <Row className={styles.subGutter}>
                                {searchedTiles.map((tile) => (
                                    <Col xs={12} key={`${tile.index}`}>
                                        <div
                                            className={[
                                                styles.tilePadding,
                                                tile.clicked
                                                    ? styles.tileClickedLook
                                                    : styles.tileLook,
                                            ].join(" ")}
                                            onClick={() => clickTile(tile.index - 1)}
                                            style={{ cursor: "pointer" }}
                                        >
                                            <Row>
                                                <Col xs={2}>
                                                    <div className={styles.tileIndexLook}>
                                                        {tile.index}
                                                    </div>
                                                </Col>
                                                <Col xs={10}>{tile.text}</Col>
                                            </Row>
                                        </div>
                                    </Col>
                                ))}
                            </Row>
                        </Col>
                    </Row>
                    {/* Bingo */}
                    <Modal show={Boolean(solution)} onHide={resetTiles} centered>
                        <Modal.Header>You got bingo!</Modal.Header>
                        <Modal.Body>
                            {solution && (
                                <Row className={styles.subGutter}>
                                    {solution.map((index) => (
                                        <Col xs={12}>
                                            <div
                                                className={[
                                                    styles.tileLook,
                                                    styles.tilePadding,
                                                ].join(" ")}
                                            >
                                                <Row>
                                                    <Col xs={2}>
                                                        <div
                                                            className={
                                                                styles.tileIndexLook
                                                            }
                                                        >
                                                            {index + 1}
                                                        </div>
                                                    </Col>
                                                    <Col xs={10}>{tiles[index].text}</Col>
                                                </Row>
                                            </div>
                                        </Col>
                                    ))}
                                </Row>
                            )}
                        </Modal.Body>
                    </Modal>
                </>
            )}
        </>
    );
}
