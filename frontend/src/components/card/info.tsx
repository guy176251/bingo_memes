import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Components } from "types/apiclient";
import VoteButtons from "./vote";
import titleWithHashtags, { createdAtStr } from "helpers";
import { Link } from "react-router-dom";

type BingoCard = Components.Schemas.CardListSchema | Components.Schemas.CardDetailSchema;

interface Props {
    card: BingoCard;
}

const styles = {
    link: "bingocard-link",
    container: "bg-light rounded h-100",
    paddingY: "py-3",
    paddingX: "px-3",
    paddingLeft: "ps-3",
    paddingRight: "pe-3",
};

export default function CardInfoComponent({ card }: Props) {
    return (
        <div className={styles.container}>
            <Row>
                <Col xs={2}>
                    <div className={[styles.paddingY, styles.paddingLeft].join(" ")}>
                        <VoteButtons card={card} />
                    </div>
                </Col>
                <Col xs={10}>
                    <Link to={`/cards/${card.id}`} className={styles.link}>
                        <div className={[styles.paddingY, styles.paddingRight].join(" ")}>
                            <h5>{titleWithHashtags(card.title)}</h5>
                            <p>
                                {card.author.username} · {createdAtStr(card.created_at)}
                            </p>
                        </div>
                    </Link>
                </Col>
            </Row>
        </div>
    );
}
