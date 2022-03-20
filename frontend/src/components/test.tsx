import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Components } from "types/apiclient";
import { useAuth } from "../context/auth";
import CardInfoComponent from "../components/card/info";

export function TestComponent() {
    const [cards, setCards] = useState<Components.Schemas.CardListSchema[]>([]);
    const { login, logout, getClient } = useAuth();

    const doRequest = async () => {
        const client = await getClient();
        const resp = await client.card_list(null, null, {
            params: { hashtags: ["art"] },
        });
        if (resp.statusText === "OK") setCards(resp.data);
    };

    return (
        <>
            {cards.length > 0 && (
                <RowGrid
                    columns={3}
                    items={cards.slice(0, 8).map((card) => (
                        <TestCardComponent card={card} />
                    ))}
                />
            )}
            <Button onClick={doRequest}>Get Cards</Button>
            <Button onClick={() => login({ username: "gabriel28", password: "pass" })}>
                Login
            </Button>
            <Button onClick={() => logout()}>Logout</Button>
        </>
    );
}

interface CardProps {
    card?: Components.Schemas.CardListSchema | null;
}

export function TestCardComponent(props: CardProps) {
    const [card, setCard] = useState(props.card);
    const { cardId } = useParams();
    const { getClient } = useAuth();

    useEffect(() => {
        let cancelled = false;
        (async () => {
            console.log("in CardComponent doOnMount");
            if ((card && !cardId) || (card && cardId && card.id === parseInt(cardId))) {
                return;
            }
            const { card_get } = await getClient();
            const resp = await card_get(cardId);
            if (resp.status === 200 && !cancelled) {
                setCard(resp.data);
            }
        })();
        return () => {
            cancelled = true;
        };
    }, [cardId]);

    return <>{card && <CardInfoComponent card={card} />}</>;
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
