import pytest
from django.test import Client

from .factories import CardFactory
from user.factories import AuthUserFactory
from category.factories import CategoryFactory
from core.tools import pprint_color


@pytest.mark.django_db
def test_factory():
    CardFactory()
    # card = CardFactory()
    # assert card.tiles.count() == 25


@pytest.mark.django_db
def test_get_card(client: Client):
    card = CardFactory()
    resp = client.get(f"/api/card/{card.id}")
    assert resp.status_code == 200
    pprint_color(resp.json())


@pytest.mark.django_db
def test_create_card(client: Client, client_auth):
    user = AuthUserFactory()
    category = CategoryFactory()
    client_auth(client, user)
    payload = {
        "name": "Created card #blessed",
        "category": {"id": category.id},
    }
    payload.update({f"tile_{n}": f"Tile {n} contents" for n in range(1, 26)})
    resp = client.post("/api/card/", payload, "application/json")
    pprint_color(resp.json())
    assert resp.status_code == 200


@pytest.mark.parametrize("up, expected_score", [(True, 2), (False, 0)])
@pytest.mark.django_db
def test_vote_card(client: Client, client_auth, up, expected_score):
    user = AuthUserFactory()
    card = CardFactory()
    payload = {"card_id": card.id, "up": up}

    # test auth
    resp = client.post("/api/card/vote", payload, "application/json")
    assert resp.status_code == 401

    client_auth(client, user)

    # test vote toggle-like function
    for score in [expected_score, card.score]:
        resp = client.post("/api/card/vote", payload, "application/json")  # first vote
        assert resp.status_code == 200

        resp = client.get(f"/api/card/{card.id}")
        assert resp.json()["score"] == score

    # test sending different up values
    for up, score in [(True, 2), (False, 0)]:
        resp = client.post(
            "/api/card/vote", {**payload, "up": up}, "application/json"
        )  # first vote
        assert resp.status_code == 200

        resp = client.get(f"/api/card/{card.id}")
        assert resp.json()["score"] == score
