from django.urls import path  # , re_path
from . import views
from pathlib import Path


def trailing_slash(path: Path) -> str:
    return str(path / " ").strip()


class Url(str):
    basedir = ""
    subdir = ""

    def __new__(cls, value):
        return str.__new__(cls, trailing_slash(Path(cls.basedir) / cls.subdir / value))

    def __truediv__(self, route):
        return Url(trailing_slash(Path(self) / route))

    def __idiv__(self, route):
        return self.__truediv__(self, route)


class BaseUrl(Url):
    basedir = "api"


class SearchUrl(BaseUrl):
    subdir = "bar"


class PopularUrl(BaseUrl):
    subdir = "popular"


class Routes:
    class Rest:
        CARDS = BaseUrl("cards")
        CATEGORIES = BaseUrl("categories")
        USERS = BaseUrl("users")

    class Auth:
        LOGIN = BaseUrl("login")
        LOGOUT = BaseUrl("logout")
        SESSION = BaseUrl("session")

    class Action:
        VOTES = BaseUrl("votes")
        SIGNUP = BaseUrl("signup")
        SUBSCRIBE = BaseUrl("subscribe")
        FOLLOW = BaseUrl("follow")

    class SearchBar:
        CARDS = SearchUrl("cards")
        CATEGORIES = SearchUrl("categories")

    class Popular:
        CATEGORIES = PopularUrl("categories")


urlpatterns = [
    path(Routes.Auth.LOGIN, views.login_view),
    path(Routes.Auth.LOGOUT, views.logout_view),
    path(Routes.Auth.SESSION, views.session_view),
    ##########################
    path(Routes.Rest.CARDS, views.CardList.as_view()),
    path(Routes.Rest.CARDS / "<int:pk>", views.CardDetail.as_view()),
    path(Routes.Rest.CATEGORIES, views.CategoryList.as_view()),
    path(Routes.Rest.CATEGORIES / "<str:name>", views.CategoryDetail.as_view()),
    path(Routes.Rest.USERS / "<int:pk>", views.UserDetail.as_view()),
    ##########################
    path(Routes.Action.VOTES, views.upvote_view),
    path(Routes.Action.SIGNUP, views.create_user_view),
    path(Routes.Action.SUBSCRIBE, views.sub_category_view),
    path(Routes.Action.FOLLOW, views.follow_user_view),
    ##########################
    path(Routes.Popular.CATEGORIES, views.PopularCategoryList.as_view()),
    path(Routes.SearchBar.CATEGORIES, views.CategorySearchList.as_view()),
    path(Routes.SearchBar.CARDS, views.CardSearchList.as_view()),
]

# urlpatterns = [
#     ##########################
#     path("api/popular/categories/", views.PopularCategoryList.as_view()),
#     ##########################
#     path("api/bar/categories/", views.CategorySearchList.as_view()),
#     path("api/bar/cards/", views.CardSearchList.as_view()),
#     ##########################
#     path("api/categories/", views.CategoryList.as_view()),
#     path("api/categories/<str:name>/", views.CategoryDetail.as_view()),
#     path("api/cards/", views.CardList.as_view()),
#     path("api/cards/<int:pk>/", views.CardDetail.as_view()),
#     path("api/users/<int:pk>/", views.UserDetail.as_view()),
#     ##########################
#     path("api/votes/", views.upvote_view),
#     path("api/signup/", views.create_user_view),
#     path("api/subscribe/", views.sub_category_view),
#     path("api/follow/", views.follow_user_view),
#     path("api/home/", views.HomePageList.as_view()),
#     ##########################
#     path("api/login/", views.login_view, name="api-login"),
#     path("api/logout/", views.logout_view, name="api-logout"),
#     path("api/session/", views.session_view, name="api-session"),
#     ##########################
# ]
