import re
from typing import Any

from django.db import models
from django.db.models import F

from card.models import Card


class ModelNames:
    CARD = "card.Card"
    PROFILE = "user.Profile"
    HASHTAG = "Hashtag"
    HASHTAG_CARD = "HashtagCard"
    HASHTAG_PROFILE = "HashtagProfile"


class Hashtag(models.Model):
    NAME_LENGTH = Card.TITLE_LENGTH - 1

    name = models.CharField(
        max_length=NAME_LENGTH,
        unique=True,
        primary_key=True,
    )
    cards = models.ManyToManyField(
        ModelNames.CARD,
        related_name="hashtags",
        through=ModelNames.HASHTAG_CARD,
    )
    subscribers = models.ManyToManyField(
        ModelNames.PROFILE,
        related_name="subscriptions",
        through=ModelNames.HASHTAG_PROFILE,
    )

    class QuerySet(models.QuerySet):
        def subscribe(self, profile_id: int, hashtag_id: str):
            """
            Subscribes a user to a hashtag.
            """
            HashtagProfile.objects.update_subscription(profile_id=profile_id, hashtag_id=hashtag_id)

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
            HashtagCard.objects.bulk_create(
                [HashtagCard(hashtag_id=name, card_id=card_id) for name in hashtag_names],
                ignore_conflicts=True,
            )

    objects: Any = QuerySet.as_manager()


class HashtagProfile(models.Model):
    hashtag = models.ForeignKey(ModelNames.HASHTAG, on_delete=models.CASCADE)
    profile = models.ForeignKey(ModelNames.PROFILE, on_delete=models.CASCADE)
    is_subscribed = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["hashtag", "profile"],
                name="unique_hashtag_subscription",
            )
        ]

    class QuerySet(models.QuerySet):
        def update_subscription(self, profile_id: int, hashtag_id: str):
            subscriptions_updated = self.filter(
                hashtag_id=hashtag_id,
                profile_id=profile_id,
            ).update(is_subscribed=(F("is_subscribed") + 1) % 2)

            if not subscriptions_updated:
                self.create(hashtag_id=hashtag_id, profile_id=profile_id)

    objects: Any = QuerySet.as_manager()


class HashtagCard(models.Model):
    hashtag = models.ForeignKey(ModelNames.HASHTAG, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["hashtag", "card"],
                name="unique_hashtag_card",
            )
        ]
