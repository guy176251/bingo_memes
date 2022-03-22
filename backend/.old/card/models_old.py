import re
from dataclasses import dataclass
from typing import Any

from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.db.models import Case, Count, Exists, F, OuterRef, Q, Subquery, Value, When

from core.db import Abs, Log10, Sign, Sqrt
from user.models import AuthUser, Profile


def hot_score():
    """
    Scoring equation that emulates reddit's "hot" scoring.
    """

    score_or_1 = Case(When(Q(score=0), then=1), default=F("score"))

    return Sign(F("score")) * Log10(Abs(score_or_1)) + (F("created_timestamp") - 1134028003) / 45000


def best_score():
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


def is_upvoted(user: AuthUser):
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


@dataclass
class VoteResult:
    vote_updated: int
    vote_created: int
    card_updated: int


class CardQuerySet(models.QuerySet):
    """
    You know what it do.
    """

    ######################
    # IMPERATIVE METHODS #
    ######################

    def order_hot(self, sort: str):
        sort_types = {
            "hot": "-hot",
            "best": "-best",
            "new": "-created_at",
        }
        sort_algos = {
            "hot": hot_score(),
            "best": best_score(),
        }
        sort = sort if sort in sort_types else "hot"
        algo = {}
        if sort in sort_algos:
            algo[sort] = sort_algos[sort]
        return self.annotate(**algo).order_by(sort_types[sort])

    def annotate_upvoted(self, user: AuthUser):
        return self.annotate(is_upvoted=is_upvoted(user))

    def prefetch_outgoing(self):
        return self.select_related("author")

    def update_score(self, card_id: int) -> int:
        """
        Calculates the and updates the score of a card.
        """

        # https://stackoverflow.com/a/65613047
        def vote_count(query):
            return Subquery(
                Vote.objects.filter(card_id=OuterRef("pk"))
                .values("card")
                .annotate(count=query)
                .values("count")
            )

        def count(query):
            return Count("card_id", filter=query)

        up = count(Q(up=1))
        down = count(Q(up=-1))
        total = count(~Q(up=0))

        updated = self.filter(id=card_id).update(
            up=vote_count(up),
            total=vote_count(total),
            score=vote_count(up - down),
        )

        return updated

    def filter_hashtag_subs(self, profile: Profile):
        return self.filter(
            hashtags__in=Subquery(HashtagSub.objects.filter(profile=profile).values("hashtag"))
        )

    #######################
    # DECLARATIVE METHODS #
    #######################

    def search(self, search: str):
        if not search:
            return self

        query = Q(title__icontains=search)
        for tile in Card.TILE_FIELDS:
            query |= Q(**{f"{tile}__icontains": search})

        return self.filter(query)

    def outgoing(
        self,
        user: AuthUser | AnonymousUser | None = None,
        sort: str = None,
        search: str = "",
    ):
        user = user or AnonymousUser()
        sort = sort or "hot"

        return self.search(search).prefetch_outgoing().annotate_upvoted(user).order_hot(sort)

    def home(self, user: AuthUser, sort: str = None):
        """
        Grabs cards for user that either:
            - belong to a subscribed hashtag
            - or, belong to a followed user

        idk how useful having cards from a user is, really...
        """

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


TILE_LENGTH = 200


class Card(models.Model):
    TILE_FIELDS = [f"tile_{n}" for n in range(1, 26)]
    TILE_LENGTH = TILE_LENGTH
    TITLE_LENGTH = 50

    objects: Any = CardQuerySet.as_manager()

    title = models.CharField(max_length=TILE_LENGTH)
    author = models.ForeignKey(
        Profile,
        related_name="cards_created",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_timestamp = models.FloatField(default=0)

    edited_at = models.DateTimeField(auto_now=True)
    edited_timestamp = models.FloatField(default=0)

    up = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    @staticmethod
    def tile_field():
        return models.CharField(max_length=TILE_LENGTH)

    tile_1 = tile_field()
    tile_2 = tile_field()
    tile_3 = tile_field()
    tile_4 = tile_field()
    tile_5 = tile_field()
    tile_6 = tile_field()
    tile_7 = tile_field()
    tile_8 = tile_field()
    tile_9 = tile_field()
    tile_10 = tile_field()
    tile_11 = tile_field()
    tile_12 = tile_field()
    tile_13 = tile_field()
    tile_14 = tile_field()
    tile_15 = tile_field()
    tile_16 = tile_field()
    tile_17 = tile_field()
    tile_18 = tile_field()
    tile_19 = tile_field()
    tile_20 = tile_field()
    tile_21 = tile_field()
    tile_22 = tile_field()
    tile_23 = tile_field()
    tile_24 = tile_field()
    tile_25 = tile_field()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return " ".join(
            (
                f"({self.id})",
                f'"{self.title}"',
            )
        )

    def create_hashtags(self):
        """
        Parses title for hashtags and creates them.
        """

        hashtags_text = set(
            word.lower() for word in re.findall(r"#(\w+)", self.title) if len(word) <= 20
        )

        Hashtag.objects.bulk_create(
            [Hashtag(name=h) for h in hashtags_text],
            ignore_conflicts=True,
        )

        HashtagToCard.objects.bulk_create(
            [HashtagToCard(hashtag_id=name, card_id=self.id) for name in hashtags_text],
            ignore_conflicts=True,
        )

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
        self.up = 1
        self.total = 1
        self.score = 1
        self.created_timestamp = self.created_at.timestamp()
        self.create_hashtags()
        self.is_init = True
        self.save()


class HashtagQueryset(models.QuerySet):
    def subscribe(self, profile_id: int, hashtag_id: str):
        """
        Subscribes a user to a hashtag.
        """
        HashtagSub.objects.update_subscription(profile_id=profile_id, hashtag_id=hashtag_id)


class Hashtag(models.Model):
    NAME_LENGTH = Card.TITLE_LENGTH - 1

    objects = HashtagQueryset.as_manager()

    name = models.CharField(
        max_length=NAME_LENGTH,
        unique=True,
        primary_key=True,
    )
    cards = models.ManyToManyField(
        Card,
        related_name="hashtags",
        through="HashtagToCard",
    )
    subscribers = models.ManyToManyField(
        Profile,
        related_name="subscriptions",
        through="HashtagSub",
    )

    class Meta:
        ordering = ["name"]


class HashtagToCard(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["hashtag", "card"],
                name="unique_hashtag_card",
            )
        ]


class HashtagSubQueryset(models.QuerySet):
    def update_subscription(self, profile_id: int, hashtag_id: str):
        """
        where do I put this method?
        """

        subscriptions_updated = self.filter(
            hashtag_id=hashtag_id,
            profile_id=profile_id,
        ).update(is_subscribed=(F("is_subscribed") + 1) % 2)

        if not subscriptions_updated:
            self.create(hashtag_id=hashtag_id, profile_id=profile_id)


class HashtagSub(models.Model):
    objects: Any = HashtagSubQueryset.as_manager()

    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_subscribed = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["hashtag", "profile"],
                name="unique_hashtag_subscription",
            )
        ]


@dataclass
class VoteUpdateResult:
    created: int
    updated: int


class VoteQueryset(models.QuerySet):
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


class Vote(models.Model):
    objects: Any = VoteQueryset.as_manager()

    profile = models.ForeignKey(
        Profile,
        related_name="votes",
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(
        Card,
        related_name="votes",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now=True)

    up_state = models.IntegerField(default=0)
    down_state = models.IntegerField(default=0)
    up = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "card"], name="user_cant_vote_on_same_card_twice"
            )
        ]

    def __str__(self):
        return (
            f"(Card {self.card_id}) "
            f"(User {self.profile_id}) "
            f"down_state = {self.down_state}, "
            f"up_state = {self.up_state}, "
            f"up = {self.up} "
        )
