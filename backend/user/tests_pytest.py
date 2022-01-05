import pytest
from django.test import Client

from .factories import AuthUserFactory, SiteUserFactory
from tools import pprint_color


@pytest.mark.django_db
def test_retrieve_user(client: Client):
    user_obj = SiteUserFactory()
    resp = client.get(f"/api/user/{user_obj.id}")
    pprint_color(resp.json())
    assert resp.status_code == 200


@pytest.mark.django_db
def test_get_all_users(client: Client):
    num_of_users = 3

    for _ in range(num_of_users):
        AuthUserFactory()

    resp = client.get("/api/user/")
    assert resp.status_code == 200
    users = resp.json()
    pprint_color(users)
    assert type(users) == list
    assert len(users) == num_of_users


@pytest.mark.django_db
def test_create_user(client: Client):
    resp = client.post(
        "/api/user/",
        {
            "username": "SomeUser",
            "email": "lkjasd@example.com",
            "password": "asdad",
        },
        "application/json",
    )
    user = resp.json()
    pprint_color(user)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_login(client: Client):
    user_obj = AuthUserFactory()
    # default password for auth user is 'pass'
    resp = client.post(
        "/api/token/pair",
        {"username": user_obj.username, "password": "pass"},
        "application/json",
    )
    assert resp.status_code == 200
    creds = resp.json()
    pprint_color(creds)

    assert all(key in creds for key in ["access", "refresh", "username"])

    client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]
    resp = client.get("/api/user/is_logged_in")
    assert resp.status_code == 200
    pprint_color(resp.json())


@pytest.mark.django_db
def test_email_validation(client: Client):
    # , content_type="application/json"
    resp = client.post(
        "/api/user/",
        {
            "username": "SomeUser",
            "email": "lkjasd@woiejfoijfgjhkeriugh.com",
            "password": "asdad",
        },
        "application/json",
    )
    assert resp.status_code == 422
    pprint_color(resp.json())


@pytest.mark.django_db
def test_not_found(client: Client):
    resp = client.get("/api/user/123")
    pprint_color(resp.json())
    assert resp.status_code == 422


@pytest.mark.django_db
def test_follow(client: Client):
    follower = AuthUserFactory()
    followed = AuthUserFactory()
    pprint_color({"username": follower.username, "follower": follower})

    # login
    resp = client.post(
        "/api/token/pair",
        {"username": follower.username, "password": "pass"},
        "application/json",
    )
    assert resp.status_code == 200
    creds = resp.json()
    client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]

    # follow should pass
    resp = client.post(
        "/api/user/follow", {"followed_id": followed.id}, "application/json"
    )
    pprint_color(resp.json())
    assert resp.status_code == 200

    # check user if follow worked
    resp = client.get(f"/api/user/{follower.id}")
    assert resp.status_code == 200
    pprint_color(resp.json())
    assert len(resp.json()["following"]) == 1

    # follow should fail
    resp = client.post("/api/user/follow", {"followed_id": 1234}, "application/json")
    pprint_color(resp.json())
    assert resp.status_code == 422
