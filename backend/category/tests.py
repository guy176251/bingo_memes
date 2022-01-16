import pytest
from faker import Faker
from django.test import Client

from .factories import CategoryFactory
from user.factories import AuthUserFactory
from tools import pprint_color


@pytest.mark.django_db
def test_factory():
    CategoryFactory()
    # pprint_color(category)


@pytest.mark.django_db
def test_retrieve_category(client: Client):
    category = CategoryFactory()
    resp = client.get(f"/api/category/{category.id}")
    assert resp.status_code == 200
    # pprint_color(resp.json())


@pytest.mark.django_db
def test_subscribe(client: Client, client_auth):
    category = CategoryFactory()
    user = AuthUserFactory()
    client_auth(client, user)
    resp = client.post(
        "/api/category/subscribe", {"category_id": category.id}, "application/json"
    )
    assert resp.status_code == 200
    # pprint_color(resp.json())


@pytest.mark.django_db
def test_list_categories(client: Client):
    num_of_categories = 5
    for _ in range(num_of_categories):
        CategoryFactory()
    resp = client.get("/api/category/")
    assert resp.status_code == 200
    data = resp.json()
    assert type(data) == list
    assert len(data) == num_of_categories
    # pprint_color(resp.json())


@pytest.mark.django_db
def test_create_category(client: Client, client_auth):
    user = AuthUserFactory()
    client_auth(client, user)
    fake = Faker()
    resp = client.post(
        "/api/category/",
        {
            "name": "Created Category",
            "description": "some description...",
            "banner_url": fake.uri(),
            "icon_url": fake.uri(),
        },
        "application/json",
    )
    # pprint_color(resp.json())
    assert resp.status_code == 200


@pytest.mark.django_db
def test_doesnt_exist(client: Client):
    resp = client.get("/api/category/1")
    assert resp.status_code == 422
