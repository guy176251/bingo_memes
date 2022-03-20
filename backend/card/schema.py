from datetime import datetime
from typing import Optional

from ninja import ModelSchema, Schema

from backend.settings import DEBUG
from user.schema import UserListSchema

from .models import Card


class HashtagSchema(Schema):
    name: str


class VoteSchema(Schema):
    card_id: int
    up: bool


class TileSchema(ModelSchema):
    class Config:
        model = Card
        model_fields = Card.TILE_FIELDS


class CardCreateSchema(ModelSchema):
    id: Optional[int] = None

    class Config:
        model = Card
        model_fields = Card.TILE_FIELDS + ["title"]


class CardListBase(Schema):
    id: int
    title: str
    author: UserListSchema
    created_at: datetime
    edited_at: datetime
    score: int
    is_upvoted: Optional[bool]


if DEBUG:

    class CardListSchema(CardListBase):
        best: Optional[float]
        hot: Optional[float]

else:

    class CardListSchema(CardListBase):  # type: ignore
        pass


print(f"{DEBUG = }")


class CardDetailSchema(CardListSchema, TileSchema):
    pass


class CardUpdateSchema(Schema):
    title: Optional[str]
    tile_1: Optional[str]
    tile_2: Optional[str]
    tile_3: Optional[str]
    tile_4: Optional[str]
    tile_5: Optional[str]
    tile_6: Optional[str]
    tile_7: Optional[str]
    tile_8: Optional[str]
    tile_9: Optional[str]
    tile_10: Optional[str]
    tile_11: Optional[str]
    tile_12: Optional[str]
    tile_13: Optional[str]
    tile_14: Optional[str]
    tile_15: Optional[str]
    tile_16: Optional[str]
    tile_17: Optional[str]
    tile_18: Optional[str]
    tile_19: Optional[str]
    tile_20: Optional[str]
    tile_21: Optional[str]
    tile_22: Optional[str]
    tile_23: Optional[str]
    tile_24: Optional[str]
    tile_25: Optional[str]
