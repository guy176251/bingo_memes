from typing import Optional

from core.auth import JWTOrReadOnlyAuth
from core.tools import pprint_color
from django.db.models import (Case, Exists, F, OuterRef, Q, QuerySet, Value,
                              When)
from email_validator import (EmailNotValidError, caching_resolver,
                             validate_email)
from ninja import ModelSchema, Router, Schema
from ninja.errors import ValidationError
from ninja.pagination import PageNumberPagination, paginate
from ninja_extra import NinjaExtraAPI, api_controller, route
from pydantic import EmailStr

from .models import AuthUser, Follow, SiteUser

router = Router(tags=["user"])
resolver = caching_resolver(timeout=10)


class UserSchema(ModelSchema):
    class Config:
        model = SiteUser
        model_fields = ["id", "username", "score", "created_at"]


class UserOutSchema(UserSchema):
    followers: list[UserSchema]
    following: list[UserSchema]
    is_following: Optional[bool]


class UserInSchema(Schema):
    email: EmailStr
    username: str
    password: str


class CreateFollowSchema(Schema):
    followed_id: int


def add_user_exceptions(api):
    @api.exception_handler(SiteUser.DoesNotExist)
    def user_not_exist(request, exc):
        pprint_color(request.user)
        return api.create_response(
            request, {"detail": "Not a valid user id."}, status=422
        )


def annotated_users(users: QuerySet, user: SiteUser):
    users = users.annotate(
        is_following=Exists(
            Follow.objects.filter(followed=OuterRef("pk"), follower=user)
        )
    )
    return users


def outgoing_users(auth):
    users = SiteUser.objects.prefetch_related("followers", "following")
    if auth.is_authenticated:
        return annotated_users(users, auth.site_user)
    else:
        return users


@router.get("{int:user_id}", response=UserOutSchema, url_name="get")
def get_user(request, user_id: int):
    return outgoing_users(request.user).get(pk=user_id)


@router.get("", response=list[UserOutSchema], url_name="list")
@paginate(PageNumberPagination)
def list_users(request, **kwargs):
    return outgoing_users(request.user)


@router.post("", response=UserOutSchema, auth=None)
def create_user(request, payload: UserInSchema):
    try:
        validate_email(payload.email, dns_resolver=resolver)
    except EmailNotValidError:
        raise ValidationError([{"detail": "Invalid email."}])

    data = payload.dict()
    username = data["username"]
    auth = AuthUser.objects.create_user(**data)
    site_user = SiteUser.objects.create(username=username, auth=auth, score=0)
    return site_user


@router.post("follow", response=CreateFollowSchema)
def follow_user(request, payload: CreateFollowSchema):
    SiteUser.objects.get(pk=payload.followed_id)

    return Follow.objects.create(
        followed_id=payload.followed_id,
        follower_id=request.user.site_user.id,
    )


@router.get("is_logged_in")
def is_logged_in(request):
    token_user = request.user
    return {
        "detail": "You're logged in!",
        "user": {
            "id": token_user.id,
            "username": token_user.username,
        },
    }
