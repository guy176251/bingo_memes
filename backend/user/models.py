from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Exists, F, OuterRef


class AuthUserManager(UserManager):
    def get(self, *args, **kwargs):
        return super().select_related("profile").get(*args, **kwargs)


class AuthUser(AbstractUser):
    USERNAME_LENGTH = 20
    REQUIRED_FIELDS = ["email"]

    objects = AuthUserManager()

    username = models.CharField(max_length=USERNAME_LENGTH, unique=True)

    def create_profile(self):
        """
        Creates a profile for a user. Is called whenever a user is created.
        """
        return Profile.objects.create(username=self.username, user=self)


class Profile(models.Model):
    """
    Represents a user profile.
    """

    username = models.CharField(max_length=AuthUser.USERNAME_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        AuthUser,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    following = models.ManyToManyField(
        "self",
        through="Follow",
        related_name="followers",
        symmetrical=False,
    )

    class QuerySet(models.QuerySet):
        def annotate_following(self, user: AuthUser):
            return (
                self.annotate(
                    is_following=Exists(
                        Follow.objects.filter(
                            followed=OuterRef("pk"),
                            follower=user.profile,
                            is_following=1,
                        )
                    )
                )
                if user.is_authenticated
                else self
            )

        def prefetch_custom(self, detail: bool):
            return self.prefetch_related("followers", "following") if detail else self

        def outgoing(self, user: AuthUser, detail: bool = False):
            return self.prefetch_custom(detail).annotate_following(user)

        def follow(self, follower_id: int, followed_id: int) -> int:
            return Follow.objects.update_follow(
                followed_id=followed_id,
                follower_id=follower_id,
            )

    objects: Any = QuerySet.as_manager()


class Follow(models.Model):

    follower = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="follows_to",
    )
    followed = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="follows_from",
    )
    created_at = models.DateTimeField(auto_now=True)
    is_following = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["followed_id", "follower_id"],
                name="unique_follow",
            )
        ]

    class QuerySet(models.QuerySet):
        def update_follow(self, follower_id: int, followed_id: int) -> int:
            num_updated = self.filter(follower_id=follower_id, followed_id=followed_id).update(
                is_following=(F("is_following") + 1) % 2
            )
            if not num_updated:
                self.create(follower_id=follower_id, followed_id=followed_id)

            return num_updated

    objects: Any = QuerySet.as_manager()
