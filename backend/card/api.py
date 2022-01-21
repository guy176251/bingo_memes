import logging
from datetime import datetime
from typing import Optional

from category.api import CategoryOutSchema
from category.models import Category
from core.auth import JWTOrReadOnlyAuth
from core.tools import pprint_color
from django.db import IntegrityError
from django.db.models import (Case, Exists, F, OuterRef, Q, QuerySet, Value,
                              When)
from ninja import ModelSchema, Query, Router, Schema
from ninja.errors import ValidationError
from ninja.pagination import PageNumberPagination, paginate
from pydantic import HttpUrl
from user.api import UserSchema

from .models import Card, Vote

router = Router(tags=["card"])
logger = logging.getLogger("debug")


class IDSchema(Schema):
    id: int


class TileSchema(Schema):
    tile_1: str
    tile_2: str
    tile_3: str
    tile_4: str
    tile_5: str
    tile_6: str
    tile_7: str
    tile_8: str
    tile_9: str
    tile_10: str
    tile_11: str
    tile_12: str
    tile_13: str
    tile_14: str
    tile_15: str
    tile_16: str
    tile_17: str
    tile_18: str
    tile_19: str
    tile_20: str
    tile_21: str
    tile_22: str
    tile_23: str
    tile_24: str
    tile_25: str


class HashtagSchema(Schema):
    name: str


class CardInSchema(TileSchema):
    id: Optional[int]
    name: str
    category: IDSchema


class CardOutListSchema(Schema):
    name: str
    author: UserSchema
    hashtags: list[HashtagSchema]
    created_at: datetime
    edited_at: datetime
    best: float
    hot: float
    score: int
    upvoted: Optional[bool]


class CardOutSchema(CardOutListSchema, TileSchema):
    pass


class VoteSchema(Schema):
    user_id: Optional[int]
    card_id: int
    up: bool


def add_card_exceptions(api):
    @api.exception_handler(Card.DoesNotExist)
    def card_not_exist(request, exc):
        return api.create_response(
            request, {"detail": "Not a valid card id."}, status=422
        )


def annotated_cards(cards: QuerySet, user):
    upvoted_cards = cards.annotate(
        upvoted=Case(
            When(
                Exists(Vote.objects.filter(card=OuterRef("pk"), user=user, up=True)),
                then=True,
            ),
            When(
                Exists(Vote.objects.filter(card=OuterRef("pk"), user=user, up=False)),
                then=False,
            ),
            default=None,
        )
    )
    # breakpoint()
    return upvoted_cards


def outgoing_cards(auth):
    """
    Annotates `upvoted` to all cards in queryset, and prefetchs things
    that are in the `CardOutSchema`. Meant for outgoing cards.
    """

    cards = Card.objects.prefetch_related("author", "hashtags")
    if auth.is_authenticated:
        print("Calculating Votes: True")
        return annotated_cards(cards, auth.site_user)
    else:
        print("Calculating Votes: False")
        return cards


@router.get("{int:card_id}", response=CardOutSchema)
def get_card(request, card_id: int):
    cards = outgoing_cards(request.user)
    return cards.get(pk=card_id)


@router.get("", response=list[CardOutListSchema], url_name="list")
@paginate(PageNumberPagination)
def list_cards(request, hashtags: list[str] = Query(None), **kwargs):
    cards = outgoing_cards(request.user)
    if hashtags:
        return cards.filter(hashtags__name__in=hashtags).distinct()
    else:
        return cards


@router.post("", response=CardInSchema)
def create_card(request, payload: CardInSchema):
    category = Category.objects.get(pk=payload.category.id)
    data = payload.dict()
    data["author"] = request.user.site_user
    data["category"] = category
    return Card.objects.create(**data)


@router.post("vote")
def create_vote(request, payload: VoteSchema):
    data = payload.dict()
    data["user_id"] = request.user.site_user.id

    try:
        vote, created = Vote.objects.get_or_create(**data)
    except IntegrityError:
        up = data.pop("up")
        vote = Vote.objects.filter(**data).first()
        vote.up = up
        vote.save()
    else:
        if not created:
            vote.delete()
