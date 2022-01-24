import auto_prefetch
from django.db import models
from user.models import SiteUser


class Category(auto_prefetch.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon_url = models.CharField(max_length=2000, default="")
    banner_url = models.CharField(max_length=2000, default="")
    description = models.CharField(max_length=200, default="")

    author = auto_prefetch.ForeignKey(
        SiteUser, related_name="categories_created", on_delete=models.CASCADE
    )

    subscribers = models.ManyToManyField(
        SiteUser, through="Subscription", related_name="subscriptions"
    )

    class Meta:
        ordering = ["-created_at"]


class Subscription(auto_prefetch.Model):
    user = auto_prefetch.ForeignKey(SiteUser, on_delete=models.CASCADE)
    category = auto_prefetch.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ['user', 'category']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category"], name="unique_subscription"
            )
        ]
