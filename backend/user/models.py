import auto_prefetch
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def get(self, *args, **kwargs):
        return super().select_related("site_user").get(*args, **kwargs)


class AuthUser(AbstractUser):
    """
    Custom user to use email instead of username for authentication
    """

    objects = CustomUserManager()


class SiteUser(auto_prefetch.Model):
    username = models.CharField(max_length=20)
    auth = auto_prefetch.OneToOneField(
        AuthUser, related_name="site_user", on_delete=models.CASCADE, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    following = models.ManyToManyField(
        "self", through="Follow", related_name="followers", symmetrical=False
    )


class Follow(auto_prefetch.Model):
    follower = auto_prefetch.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_to"
    )
    followed = auto_prefetch.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_from"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["followed_id", "follower_id"], name="unique_follow"
            )
        ]
