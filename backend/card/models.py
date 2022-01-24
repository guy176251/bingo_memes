import auto_prefetch
from category.models import Category
from django.db import models
from user.models import SiteUser


def tile_field():
    return models.CharField(max_length=200)


class Card(auto_prefetch.Model):
    name = models.CharField(max_length=50)
    author = auto_prefetch.ForeignKey(
        SiteUser, related_name="cards_created", on_delete=models.CASCADE
    )

    category = auto_prefetch.ForeignKey(
        Category, related_name="cards", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_timestamp = models.FloatField(default=0)

    edited_at = models.DateTimeField(auto_now=True)
    edited_timestamp = models.FloatField(default=0)

    # best = models.FloatField(default=0)  # wilson score
    # hot = models.FloatField(default=0)

    up = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

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


# tile_fields = [f'tile_{n}' for n in range(1, 26)]
# for each in tile_fields:
#     Card.add_to_class(each, models.CharField(max_length=200))


# class Tile(auto_prefetch.Model):
#     text = models.CharField(max_length=200)
#     score = models.FloatField(default=0)
#     card = auto_prefetch.ForeignKey(Card, related_name="tiles", on_delete=models.CASCADE)


class Hashtag(auto_prefetch.Model):
    name = models.CharField(max_length=20, unique=True)
    categories = models.ManyToManyField(
        Category,
        related_name="hashtags",
        through="HashtagRelation",
        # through_fields=["hashtag", "category"],
    )
    cards = models.ManyToManyField(
        Card,
        related_name="hashtags",
        through="HashtagRelation",
        # through_fields=["hashtag", "card"],
    )

    class Meta:
        ordering = ["name"]


class HashtagRelation(auto_prefetch.Model):
    hashtag = auto_prefetch.ForeignKey(Hashtag, on_delete=models.CASCADE)
    card = auto_prefetch.ForeignKey(Card, on_delete=models.CASCADE)
    category = auto_prefetch.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["hashtag", "card", "category"],
                name="reduce_dupes",
            ),
            # models.UniqueConstraint(
            #     fields=["hashtag", "card"],
            #     name="unique_card",
            # ),
            # models.UniqueConstraint(
            #     fields=["hashtag", "category"],
            #     name="unique_category",
            # )
        ]


class Vote(auto_prefetch.Model):
    user = auto_prefetch.ForeignKey(
        SiteUser, related_name="votes", on_delete=models.CASCADE
    )
    card = auto_prefetch.ForeignKey(
        Card, related_name="votes", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # up = models.BooleanField()

    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    up = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "card"], name="user_cant_vote_on_same_card_twice"
            )
        ]

    def __str__(self):
        return (
            f"card = {self.card_id}, "
            f"user = {self.user_id}, "
            f"votes_down = {self.votes_down}, "
            f"votes_up = {self.votes_up}, "
            f"up = {self.up} "
        )
