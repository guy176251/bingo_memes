from typing import Optional
from datetime import datetime
from ninja_jwt.authentication import JWTAuth
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError
from ninja.pagination import paginate, PageNumberPagination
from ninja_extra import NinjaExtraAPI
from pydantic import HttpUrl

from .models import Card, Tile
from category.models import Category
from user.api import UserSchema
from category.api import CategoryOutSchema

api = NinjaExtraAPI(urls_namespace="card")


class IDSchema(Schema):
    id: int


class TileSchema(Schema):
    text: str


class HashtagSchema(Schema):
    name: str


class CardInSchema(Schema):
    id: Optional[int]
    name: str
    category: IDSchema
    tiles: list[TileSchema]


class CardOutSchema(Schema):
    name: str
    author: UserSchema
    tiles: list[TileSchema]
    hashtags: list[HashtagSchema]
    created_at: datetime
    edited_at: datetime
    best: int
    hot: int
    ups: int
    votes_total: int
    score: int


@api.exception_handler(Card.DoesNotExist)
def card_not_exist(request, exc):
    return api.create_response(request, {"detail": "Not a valid card id."}, status=422)


@api.get("{int:card_id}", response=CardOutSchema)
def get_card(request, card_id: int):
    return Card.objects.get(pk=card_id)


@api.post("", response=CardInSchema, auth=JWTAuth())
def create_card(request, payload: CardInSchema):
    if len(payload.tiles) != 25:
        raise ValidationError([{"detail": "Card must have exactly 25 tiles."}])
    category = Category.objects.get(pk=payload.category.id)
    data = payload.dict()
    data["author"] = request.user.site_user
    data["category"] = category
    tile_data = data.pop("tiles")
    card = Card.objects.create(**data)
    Tile.objects.bulk_create([Tile(**each, card=card) for each in tile_data])
    return card
