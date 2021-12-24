from django.db import models

from user.models import SiteUser


class Follow(models.Model):
    follower = models.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_to"
    )
    followee = models.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_from"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ['user', 'following']
        constraints = [
            models.UniqueConstraint(
                fields=["followee", "follower"], name="unique_follow"
            )
        ]
