import pytest
from django.test import Client

from user.models import AuthUser, SiteUser
from core.tools import pprint_color


@pytest.fixture
def request_or_fail():
    """
    Makes a request and sends back api data.
    Fails if status code doesn't match request.
    """

    def wrapper(method, status_code, *args, **kwargs):
        resp = method(*args, **kwargs)
        data = resp.json()
        pprint_color({"URL": args[0], "DATA": data})
        assert resp.status_code == status_code
        return data

    return wrapper


@pytest.fixture
def client_auth(request_or_fail):
    def authorizer(client: Client, user: SiteUser):
        creds = request_or_fail(
            client.post,
            200,
            "/api/token/pair",
            {"username": user.auth.username, "password": "pass"},
            "application/json",
        )
        client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]
        return creds

    return authorizer
