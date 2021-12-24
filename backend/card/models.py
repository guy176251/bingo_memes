from django.db import models

from user.models import SiteUser
from category.models import BingoCardCategory


class BingoCard(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        SiteUser, related_name="cards_created", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_timestamp = models.FloatField(default=0)

    edited_at = models.DateTimeField(auto_now=True)
    edited_timestamp = models.FloatField(default=0)

    category = models.ForeignKey(
        BingoCardCategory, related_name="cards", on_delete=models.CASCADE
    )

    best = models.FloatField(default=0)  # wilson score
    hot = models.FloatField(default=0)
    ups = models.IntegerField()
    votes_total = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        ordering = ["-created_at"]


class BingoTile(models.Model):
    text = models.CharField(max_length=200)
    score = models.FloatField(default=0)
    card = models.ForeignKey(BingoCard, related_name="tiles", on_delete=models.CASCADE)


class Hashtag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    categories = models.ManyToManyField(BingoCardCategory, related_name="hashtags")
    cards = models.ManyToManyField(BingoCard, related_name="hashtags")

    class Meta:
        ordering = ["name"]
