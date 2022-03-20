"""
Should mostly contain app-facing models and queryset methods.
"""

import re
from dataclasses import dataclass
from typing import Any

from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.db.models import Q

from .base import CardBase, HashtagBase
from .const import ModelNames, UserType
from .plumbing import CardBaseQS, HashtagSub, HashtagToCard, Vote
from .relations import CardRelations, HashtagRelations


@dataclass
class VoteResult:
    vote_updated: int
    vote_created: int
    card_updated: int


class Card(CardBase, CardRelations):

    is_init = models.BooleanField(default=False)

    def init(self):
        """
        Method that is called on card creation.
        Sets values, creates related items, then calls `save`.
        Can only resolve if `self.init` is False.
        """

        if self.is_init:
            return

        Vote.objects.create(card=self, profile=self.author, up=True)
        Hashtag.objects.bulk_create_hashtags(string=self.title, card_id=self.id)

        self.up = 1
        self.total = 1
        self.score = 1
        self.created_timestamp = self.created_at.timestamp()
        self.is_init = True

        self.save()

    class Meta:
        ordering = ["-created_at"]

    class QuerySet(CardBaseQS):
        def search(self, search: str):
            if not search:
                return self

            query = Q(title__icontains=search)
            for tile in Card.TILE_FIELDS:
                query |= Q(**{f"{tile}__icontains": search})

            return self.filter(query)

        def outgoing(self, user=None, sort: str = None, search: str = ""):

            user = user or AnonymousUser()
            sort = sort or "hot"

            return self.search(search).prefetch_outgoing().annotate_upvoted(user).order_hot(sort)

        def home(self, user, sort: str = None):
            if not user.is_authenticated:
                return self.outgoing(sort=sort)

            return self.filter_hashtag_subs(user.profile).outgoing(user=user, sort=sort)

        def vote(self, up: bool, card_id: int, profile_id: int) -> VoteResult:
            result = Vote.objects.update_vote(
                up=up,
                card_id=card_id,
                profile_id=profile_id,
            )
            updated = self.update_score(card_id=card_id)

            return VoteResult(
                vote_created=result.created,
                vote_updated=result.updated,
                card_updated=updated,
            )

    objects: Any = QuerySet.as_manager()


class Hashtag(HashtagBase, HashtagRelations):
    class Queryset(models.QuerySet):
        def subscribe(self, profile_id: int, hashtag_id: str):
            """
            Subscribes a user to a hashtag.
            """
            HashtagSub.objects.update_subscription(profile_id=profile_id, hashtag_id=hashtag_id)

        def bulk_create_hashtags(self, string: str, card_id: int):
            """
            Parses string for hashtags and creates them.
            """

            hashtag_names = set(
                word.lower() for word in re.findall(r"#(\w+)", string) if len(word) <= 20
            )
            self.bulk_create(
                [Hashtag(name=h) for h in hashtag_names],
                ignore_conflicts=True,
            )
            HashtagToCard.objects.bulk_create(
                [HashtagToCard(hashtag_id=name, card_id=card_id) for name in hashtag_names],
                ignore_conflicts=True,
            )

    objects: Any = Queryset.as_manager()


assert Card.__name__ == ModelNames.CARD
assert Vote.__name__ == ModelNames.VOTE
assert Hashtag.__name__ == ModelNames.HASHTAG
assert HashtagToCard.__name__ == ModelNames.HASHTAG_CARD
assert HashtagSub.__name__ == ModelNames.HASHTAG_PROFILE
