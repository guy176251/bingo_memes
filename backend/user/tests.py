from django.test import TestCase

from .factories import AuthUserFactory
from tools import pprint_color


class EndpointTest(TestCase):
    def post_json(self, url, data, **kwargs):
        """
        Helper shortcut for POST requests with JSON data.
        """

        return self.client.post(url, data, **kwargs, content_type="application/json")

    def test_get_all_users(self):
        for _ in range(5):
            AuthUserFactory()

        resp = self.client.get("/api/user/")
        self.assertEqual(resp.status_code, 200)
        users = resp.json()
        pprint_color(users)
        self.assertEqual(type(users), list)

    def test_retrieve_user(self):
        user_obj = AuthUserFactory()
        resp = self.client.get(f"/api/user/{user_obj.site_user.id}")
        pprint_color(resp.json())
        self.assertEqual(resp.status_code, 200)

    def test_create_user(self):
        resp = self.post_json(
            "/api/user/",
            {
                "username": "SomeUser",
                "email": "lkjasd@woiejfoijfgjhkeriugh.com",
                "password": "asdad",
            },
        )
        self.assertEqual(resp.status_code, 422)
        resp = self.post_json(
            "/api/user/",
            {
                "username": "SomeUser",
                "email": "lkjasd@example.com",
                "password": "asdad",
            },
        )
        user = resp.json()
        pprint_color(user)
        self.assertEqual(resp.status_code, 200)

    def test_login(self):
        user_obj = AuthUserFactory()
        # default password for auth user is 'pass'
        resp = self.post_json(
            "/api/user/token/pair", {"username": user_obj.username, "password": "pass"}
        )
        self.assertEqual(resp.status_code, 200)
        creds = resp.json()
        pprint_color(creds)

        self.assertTrue("access" in creds)
        self.assertTrue("refresh" in creds)
        self.assertTrue("username" in creds)

        self.client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]
        resp = self.client.get("/api/user/is_logged_in")
        self.assertEqual(resp.status_code, 200)
        pprint_color(resp.json())

    def test_follow(self):
        follower = AuthUserFactory()
        followed = AuthUserFactory()

        # login
        resp = self.post_json(
            "/api/user/token/pair", {"username": follower.username, "password": "pass"}
        )
        self.assertEqual(resp.status_code, 200)
        creds = resp.json()
        self.client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + creds["access"]

        # follow should pass
        resp = self.post_json("/api/user/follow", {"followed_id": followed.id})
        pprint_color(resp.json())
        self.assertEqual(resp.status_code, 200)

        # check user if follow worked
        resp = self.client.get(f"/api/user/{follower.id}")
        self.assertEqual(resp.status_code, 200)
        pprint_color(resp.json())
        self.assertEqual(len(resp.json()["following"]), 1)

        # follow should fail
        resp = self.post_json("/api/user/follow", {"followed_id": 1234})
        pprint_color(resp.json())
        self.assertEqual(resp.status_code, 422)

    def test_not_found(self):
        resp = self.client.get("/api/user/123")
        pprint_color(resp.json())
        self.assertEqual(resp.status_code, 422)

        # resp = self.client.get("/api/user/")
        # self.assertEqual(resp.status_code, 200)
        # users = resp.json()
        # pprint_color(users)
        # self.assertEqual(len(users["results"]), 2)

        # resp = self.client.get(f"/api/user/{user1.site_user.id}")
        # pprint_color(resp.json())
        # self.assertEqual(resp.status_code, 200)

    def test_redirect(self):
        resp = self.client.get("/api/user/go_somewhere_else")
        self.assertEqual(resp.status_code, 200)
        users = resp.json()
        pprint_color(users)
        # self.assertEqual(len(users["results"]), 2)
