import { Col, Row } from "react-bootstrap";
import { Components } from "types/apiclient";
import { listColumns } from "./const";
import CardInfoComponent from "./info";

interface Props {
    cards: Components.Schemas.CardListSchema[];
}

const styles = {
    gutter: "g-3",
    columns: listColumns,
};

export default function CardListComponent({ cards }: Props) {
    return (
        <Row className={styles.gutter}>
            {cards.map((card) => (
                <Col xs={12} lg={12 / styles.columns}>
                    <CardInfoComponent card={card} />
                </Col>
            ))}
        </Row>
    );
}
