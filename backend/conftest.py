import pytest
from django.test import Client

from user.models import AuthUser


@pytest.fixture
def client_auth():
    def authorizer(client: Client, user: AuthUser):
        resp = client.post(
            "/api/user/token/pair",
            {"username": user.username, "password": "pass"},
            "application/json",
        )
        assert resp.status_code == 200
        creds = resp.json()
        client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]
        return creds

    return authorizer
