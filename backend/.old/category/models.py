import auto_prefetch
from django.db import models

from user.models import Profile


class MaxLength:
    CATEGORY_NAME = 20
    CATEGORY_DESCRIPTION = 200
    CATEGORY_ICON_URL = 2083
    CATEGORY_BANNER_URL = 2083


class Category(auto_prefetch.Model):
    name = models.CharField(max_length=MaxLength.CATEGORY_NAME, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon_url = models.CharField(max_length=MaxLength.CATEGORY_ICON_URL, default="")
    banner_url = models.CharField(max_length=MaxLength.CATEGORY_BANNER_URL, default="")
    description = models.CharField(max_length=MaxLength.CATEGORY_DESCRIPTION, default="")

    author = auto_prefetch.ForeignKey(
        Profile, related_name="categories_created", on_delete=models.CASCADE
    )

    subscribers = models.ManyToManyField(
        Profile, through="Subscription", related_name="subscriptions"
    )

    class Meta:
        ordering = ["-created_at"]


class Subscription(auto_prefetch.Model):
    user = auto_prefetch.ForeignKey(Profile, on_delete=models.CASCADE)
    category = auto_prefetch.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_subscribed = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "category"], name="unique_subscription")
        ]
