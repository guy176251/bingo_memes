from django.db import models

# from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AuthUser(AbstractUser):
    """
    Custom user to use email instead of username for authentication
    """

    # email = models.EmailField("Email Address", unique=True)

    # username = None
    # objects = UserManager()

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS: list[str] = []


class SiteUser(models.Model):
    username = models.CharField(max_length=20)
    auth = models.OneToOneField(
        AuthUser, related_name="site_user", on_delete=models.CASCADE, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    following = models.ManyToManyField(
        "self", through="Follow", related_name="followers", symmetrical=False
    )


class Follow(models.Model):
    follower = models.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_to"
    )
    followed = models.ForeignKey(
        SiteUser, on_delete=models.CASCADE, related_name="follows_from"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ['user', 'following']
        constraints = [
            models.UniqueConstraint(
                fields=["followed_id", "follower_id"], name="unique_follow"
            )
        ]
