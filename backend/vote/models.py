from django.db import models

from user.models import SiteUser
from card.models import BingoCard


class Vote(models.Model):
    user = models.ForeignKey(SiteUser, related_name="votes", on_delete=models.CASCADE)
    card = models.ForeignKey(BingoCard, related_name="votes", on_delete=models.CASCADE)
    up = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "card"]
