from django.db.models import F
from ninja import Router
from ninja.pagination import PageNumberPagination, paginate

from .models import Category, Subscription
from .querysets import outgoing_categories
from .schema import (
    CategoryCreateSchema,
    CategoryDetailSchema,
    CategoryListSchema,
    SubscriptionSchema,
)

router = Router()


@router.get("{int:category_id}", response=CategoryDetailSchema, operation_id="category_get")
def get_category(request, category_id: int):
    return outgoing_categories(request.user).get(pk=category_id)


@router.get("", response=list[CategoryListSchema], operation_id="category_list")
@paginate(PageNumberPagination)
def list_categories(request, **kwargs):
    return outgoing_categories(request.user)


@router.post("", response=CategoryDetailSchema, operation_id="category_create")
def create_category(request, payload: CategoryCreateSchema):
    data = payload.dict()
    data["author"] = request.user.profile
    return Category.objects.create(**data)


@router.post("subscribe", operation_id="subscribe_category")
def create_subscription(request, payload: SubscriptionSchema):
    data = payload.dict()
    data["user_id"] = request.user.profile.id
    # return Subscription.objects.create(**data)
    subscriptions_updated = Subscription.objects.filter(**data).update(
        is_subscribed=(F("is_subscribed") + 1) % 2
    )

    if not subscriptions_updated:
        Subscription.objects.create(**data)
