from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Card


@receiver(post_save, sender=Card)
def card_post_create(sender: Card, instance: Card, created: bool, **kwargs):
    if not created:
        return

    instance.init()
