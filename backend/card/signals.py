from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
    post_init,
    pre_init,
    pre_delete,
    post_delete,
)
from .models import Vote, Card, Hashtag
from user.models import SiteUser
from libreddit_sort import hot_score, best_score
from django.db.transaction import atomic
import re


def create_unix_timestamp(card: Card):
    # get unix timestamp
    card.created_timestamp = card.created_at.timestamp()
    card.save()


def create_hashtags(card: Card):
    # parse bingo card name for first 4 hashtags and create them, then add them to card and category
    hashtags_text = re.findall(r"#(\w+)", card.name)[:4]

    Hashtag.objects.bulk_create(
        [Hashtag(name=h.lower()) for h in hashtags_text if len(h) <= 20],
        ignore_conflicts=True,
    )

    hashtags = Hashtag.objects.filter(name__in=hashtags_text)

    card.hashtags.add(*hashtags)
    card.category.hashtags.add(*hashtags)


def adjust_card_scores(card: Card):
    votes = card.votes
    up = votes.filter(up=True).count()
    total = votes.count()
    score = up - (total - up)

    card.hot = hot_score(up, total, card.created_timestamp)
    card.best = best_score(up, total)
    card.score = score

    # with atomic():
    card.save()

    author = card.author
    author.score = author.cards_created.aggregate(Sum("score"))["score__sum"]
    author.save()


@receiver(post_save, sender=Card)
def card_post_create(sender: Card, instance: Card, created: bool, **kwargs):
    if not created:
        return

    create_unix_timestamp(instance)
    create_hashtags(instance)

    Vote.objects.create(card=instance, user=instance.author, up=True)


@receiver(post_save, sender=Vote)
def increase_card_scores(sender: Vote, instance: Vote, created: bool, **kwargs):
    card = instance.card
    adjust_card_scores(card)


@receiver(post_delete, sender=Vote)
def decrease_card_scores(sender: Vote, instance: Vote, using, **kwargs):
    card = instance.card
    adjust_card_scores(card)
