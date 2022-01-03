import pytest
from django.test import Client

from .factories import CardFactory
from user.factories import AuthUserFactory
from category.factories import CategoryFactory
from tools import pprint_color


@pytest.mark.django_db
def test_factory():
    card = CardFactory()
    assert card.tiles.count() == 25


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
        "tiles": [{"text": f"Tile {n}"} for n in range(1, 26)],
    }
    resp = client.post("/api/card/", payload, "application/json")
    pprint_color(resp.json())
    assert resp.status_code == 200
