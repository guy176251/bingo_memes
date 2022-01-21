import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { getAPIClient } from "../api/axios";
import { Components } from "../api/client";

export function TestComponent() {
    const [cards, setCards] = useState<Components.Schemas.CardOutListSchema[]>([]);

    const doRequest = async () => {
        const client = await getAPIClient();
        const resp = await client.card_api_list_cards(null, null, { params: { hashtags: ["art"] } });
        if (resp.statusText === "OK") setCards(resp.data);
    };

    return (
        <>
            {cards.length > 0 && (
                <RowGrid
                    columns={4}
                    items={cards.slice(0, 8).map((card) => (
                        <Card>
                            <Card.Body>
                                <Card.Title>{card.name}</Card.Title>
                                <Card.Text>By {card.author.username}</Card.Text>
                            </Card.Body>
                        </Card>
                    ))}
                />
            )}
            <Button onClick={doRequest}>Get User</Button>
        </>
    );
}

interface CardProps {
    card: Components.Schemas.CardOutSchema | null;
}

export function CardComponent(props: CardProps) {
    const [card, setCard] = useState(props.card);
    const { cardId } = useParams();

    const doRequest = async () => {
        if (card || !cardId) return;
        const client = await getAPIClient();
        const resp = await client.card_api_get_card(cardId);
        if (resp.status === 200) setCard(resp.data);
    };

    useEffect(() => {
        doRequest();
    }, []);

    return <></>;
}

interface GridProps {
    columns: 1 | 2 | 3 | 4 | 6 | 12;
    items: any[];
}

export function RowGrid({ columns, items }: GridProps) {
    return (
        <Row className="g-4">
            {items.map((item) => (
                <Col xs={12 / columns}>{item}</Col>
            ))}
        </Row>
    );
}
