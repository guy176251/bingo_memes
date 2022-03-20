import { Col, Placeholder, Row } from "react-bootstrap";
import {
    PlaceholderAnimation,
    PlaceholderSize,
} from "react-bootstrap/esm/usePlaceholder";
import { listColumns } from "./const";

const styles = {
    animation: "glow" as PlaceholderAnimation,
    columns: listColumns,
    rows: 8,
    gutter: "g-4",
    scorePadding: "my-2",
    scoreSize: "lg" as PlaceholderSize,
    textPadding: "me-1",
    textSize: "sm" as PlaceholderSize,
    upvoteColor: "warning",
    voteAlign: "w-100 text-center",
    container: "bg-light rounded",
    padding: "p-3",
};

function CardPlaceholderItem() {
    return (
        <div className={[styles.container, styles.padding].join(" ")}>
            <Row>
                <Col xs={2}>
                    <div className={styles.voteAlign}>
                        <div>
                            <Placeholder animation={styles.animation}>
                                <Placeholder xs={2} />
                            </Placeholder>
                        </div>
                        <div className={styles.scorePadding}>
                            <Placeholder animation={styles.animation}>
                                <Placeholder xs={1} size={styles.scoreSize} />
                            </Placeholder>
                        </div>
                        <div>
                            <Placeholder animation={styles.animation}>
                                <Placeholder xs={2} />
                            </Placeholder>
                        </div>
                    </div>
                </Col>
                <Col xs={10}>
                    <Placeholder as="h5" animation={styles.animation}>
                        <Placeholder xs={5} />
                    </Placeholder>
                    <Placeholder as="p" animation={styles.animation}>
                        <Placeholder
                            xs={3}
                            size={styles.textSize}
                            className={styles.textPadding}
                        />
                        <Placeholder
                            xs={8}
                            size={styles.textSize}
                            className={styles.textPadding}
                        />
                        <Placeholder
                            xs={6}
                            size={styles.textSize}
                            className={styles.textPadding}
                        />
                        <Placeholder
                            xs={4}
                            size={styles.textSize}
                            className={styles.textPadding}
                        />
                    </Placeholder>
                </Col>
            </Row>
        </div>
    );
}

export default function CardPlaceholderComponent() {
    return (
        <Row className={styles.gutter}>
            {Array(styles.rows * styles.columns)
                .fill(0)
                .map((_) => (
                    <Col xs={12} lg={12 / styles.columns}>
                        <CardPlaceholderItem />
                    </Col>
                ))}
        </Row>
    );
}
