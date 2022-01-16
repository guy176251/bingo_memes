from typing import Optional
from datetime import datetime
from ninja import ModelSchema, Schema, Router
from ninja.errors import ValidationError
from ninja.pagination import paginate, PageNumberPagination
from pydantic import HttpUrl

from .models import Category, Subscription
from user.api import UserSchema

router = Router(tags=["category"])


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


def add_category_exceptions(api):
    @api.exception_handler(Category.DoesNotExist)
    def category_not_exist(request, exc):
        return api.create_response(
            request, {"detail": "Not a valid category id."}, status=422
        )


@router.get("{int:category_id}", response=CategoryOutSchema)
def get_category(request, category_id: int):
    return Category.objects.get(pk=category_id)


@router.get("", response=list[CategoryOutSchema], url_name="list")
@paginate(PageNumberPagination)
def list_categories(request, **kwargs):
    return Category.objects.all()


@router.post("", response=CategoryOutSchema)
def create_category(request, payload: CategoryInSchema):
    data = payload.dict()
    data["author"] = request.user.site_user
    return Category.objects.create(**data)


@router.post("subscribe", response=SubscriptionSchema)
def create_subscription(request, payload: SubscriptionSchema):
    data = payload.dict()
    data["user_id"] = request.user.site_user.id
    return Subscription.objects.create(**data)
