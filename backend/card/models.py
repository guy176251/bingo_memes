from django.db import models

from user.models import SiteUser
from category.models import Category


class Card(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        SiteUser, related_name="cards_created", on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category, related_name="cards", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_timestamp = models.FloatField(default=0)

    edited_at = models.DateTimeField(auto_now=True)
    edited_timestamp = models.FloatField(default=0)

    best = models.FloatField(default=0)  # wilson score
    hot = models.FloatField(default=0)
    ups = models.IntegerField(default=0)
    votes_total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]


class Tile(models.Model):
    text = models.CharField(max_length=200)
    score = models.FloatField(default=0)
    card = models.ForeignKey(Card, related_name="tiles", on_delete=models.CASCADE)


class Hashtag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    categories = models.ManyToManyField(Category, related_name="hashtags")
    cards = models.ManyToManyField(Card, related_name="hashtags")

    class Meta:
        ordering = ["name"]


class Vote(models.Model):
    user = models.ForeignKey(SiteUser, related_name="votes", on_delete=models.CASCADE)

    card = models.ForeignKey(Card, related_name="votes", on_delete=models.CASCADE)

    up = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ["user", "card"]
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "card_id"], name="user_cant_vote_on_same_card_twice"
            )
        ]
