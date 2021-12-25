# from django.contrib.auth.models import User
from ninja import NinjaAPI, ModelSchema, Schema
from pydantic import EmailStr
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from .models import SiteUser, AuthUser

# api = NinjaAPI()
api = NinjaExtraAPI()
# adds jwt authentication
api.register_controllers(NinjaJWTDefaultController)


class AuthUserSchema(ModelSchema):
    class Config:
        model = AuthUser
        model_fields = ["email"]


class SiteUserSchema(ModelSchema):
    auth_user: AuthUserSchema

    class Config:
        model = SiteUser
        model_fields = ["id", "username", "score", "created_at"]


class UserCreateSchema(Schema):
    email: EmailStr
    username: str
    password: str


@api.exception_handler(SiteUser.DoesNotExist)
def user_not_exist(request, exc):
    return api.create_response(request, {"detail": "Not a valid user id."}, status=422)


@api.get("{int:user_id}", response=SiteUserSchema)
def get_user(request, user_id: int):
    return SiteUser.objects.get(pk=user_id)


@api.post("", response=SiteUserSchema)
def create_user(request, payload: UserCreateSchema):
    data = payload.dict()
    username = data["username"]
    auth_user = AuthUser.objects.create_user(**data)
    site_user = SiteUser.objects.create(username=username, auth_user=auth_user, score=0)
    return site_user
