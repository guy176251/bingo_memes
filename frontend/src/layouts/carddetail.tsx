import CardInfoComponent from "components/card/info";
import TileComponent from "components/tile";
import TileInfoComponent from "components/tile/navbar";
import { useAuth } from "context/auth";
import { useEffect, useState } from "react";
import { Col, Row } from "react-bootstrap";
import { useParams } from "react-router-dom";
import { Components } from "types/apiclient";

type CardState = Components.Schemas.CardDetailSchema | null;

const styles = {
    gutter: "g-3",
    showOnDesktop: 'd-none d-lg-block',
};

export default function CardDetailLayout() {
    const [card, setCard] = useState<CardState>(null);
    const { cardId } = useParams();
    const { getClient } = useAuth();

    useEffect(() => {
        const controller = new AbortController();
        const getData = async () => {
            if (!cardId) {
                return;
            }
            const client = await getClient();
            const resp = await client.card_get(cardId, null, {
                signal: controller.signal,
            });
            if (resp.status === 200) {
                setCard(resp.data);
            }
        };
        getData();
        return () => controller.abort();
    }, [cardId]);

    return (
        <>
            {card ? (
                <Row className={styles.gutter}>
                    <Col xs={12}>
                        <CardInfoComponent card={card} />
                    </Col>
                    <Col xs={12} className={styles.showOnDesktop}>
                        <TileInfoComponent />
                    </Col>
                    <Col xs={12}>
                        <TileComponent card={card} />
                    </Col>
                </Row>
            ) : (
                <div>loading</div>
            )}
        </>
    );
}
