"""
Should mostly contain through models and base-level queryset methods.
"""

from dataclasses import dataclass
from typing import Any

from django.db import models
from django.db.models import Case, Exists, F, OuterRef, Q, Subquery, Value, When
from sql_util.utils import SubqueryCount

from core.db import Abs, Log10, Sign, Sqrt

from .base import HashtagProfileBase, VoteBase
from .const import UserType
from .relations import HashtagCardRelations, HashtagProfileRelations, VoteRelations


class CardBaseQS(models.QuerySet):
    def order_hot(self, sort: str):
        sort_types = {
            "hot": "-hot",
            "best": "-best",
            "new": "-created_at",
        }
        sort_algos = {
            "hot": CardQueries.hot(),
            "best": CardQueries.best(),
        }
        sort = sort if sort in sort_types else "hot"
        algo = {}
        if sort in sort_algos:
            algo[sort] = sort_algos[sort]

        return self.annotate(**algo).order_by(sort_types[sort])

    def annotate_upvoted(self, user: UserType):
        return self.annotate(is_upvoted=CardQueries.is_upvoted(user))

    def prefetch_outgoing(self):
        return self.select_related("author")

    def update_score(self, card_id: int) -> int:
        """
        Calculates the and updates the score of a card.
        """

        updated = (
            self.filter(id=card_id)
            .annotate(
                a_up=SubqueryCount("votes", filter=Q(up=1)),
                a_total=SubqueryCount("votes", filter=~Q(up=0)),
                a_score=SubqueryCount("votes", filter=Q(up=1))
                - SubqueryCount("votes", filter=Q(up=-1)),
            )
            .update(
                up=F("a_up"),
                total=F("a_total"),
                score=F("a_score"),
            )
        )

        return updated

    def filter_hashtag_subs(self, profile: Any):
        return self.filter(
            hashtags__in=Subquery(HashtagSub.objects.filter(profile=profile).values("hashtag"))
        )


@dataclass
class VoteUpdateResult:
    created: int
    updated: int


class Vote(VoteBase, VoteRelations):
    class Meta:
        constraints = VoteRelations.CONSTRAINTS

    class QuerySet(models.QuerySet):
        def update_vote(self, up: bool, card_id: int, profile_id: int) -> VoteUpdateResult:
            """
            Updates the state of a card vote. Creates new vote if it doesn't exist.
            """

            up_state = F("up_state")
            down_state = F("down_state")

            if up:
                up_query = Case(When(Q(up_state=0), then=1), default=0)
                up_state = (up_state + 1) % 2
            else:
                up_query = Case(When(Q(down_state=0), then=-1), default=0)
                down_state = (down_state + 1) % 2

            created = 0
            updated = self.filter(profile_id=profile_id, card_id=card_id).update(
                up_state=up_state,
                down_state=down_state,
                up=up_query,
            )

            if not updated:
                field = "up_state" if up else "down_state"
                data = {field: 1, "up": 1 if up else -1}
                self.create(**data, profile_id=profile_id, card_id=card_id)
                created = 1

            return VoteUpdateResult(created=created, updated=updated)

    objects: Any = QuerySet.as_manager()


class HashtagSub(HashtagProfileBase, HashtagProfileRelations):
    class Meta:
        constraints = HashtagProfileRelations.CONSTRAINTS

    class QuerySet(models.QuerySet):
        def update_subscription(self, profile_id: int, hashtag_id: str):
            subscriptions_updated = self.filter(
                hashtag_id=hashtag_id,
                profile_id=profile_id,
            ).update(is_subscribed=(F("is_subscribed") + 1) % 2)

            if not subscriptions_updated:
                self.create(hashtag_id=hashtag_id, profile_id=profile_id)

    objects: Any = QuerySet.as_manager()


class HashtagToCard(HashtagCardRelations):
    class Meta:
        constraints = HashtagCardRelations.CONSTRAINTS


class CardQueries:
    @staticmethod
    def hot():
        """
        Scoring equation that emulates reddit's "hot" scoring.
        """

        score_or_1 = Case(When(Q(score=0), then=1), default=F("score"))

        return (
            Sign(F("score")) * Log10(Abs(score_or_1))
            + (F("created_timestamp") - 1134028003) / 45000
        )

    @staticmethod
    def best():
        """
        Scoring equation that emulates reddit's "best" scoring.
        """

        up = F("up")
        total = F("total")

        # z = 1.96
        z = 1.28  # 80% confidence
        p = up / total

        left = p + z * z / (2.0 * total)
        s = (p * (1.0 - p) + z * z / (4.0 * total)) / total
        right = z * Sqrt(s)
        under = 1.0 + z * z / total

        best = (left - right) / under

        return Case(When(score=0, then=0.0), default=best)

    @staticmethod
    def is_upvoted(user):
        """
        Evaluates whether a user has voted on a card.
        """

        if not user.is_authenticated:
            # hack to annotate None value
            return Value(None, models.BooleanField(null=True))

        def vote_exists(up: int):
            return Exists(
                Vote.objects.filter(
                    card=OuterRef("pk"),
                    profile=user.profile,
                    up=up,
                )
            )

        return Case(
            When(vote_exists(0), then=None),
            When(vote_exists(1), then=True),
            When(vote_exists(-1), then=False),
            default=None,
        )
