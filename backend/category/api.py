from typing import Optional
from datetime import datetime
from ninja_jwt.authentication import JWTAuth
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError
from ninja.pagination import paginate, PageNumberPagination
from ninja_extra import NinjaExtraAPI
from pydantic import HttpUrl

from .models import Category, Subscription
from user.api import UserSchema

api = NinjaExtraAPI(urls_namespace="category")


class CategoryInSchema(Schema):
    name: str
    description: str
    icon_url: HttpUrl
    banner_url: HttpUrl


class CategoryOutSchema(CategoryInSchema):
    id: int
    author: UserSchema
    created_at: datetime


class SubscriptionSchema(Schema):
    category_id: int
    user_id: Optional[int]


@api.exception_handler(Category.DoesNotExist)
def category_not_exist(request, exc):
    return api.create_response(
        request, {"detail": "Not a valid category id."}, status=422
    )


@api.get("{int:category_id}", response=CategoryOutSchema)
def get_category(request, category_id: int):
    return Category.objects.get(pk=category_id)


@api.get("", response=list[CategoryOutSchema], url_name="list")
@paginate(PageNumberPagination)
def list_categories(request, **kwargs):
    return Category.objects.all()


@api.post("", response=CategoryOutSchema, auth=JWTAuth())
def create_category(request, payload: CategoryInSchema):
    data = payload.dict()
    data["author"] = request.user.site_user
    return Category.objects.create(**data)


@api.post("subscribe", response=SubscriptionSchema, auth=JWTAuth())
def create_subscription(request, payload: SubscriptionSchema):
    data = payload.dict()
    data["user_id"] = request.user.site_user.id
    return Subscription.objects.create(**data)
