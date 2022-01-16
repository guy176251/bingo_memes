from ninja import ModelSchema, Schema, Router
from ninja.errors import ValidationError

from ninja_extra import NinjaExtraAPI, api_controller, route

from pydantic import EmailStr
from email_validator import validate_email, caching_resolver, EmailNotValidError

from ninja.pagination import paginate, PageNumberPagination

# from ninja_extra.pagination import (
#     paginate,
#     PageNumberPaginationExtra,
#     PaginatedResponseSchema,
# )

from .models import SiteUser, AuthUser, Follow

router = Router(tags=["user"])
resolver = caching_resolver(timeout=10)


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


def add_user_exceptions(api):
    @api.exception_handler(SiteUser.DoesNotExist)
    def user_not_exist(request, exc):
        return api.create_response(
            request, {"detail": "Not a valid user id."}, status=422
        )


def outgoing_users():
    return SiteUser.objects.prefetch_related("followers", "following")


@router.get("{int:user_id}", response=UserOutSchema, url_name="get")
def get_user(request, user_id: int):
    return outgoing_users().get(pk=user_id)


@router.get("", response=list[UserSchema], url_name="list")
@paginate(PageNumberPagination)
def list_users(request, **kwargs):
    return outgoing_users()


@router.post("", response=UserOutSchema)
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


@router.post(
    "follow",
    response=CreateFollowSchema,
)
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


# @api_controller("user/")
# class UserController:
#     @route.get("{int:user_id}", response=UserOutSchema, url_name="get")
#     def get_user(self, request, user_id: int):
#         return SiteUser.objects.get(pk=user_id)
#
#     @route.get("", response=PaginatedResponseSchema[UserSchema], url_name="list")
#     @paginate(PageNumberPaginationExtra, page_size=50)
#     def list_users(self):
#         return SiteUser.objects.all()
#
#     @route.post("", response=UserOutSchema)
#     def create_user(self, request, payload: UserInSchema):
#         try:
#             validate_email(payload.email, dns_resolver=resolver)
#         except EmailNotValidError:
#             raise ValidationError([{"detail": "Invalid email."}])
#
#         data = payload.dict()
#         username = data["username"]
#         auth = AuthUser.objects.create_user(**data)
#         site_user = SiteUser.objects.create(
#             username=username, auth=auth, score=0
#         )
#         return site_user
#
#     @route.post(
#         "follow",
#         response=CreateFollowSchema,
#         auth=jwt_auth,
#     )
#     def follow_user(self, request, payload: CreateFollowSchema):
#         SiteUser.objects.get(pk=payload.followed_id)
#
#         return Follow.objects.create(
#             followed_id=payload.followed_id,
#             follower_id=request.user.site_user.id,
#         )
#
#     @route.get("is_logged_in", auth=jwt_auth)
#     def is_logged_in(self, request):
#         return {"detail": "You're logged in!"}
