import pytest
from rest_framework.test import APITestCase

from api.models import BingoCard, BingoCardCategory
from api.serializers import CardListSerializer, TileSerializer


@pytest.mark.django_db
def test_login(api_client, create_user_and_login):
    username = "guy"
    create_user_and_login(client=api_client, username=username)


@pytest.mark.django_db
def test_create_card(create_card_and_user):
    create_card_and_user(
        username="author",
        category_name="category 1",
        card_name="card 1",
    )


@pytest.mark.django_db
def test_get_cards(api_client, create_card_and_user):
    create_card_and_user(username="u", category_name="C", card_name="c")
    resp = api_client.get("/api/cards/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_vote(api_client, create_user_and_login, create_card):
    user = create_user_and_login(
        client=api_client,
        username="user1",
    )
    card = create_card(
        user=user,
        category_name="category 1",
        card_name="card 1",
    )
    resp = api_client.post("/api/votes/", {"up": True, "card_id": card.id})
    assert resp.status_code == 200


def test_tile_serializer():
    data = [{"text": "asd"}]
    s = TileSerializer(data=data, many=True)
    valid = s.is_valid()
    if not valid:
        print(s.errors)
    assert valid


def test_card_list_serializer():
    data = {
        "name": "card 1",
        "category_id": 1,
        "tiles": [{"text": "asd"} for _ in range(25)],
    }
    serializer = CardListSerializer(data=data)
    valid = serializer.is_valid()
    if not valid:
        print(f"{serializer.errors = }")
    assert valid


@pytest.mark.django_db
def test_create_card_api(api_client, create_user_and_login, create_category):
    user = create_user_and_login(
        client=api_client,
        username="guy",
    )
    category = create_category(user=user, category_name="category 1")
    resp = api_client.post(
        "/api/cards/",
        {
            "tiles": [{"text": "asd"} for _ in range(25)],
            "name": "card 1",
            "category_id": category.id,
        },
    )
    print(resp.json())
    assert resp.status_code == 201
