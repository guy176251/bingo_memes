import pytest
from django.urls import reverse

from .factories import AuthUserFactory


@pytest.mark.django_db
def test_get_user(api_client):
    user = AuthUserFactory()
    api_client.request_or_fail(200, "get", f"/api/user/{user.profile.id}")


@pytest.mark.django_db
def test_list_users(api_client):
    AuthUserFactory()
    data = api_client.request_or_fail(200, "get", "/api/user/")
    assert type(data) == dict
    assert "items" in data
    assert len(data["items"]) == 1


@pytest.mark.django_db
def test_create_user(api_client):
    api_client.set_csrf_header()
    api_client.request_or_fail(
        200,
        "post",
        reverse("api-1.0.0:user_create"),
        {
            "username": "ssssssssssssssssssss",
            "email": "lkjasd@example.com",
            "password": "asdad",
        },
    )


@pytest.mark.django_db
def test_login(api_client):
    user = AuthUserFactory()
    api_client.jwt_login(user)
    api_client.request_or_fail(200, "get", "/api/user/is_logged_in")


@pytest.mark.django_db
def test_email_validation(api_client):
    api_client.set_csrf_header()
    # pass invalid email domain, should fail validation
    api_client.request_or_fail(
        422,
        "post",
        "/api/user/",
        {
            "username": "SomeUser",
            "email": "lkjasd@woiejfoijfgjhkeriugh.com",
            "password": "asdad",
        },
    )


@pytest.mark.django_db
def test_not_found(api_client):
    api_client.request_or_fail(422, "get", "/api/user/123")


@pytest.mark.django_db
def test_follow(api_client):
    follower = AuthUserFactory()
    followed = AuthUserFactory()
    api_client.jwt_login(follower)

    # follow should pass
    api_client.request_or_fail(200, "post", "/api/user/follow", {"followed_id": followed.id})

    # check user if follow worked
    data = api_client.request_or_fail(200, "get", f"/api/user/{follower.profile.id}")
    assert len(data["following"]) == 1

    data = api_client.request_or_fail(200, "get", f"/api/user/{followed.profile.id}")
    assert data["is_following"] is True


@pytest.mark.django_db
def test_jwt_refresh(api_client):
    user = AuthUserFactory()
    api_client.set_csrf_header()
    data = api_client.request_or_fail(401, "post", "/api/token/refresh")
    api_client.jwt_login(user)
    data = api_client.request_or_fail(200, "post", "/api/token/refresh")
    assert "access" in data
    assert "refresh" in api_client.cookies
