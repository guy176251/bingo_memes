from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AuthUser


@receiver(post_save, sender=AuthUser)
def user_post_create(sender: AuthUser, instance: AuthUser, created: bool, **kwargs):
    if not created:
        # print("User post-save: Not created, returning")
        return

    # print("User post-save: Created profile")
    instance.create_profile()
