import logging
from datetime import datetime
from typing import Any, Optional, Union

from category.api import CategoryOutSchema
from category.models import Category
from core.auth import JWTOrReadOnlyAuth
from core.db import Mod, Sign
from core.tools import pprint_color
from django.db import IntegrityError
from django.db.models import (Case, Exists, F, OuterRef, Q, QuerySet, Value,
                              When)
from ninja import ModelSchema, Query, Router, Schema
from ninja.errors import ValidationError
from ninja.pagination import PageNumberPagination, paginate
from pydantic import HttpUrl
from user.api import UserSchema

from .db import best_query, hot_query, upvote_query
from .models import Card, Vote
from .signals import adjust_card_score

router = Router(tags=["card"])
logger = logging.getLogger("debug")


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
    category_id: int


class CardOutListSchema(Schema):
    id: int
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
    card_id: int
    up: bool


def add_card_exceptions(api):
    @api.exception_handler(Card.DoesNotExist)
    def card_not_exist(request, exc):
        return api.create_response(
            request, {"detail": "Not a valid card id."}, status=422
        )


def outgoing_cards(user, **list_kwargs):
    """
    Annotates `upvoted` to all cards in queryset, and prefetchs things
    that are in the `CardOutSchema`. Meant for outgoing cards.
    """

    if user.is_authenticated:
        queries = dict(upvoted=upvote_query(user.site_user))
    else:
        queries = dict()

    sort_types = dict(
        hot=hot_query().desc(),
        best=best_query().desc(),
        new="-created_at",
    )
    sort = list_kwargs.pop("sort", "hot")
    sort_by = sort_types.get(sort, hot_query)

    return (
        Card.objects.filter(**list_kwargs)
        .prefetch_related("hashtags")
        .annotate(
            **queries,
            hot=hot_query(),
            best=best_query(),
        )
        .order_by(sort_by)
        .distinct()
    )


@router.get("{int:card_id}", response=CardOutSchema)
def get_card(request, card_id: int):
    cards = outgoing_cards(request.user)
    return cards.get(pk=card_id)


@router.get("", response=list[CardOutListSchema], url_name="list")
@paginate(PageNumberPagination)
def list_cards(request, sort: str = "hot", hashtags: list[str] = Query(None), **kwargs):
    list_kwargs: dict[str, Any] = dict(sort=sort)
    if hashtags:
        list_kwargs["hashtags__name__in"] = hashtags
    return outgoing_cards(request.user, **list_kwargs)


@router.post("", response=CardInSchema)
def create_card(request, payload: CardInSchema):
    data = payload.dict()
    data["author"] = request.user.site_user
    return Card.objects.create(**data)


@router.post("vote")
def create_vote(request, payload: VoteSchema):
    user_id = request.user.site_user.id
    card_id = payload.card_id
    up = payload.up

    votes_up = F("votes_up")
    votes_down = F("votes_down")

    if up:
        up_query = Case(When(Q(votes_up=0), then=1), default=0)
        votes_up = (votes_up + 1) % 2
    else:
        up_query = Case(When(Q(votes_down=0), then=-1), default=0)
        votes_down = (votes_down + 1) % 2

    votes_updated = Vote.objects.filter(user_id=user_id, card_id=card_id).update(
        votes_up=votes_up,
        votes_down=votes_down,
        up=up_query,
    )

    if not votes_updated:
        field = "votes_up" if up else "votes_down"
        data = {field: 1, "up": 1 if up else -1}
        Vote.objects.create(**data, user_id=user_id, card_id=card_id)

    adjust_card_score(card_id=card_id, update=True)
