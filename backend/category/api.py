import re
from datetime import datetime
from typing import Optional, Set

from core.auth import JWTOrReadOnlyAuth
from django.db.models import (Case, Exists, F, OuterRef, Q, QuerySet, Value,
                              When)
from ninja import ModelSchema, Router, Schema
from ninja.pagination import PageNumberPagination, paginate
from pydantic import HttpUrl, validator
from pydantic.dataclasses import dataclass as pyd_dataclass
from user.api import UserSchema

from .models import Category, Subscription

router = Router(tags=["category"])


@pyd_dataclass(eq=True, frozen=True)
class Foo:
    foo: str = "foo"


class CategoryInSchema(Schema):
    name: str
    description: str
    icon_url: HttpUrl
    banner_url: HttpUrl

    @validator("name")
    def validate_name(cls, name):
        match = re.match(r"^\w+$", name)
        if not match:
            raise ValueError("Name can only contain numbers, letters and _.")
        return name


@pyd_dataclass(eq=True, frozen=True)
class HashtagSchema(Schema):
    name: str

    # def __hash__(self):  # make hashable BaseModel subclass
    #     return hash((type(self),) + tuple(self.__dict__.values()))


class CategoryOutSchema(CategoryInSchema):
    id: int
    author: UserSchema
    created_at: datetime
    hashtags: Set[HashtagSchema]
    is_subscribed: Optional[bool]


class SubscriptionSchema(Schema):
    category_id: int
    user_id: Optional[int]


def add_category_exceptions(api):
    @api.exception_handler(Category.DoesNotExist)
    def category_not_exist(request, exc):
        return api.create_response(
            request, {"detail": "Not a valid category id."}, status=422
        )


def annotated_categories(categories: QuerySet, user):
    categories = categories.annotate(
        is_subscribed=Exists(
            Subscription.objects.filter(category=OuterRef("pk"), user=user)
        )
    )
    return categories


def outgoing_categories(auth):
    categories = Category.objects.prefetch_related("author")
    if auth.is_authenticated:
        return annotated_categories(categories, auth.site_user)
    else:
        return categories


@router.get("{int:category_id}", response=CategoryOutSchema)
def get_category(request, category_id: int):
    return outgoing_categories(request.user).get(pk=category_id)


@router.get("", response=list[CategoryOutSchema], url_name="list")
@paginate(PageNumberPagination)
def list_categories(request, **kwargs):
    return Category.objects.prefetch_related("author")


@router.post("", response=CategoryOutSchema)
def create_category(request, payload: CategoryInSchema):
    data = payload.dict()
    data["author"] = request.user.site_user
    return Category.objects.create(**data)


@router.post("subscribe", response=SubscriptionSchema)
def create_subscription(request, payload: SubscriptionSchema):
    data = payload.dict()
    data["user_id"] = request.user.site_user.id
    # return Subscription.objects.create(**data)
    subscription, created = Subscription.objects.get_or_create(**data)
    if not created:
        subscription.delete()
    return subscription
