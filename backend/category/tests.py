import pytest
from core.tools import pprint_color
from django.test import Client
from faker import Faker
from user.factories import AuthUserFactory, SiteUserFactory

from .factories import CategoryFactory


@pytest.mark.django_db
def test_factory():
    CategoryFactory()


@pytest.mark.django_db
def test_retrieve_category(client: Client, request_or_fail):
    category = CategoryFactory()
    request_or_fail(client.get, 200, f"/api/category/{category.id}")


@pytest.mark.django_db
def test_subscribe(client: Client, client_auth, request_or_fail):
    category = CategoryFactory()
    user = SiteUserFactory()
    client_auth(client, user)

    # test subscription toggle
    for i in range(1, 4):
        request_or_fail(
            client.post,
            200,
            "/api/category/subscribe",
            {"category_id": category.id},
            "application/json",
        )
        data = request_or_fail(client.get, 200, f"/api/category/{category.id}")
        assert data['subscribed'] == bool(i % 2)


@pytest.mark.django_db
def test_list_categories(client: Client, request_or_fail):
    CategoryFactory()
    data = request_or_fail(client.get, 200, "/api/category/")
    assert type(data) == list
    assert len(data) == 1


@pytest.mark.django_db
def test_create_category(client: Client, client_auth, request_or_fail):
    user = SiteUserFactory()
    fake = Faker()
    client_auth(client, user)
    request_or_fail(
        client.post,
        200,
        "/api/category/",
        {
            "name": "CreatedCategory",
            "description": "some description...",
            "banner_url": fake.uri(),
            "icon_url": fake.uri(),
        },
        "application/json",
    )


@pytest.mark.django_db
def test_doesnt_exist(client: Client):
    resp = client.get("/api/category/1")
    assert resp.status_code == 422
