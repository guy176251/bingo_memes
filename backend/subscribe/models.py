from django.db import models

from user.models import SiteUser
from category.models import BingoCardCategory


class Subscription(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    category = models.ForeignKey(BingoCardCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ['user', 'category']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category"], name="unique_subscription"
            )
        ]
