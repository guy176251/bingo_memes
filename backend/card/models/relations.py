from django.db import models

from .const import ModelNames


class CardRelations(models.Model):
    author = models.ForeignKey(
        ModelNames.PROFILE,
        related_name="cards_created",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class VoteRelations(models.Model):
    CONSTRAINTS = [
        models.UniqueConstraint(
            fields=["profile", "card"],
            name="user_cant_vote_on_same_card_twice",
        )
    ]

    profile = models.ForeignKey(
        ModelNames.PROFILE,
        related_name="votes",
        on_delete=models.CASCADE,
    )
    card = models.ForeignKey(  # type: ignore
        ModelNames.CARD,
        related_name="votes",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class HashtagRelations(models.Model):
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

    class Meta:
        abstract = True


class HashtagProfileRelations(models.Model):
    CONSTRAINTS = [
        models.UniqueConstraint(
            fields=["hashtag", "profile"],
            name="unique_hashtag_subscription",
        )
    ]

    hashtag = models.ForeignKey(ModelNames.HASHTAG, on_delete=models.CASCADE)  # type: ignore
    profile = models.ForeignKey(ModelNames.PROFILE, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class HashtagCardRelations(models.Model):
    CONSTRAINTS = [
        models.UniqueConstraint(
            fields=["hashtag", "card"],
            name="unique_hashtag_card",
        )
    ]

    hashtag = models.ForeignKey(ModelNames.HASHTAG, on_delete=models.CASCADE)  # type: ignore
    card = models.ForeignKey(ModelNames.CARD, on_delete=models.CASCADE)  # type: ignore

    class Meta:
        abstract = True
