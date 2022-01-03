from django.urls import resolve, reverse
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError
from ninja.pagination import paginate, PageNumberPagination
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController
from pydantic import EmailStr
from email_validator import validate_email, caching_resolver, EmailNotValidError

from .models import SiteUser, AuthUser, Follow

api = NinjaExtraAPI(urls_namespace="user")
api.register_controllers(NinjaJWTDefaultController)
resolver = caching_resolver(timeout=10)
jwt_auth = JWTAuth()


class UserSchema(ModelSchema):
    class Config:
        model = SiteUser
        model_fields = ["id", "username", "score", "created_at"]


class UserOutSchema(UserSchema):
    followers: list[UserSchema]
    following: list[UserSchema]


class UserInSchema(Schema):
    email: EmailStr
    username: str
    password: str


class CreateFollowSchema(Schema):
    followed_id: int


@api.exception_handler(SiteUser.DoesNotExist)
def user_not_exist(request, exc):
    return api.create_response(request, {"detail": "Not a valid user id."}, status=422)


@api.get("{int:user_id}", response=UserOutSchema, url_name="get")
def get_user(request, user_id: int):
    return SiteUser.objects.get(pk=user_id)


@api.get("", response=list[UserSchema], url_name="list")
@paginate(PageNumberPagination)
def list_users(request, **kwargs):
    return SiteUser.objects.all()


@api.post("", response=UserOutSchema)
def create_user(request, payload: UserInSchema):
    try:
        validate_email(payload.email, dns_resolver=resolver)
    except EmailNotValidError:
        raise ValidationError("Invalid email.")

    data = payload.dict()
    username = data["username"]
    auth_user = AuthUser.objects.create_user(**data)
    site_user = SiteUser.objects.create(username=username, auth_user=auth_user, score=0)
    return site_user


@api.post(
    "follow",
    response=CreateFollowSchema,
    auth=jwt_auth,
)
def follow_user(request, payload: CreateFollowSchema):
    SiteUser.objects.get(pk=payload.followed_id)

    return Follow.objects.create(
        followed_id=payload.followed_id,
        follower_id=request.user.site_user.id,
    )


@api.get("is_logged_in", auth=jwt_auth)
def is_logged_in(request):
    return {"detail": "You're logged in!"}


@api.get("go_somewhere_else")
def users_redir(request):
    view, args, kwargs = resolve(reverse("user:list"))
    kwargs["request"] = request
    return view(*args, **kwargs)
