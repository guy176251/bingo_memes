import { sortMethods } from "components/card/const";
import CardListComponent from "components/card/list";
import CardPlaceholderComponent from "components/card/placeholder";
import CardSortComponent from "components/card/sort";
import { useAuth } from "context/auth";
import { useEffect, useState } from "react";
import { Col, Row } from "react-bootstrap";
import { useSearchParams } from "react-router-dom";
import { Components } from "types/apiclient";

type CardList = Components.Schemas.CardListSchema[];

const styles = {
    gutter: "g-3",
    padding: "py-2",
    loadingAlign: "text-center",
};

export default function CardListLayout() {
    const [cards, setCards] = useState<CardList | null>(null);
    const [searchParams] = useSearchParams();
    const { getClient } = useAuth();
    const sortParam = searchParams.get("sort");
    const currentSort = sortParam && sortMethods.includes(sortParam) ? sortParam : "hot";

    useEffect(() => {
        const controller = new AbortController();
        const getData = async () => {
            setCards(null);
            const client = await getClient();
            const resp = await client.card_list(null, null, {
                signal: controller.signal,
                params: { sort: currentSort },
            });
            if (resp.status === 200) setCards(resp.data);
        };
        getData();
        return () => controller.abort();
    }, [searchParams]);

    return (
        <>
            <Row className={[styles.gutter].join(" ")}>
                <Col xs={12}>
                    <CardSortComponent currentSort={currentSort} />
                </Col>
                <Col xs={12}>
                    {cards ? (
                        <CardListComponent cards={cards} />
                    ) : (
                        <CardPlaceholderComponent />
                    )}
                </Col>
            </Row>
        </>
    );
}
