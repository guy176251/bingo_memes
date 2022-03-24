import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import BingoCard, BingoCardCategory, SiteUser


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def wrapper(username: str) -> User:
        """Password is always "pass"."""
        user = User.objects.create_user(username=username, password="pass")
        SiteUser.objects.create(auth_user=user, name=username)
        return user

    return wrapper


@pytest.fixture
def login():
    def wrapper(client: APIClient, username: str):
        resp = client.post("/api/login/", {"username": username, "password": "pass"})
        assert resp.status_code == 200

    return wrapper


@pytest.fixture
def create_user_and_login(create_user, login):
    def wrapper(client: APIClient, username: str) -> User:
        user = create_user(username=username)
        login(client=client, username=username)
        return user

    return wrapper


@pytest.fixture
def create_category():
    def wrapper(user: User, category_name: str) -> BingoCardCategory:
        category = BingoCardCategory.objects.create(
            name=category_name,
            author=user.site_user,
        )
        return category

    return wrapper


@pytest.fixture
def create_card(create_category):
    def wrapper(user: User, category_name: str, card_name: str) -> BingoCard:
        category = create_category(
            category_name=category_name,
            user=user,
        )
        card = BingoCard.objects.create(
            name=card_name,
            category=category,
            author=user.site_user,
            ups=0,
            votes_total=0,
            score=0,
        )
        return card

    return wrapper


@pytest.fixture
def create_card_and_user(create_user, create_card):
    def wrapper(username: str, category_name: str, card_name: str) -> BingoCard:
        user = create_user(username=username)
        card = create_card(user=user, category_name=category_name, card_name=card_name)
        return card

    return wrapper
