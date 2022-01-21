from django.db import models
from user.models import SiteUser


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon_url = models.CharField(max_length=2000, default="")
    banner_url = models.CharField(max_length=2000, default="")
    description = models.CharField(max_length=200, default="")

    author = models.ForeignKey(
        SiteUser, related_name="categories_created", on_delete=models.CASCADE
    )

    subscribers = models.ManyToManyField(
        SiteUser, through="Subscription", related_name="subscriptions"
    )

    class Meta:
        ordering = ["-created_at"]


class Subscription(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ['user', 'category']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category"], name="unique_subscription"
            )
        ]
