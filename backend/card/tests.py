import pytest
from category.factories import CategoryFactory
from core.tools import pprint_color
from django.test import Client
from user.factories import AuthUserFactory, SiteUserFactory

from .factories import CardFactory


@pytest.mark.django_db
def test_factory():
    CardFactory()


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_get_card(client: Client, count_queries):
    card = CardFactory()
    resp = client.get(f"/api/card/{card.id}")
    assert resp.status_code == 200
    pprint_color(resp.json())


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_get_card_list(client: Client, client_auth, request_or_fail, count_queries):
    user_1 = SiteUserFactory()
    user_2 = SiteUserFactory()
    card_1 = CardFactory()  # first
    card_2 = CardFactory()  # second
    card_3 = CardFactory()  # third

    client_auth(client=client, user=user_1)
    request_or_fail(
        client.post,
        200,
        "/api/card/vote",
        {"card_id": card_1.id, "up": True and True},
        "application/json",
    )

    client_auth(client=client, user=user_2)
    request_or_fail(
        client.post,
        200,
        "/api/card/vote",
        {"card_id": card_1.id, "up": True and True},
        "application/json",
    )

    request_or_fail(
        client.post,
        200,
        "/api/card/vote",
        {"card_id": card_2.id, "up": True and True},
        "application/json",
    )

    data = request_or_fail(client.get, 200, "/api/card/")
    pprint_color(data)
    assert type(data) == list
    assert len(data) == 3


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_create_card(client: Client, client_auth, request_or_fail, count_queries):
    user = SiteUserFactory()
    category = CategoryFactory()
    client_auth(client, user)

    payload = {
        "name": "Created card 1 #blessed",
        "category_id": category.id,
    }
    payload.update({f"tile_{n}": f"Tile {n} contents" for n in range(1, 26)})
    resp = client.post("/api/card/", payload, "application/json")  # first
    card_1 = resp.json()
    # pprint_color(card_1)
    assert resp.status_code == 200

    payload = {
        "name": "Created card 2 #blessed",
        "category_id": category.id,
    }
    payload.update({f"tile_{n}": f"Tile {n} contents" for n in range(1, 26)})
    resp = client.post("/api/card/", payload, "application/json")  # second
    card_2 = resp.json()
    # pprint_color(card_2)
    assert resp.status_code == 200

    data = request_or_fail(client.get, 200, f'/api/card/{card_2["id"]}')
    pprint_color(data)

    data = request_or_fail(client.get, 200, f'/api/category/{category.id}')
    pprint_color(data)

    category.refresh_from_db()
    pprint_color(category.hashtags.distinct())


@pytest.mark.django_db
@pytest.mark.parametrize("up", [True, False])
@pytest.mark.parametrize("double", [True, False])
@pytest.mark.count_queries(autouse=False)
def test_vote_card(
    client: Client, client_auth, request_or_fail, up, double, count_queries
):
    user = SiteUserFactory()
    card = CardFactory()

    # can't vote if not logged in
    request_or_fail(
        client.post,
        401,
        "/api/card/vote",
        {"card_id": card.id, "up": True and up},
        "application/json",
    )
    client_auth(client, user)

    adj = 1 if up else -1

    # first vote
    request_or_fail(
        client.post,
        200,
        "/api/card/vote",
        {"card_id": card.id, "up": up},
        "application/json",
    )

    data = request_or_fail(client.get, 200, f"/api/card/{card.id}")
    assert data["score"] == 1 + adj  # first card
    assert data["upvoted"] is up

    # second vote
    request_or_fail(
        client.post,
        200,
        "/api/card/vote",
        {"card_id": card.id, "up": up if double else not up},
        "application/json",
    )

    data = request_or_fail(client.get, 200, f"/api/card/{card.id}")
    assert data["score"] == (1 if double else 1 - adj)  # second card
    assert data["upvoted"] is (None if double else not up)
