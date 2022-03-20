from typing import Optional

import pytest
from django.http import HttpResponse
from django.test import Client

from core.tools import pprint_color
from user.models import AuthUser, Profile


@pytest.fixture
def request_or_fail():
    """
    Makes a request and sends back api data.
    Fails if status code doesn't match request.
    """

    def wrapper(method, status_code, *args, **kwargs):
        resp = method(*args, **kwargs)
        data = resp.json()
        pprint_color(resp.headers)
        assert resp.status_code == status_code
        return data

    return wrapper


class ApiClient(Client):
    def _request(
        self,
        method: str,
        path: str,
        data: Optional[dict] = None,
        follow=False,
        secure=False,
        **extra,
    ) -> HttpResponse:
        """Makes a request with content_type set to "application/json"."""

        self.extra = extra
        fn = getattr(super(), method)
        response = fn(path, data=data, content_type="application/json", secure=secure, **extra)
        if follow:
            response = self._handle_redirects(
                response, data=data, content_type="application/json", **extra
            )
        return response

    def post(self, path: str, data: dict, follow=False, secure=False, **extra) -> HttpResponse:
        return self._request("post", path, data, follow, secure, **extra)

    def put(self, path: str, data: dict, follow=False, secure=False, **extra) -> HttpResponse:
        return self._request("put", path, data, follow, secure, **extra)

    def patch(self, path: str, data: dict, follow=False, secure=False, **extra) -> HttpResponse:
        return self._request("patch", path, data, follow, secure, **extra)

    def request_or_fail(
        self,
        status_code: int,
        method: str,
        path: str,
        data: Optional[dict] = None,
        follow=False,
        secure=False,
        **extra,
    ) -> Optional[dict]:
        """Makes a request and returns json response. Fails if status_code assertion fails."""

        response = self._request(method, path, data, follow, secure, **extra)
        try:
            pprint_color(response.json())
        except Exception:
            pass
        assert response.status_code == status_code
        try:
            return response.json()
        except Exception as err:
            print(err)
            return None

    def set_csrf_header(self):
        self.get("/api/token/check_in")
        self.defaults["HTTP_X_CSRFTOKEN"] = self.cookies["csrftoken"].value

    def jwt_login(self, user: AuthUser):
        self.set_csrf_header()
        resp = self.post(
            "/api/token/pair",
            {"username": user.username, "password": "pass"},
        )
        assert resp.status_code == 200
        self.defaults["HTTP_AUTHORIZATION"] = f"Bearer {resp.json()['access']}"
        # have to reset token header because csrf is rotated on
        # every auth token operation
        self.set_csrf_header()


@pytest.fixture
def api_client():
    return ApiClient(enforce_csrf_checks=True, HTTP_ACCEPT="application/json")
