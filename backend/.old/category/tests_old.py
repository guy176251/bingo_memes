import pytest
from faker import Faker

from user.factories import ProfileFactory

from .factories import CategoryFactory


@pytest.mark.django_db
def test_retrieve_category(api_client):
    category = CategoryFactory()
    api_client.request_or_fail("get", 200, f"/api/category/{category.id}")


@pytest.mark.django_db
def test_subscribe(api_client):
    category = CategoryFactory()
    user = ProfileFactory()
    api_client.jwt_login(user)

    # test subscription toggle
    for i in range(1, 4):
        api_client.request_or_fail(
            "post",
            200,
            "/api/category/subscribe",
            {"category_id": category.id},
        )
        data = api_client.request_or_fail("get", 200, f"/api/category/{category.id}")
        assert data["is_subscribed"] == bool(i % 2)


@pytest.mark.django_db
def test_list_categories(api_client):
    CategoryFactory()
    data = api_client.request_or_fail("get", 200, "/api/category/")
    assert type(data) == list
    assert len(data) == 1


@pytest.mark.django_db
def test_create_category(api_client):
    user = ProfileFactory()
    fake = Faker()
    api_client.jwt_login(user)
    api_client.request_or_fail(
        "post",
        200,
        "/api/category/",
        {
            "name": "CreatedCategory",
            "description": "some description...",
            "banner_url": fake.uri(),
            "icon_url": fake.uri(),
        },
    )


@pytest.mark.django_db
def test_doesnt_exist(api_client):
    api_client.request_or_fail("get", 422, "/api/category/1")
