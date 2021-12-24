from django.db import models
from django.conf import settings


class SiteUser(models.Model):
    name = models.CharField(max_length=20)
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="site_user", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    followers = models.ManyToManyField(
        "self", through="Follow", related_name="following", symmetrical=False
    )
