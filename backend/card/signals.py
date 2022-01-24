import re
from dataclasses import dataclass
from typing import Optional

from core.db import Abs, Log10, Sign, Sqrt
from core.tools import pprint_color
from django.db.models import (Case, Count, Exists, F, Func, OuterRef, Q, Sum,
                              When)
from django.db.models.signals import (post_delete, post_init, post_save,
                                      pre_delete, pre_init, pre_save)
from django.db.transaction import atomic
from django.dispatch import receiver
from libreddit_sort import best_score, hot_score
from user.models import SiteUser

from .models import Card, Hashtag, HashtagRelation, Vote


@dataclass
class CardScore:
    score: int
    up: int
    total: int


@receiver(post_save, sender=Card)
def card_post_create(sender: Card, instance: Card, created: bool, **kwargs):
    if not created:
        return

    print(f"card_id = {instance.id}")

    instance.created_timestamp = instance.created_at.timestamp()

    Vote.objects.create(card=instance, user=instance.author, up=True)
    data = adjust_card_score(instance.id)

    if data:
        instance.up = data.up
        instance.total = data.total
        instance.score = data.score

    create_hashtags(instance)

    instance.save()


def adjust_card_score(card_id: int, update=False) -> Optional[CardScore]:
    data = Vote.objects.filter(card_id=card_id).aggregate(
        total=Count("id", filter=~Q(up=0)),
        up=Count("id", filter=Q(up=1)),
    )
    up = data["up"]
    total = data["total"]
    score = up - (total - up)

    if update:
        Card.objects.filter(id=card_id).update(
            up=up, total=total, score=score
        )
        return None
    else:
        return CardScore(up=up, total=total, score=score)


def create_hashtags(card: Card):
    """
    Parse bingo card name for first 4 hashtags and create them,
    then add them to card and category.
    """

    hashtags_text = list(set(re.findall(r"#(\w+)", card.name)))[:4]

    Hashtag.objects.bulk_create(
        [Hashtag(name=h.lower()) for h in hashtags_text if len(h) <= 20],
        ignore_conflicts=True,
    )

    hashtags = Hashtag.objects.filter(name__in=hashtags_text)
    pprint_color(hashtags)

    HashtagRelation.objects.bulk_create(
        [
            HashtagRelation(hashtag=hashtag, card=card, category_id=card.category_id)
            for hashtag in hashtags
        ],
        # ignore_conflicts=True,
    )
