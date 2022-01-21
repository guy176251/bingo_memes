import pytest
from category.factories import CategoryFactory
from core.tools import pprint_color
from django.test import Client
from user.factories import AuthUserFactory, SiteUserFactory

from .factories import CardFactory


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
    user = SiteUserFactory()
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
def test_vote_card(client: Client, client_auth, request_or_fail, up, expected_score):
    user = SiteUserFactory()
    card = CardFactory()
    payload = {"card_id": card.id, "up": up}

    # test auth
    resp = client.post("/api/card/vote", payload, "application/json")
    assert resp.status_code == 401

    client_auth(client, user)

    # test vote toggle-like function
    for score in [expected_score, 1]:
        request_or_fail(client.post, 200, "/api/card/vote", payload, "application/json")
        data = request_or_fail(client.get, 200, f"/api/card/{card.id}")
        assert data["score"] == score

    # test sending different up values
    for up, score in [(True, 2), (False, 0)]:
        resp = client.post(
            "/api/card/vote", {**payload, "up": up}, "application/json"
        )  # first vote
        assert resp.status_code == 200

        resp = client.get(f"/api/card/{card.id}")
        assert resp.json()["score"] == score
