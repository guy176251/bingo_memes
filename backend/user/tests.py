from django.test import TestCase

from .factories import AuthUserFactory
from tools import pprint_color


class EndpointTest(TestCase):
    def post(self, url, data, **kwargs):
        """
        Helper shortcut for POST requests with JSON data.
        """

        return self.client.post(url, data, **kwargs, content_type="application/json")

    def test_user(self):
        user = AuthUserFactory()
        resp = self.client.get(f"/user/{user.site_user.id}")
        pprint_color(resp.json())
        self.assertEquals(resp.status_code, 200)
        payload = {
            "username": "SomeUser",
            "email": "lkjasd@example.com",
            "password": "asdad",
        }
        resp = self.post("/user/", payload)
        pprint_color(resp.json())
        self.assertEquals(resp.status_code, 200)

        # payload.pop("username")
        resp = self.post("/user/token/pair", payload)
        self.assertEquals(resp.status_code, 200)
        pprint_color(resp.json())
