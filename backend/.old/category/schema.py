import re
from datetime import datetime
from typing import Optional

from ninja import Schema
from pydantic import HttpUrl, constr, validator

from user.schema import UserListSchema

from .models import MaxLength


class HashtagSchema(Schema):
    name: str


class SubscriptionSchema(Schema):
    category_id: int


class CategoryCreateSchema(Schema):
    name: constr(max_length=MaxLength.CATEGORY_NAME)
    description: constr(max_length=MaxLength.CATEGORY_DESCRIPTION)
    icon_url: HttpUrl
    banner_url: HttpUrl

    @validator("name")
    def validate_name(cls, name):
        match = re.match(r"^\w+$", name)
        if not match:
            raise ValueError("Name can only contain numbers, letters and _.")
        return name


class CategoryListSchema(Schema):
    id: int
    name: str
    created_at: datetime
    description: str
    icon_url: HttpUrl
    is_subscribed: Optional[bool]


class CategoryDetailSchema(CategoryListSchema):
    author: UserListSchema
    banner_url: HttpUrl
    hashtags: list[HashtagSchema]
