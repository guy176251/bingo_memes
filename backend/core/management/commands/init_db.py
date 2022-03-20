from random import randint, sample

from django.core.management.base import BaseCommand
from django.db.transaction import atomic

from card.factories import CardFactory
from card.models import Card
from user.factories import AuthUserFactory


class Command(BaseCommand):
    @atomic
    def handle(self, *args, **options):
        authors = AuthUserFactory.create_batch(5)
        cards = []

        for author in authors:
            cards.extend(CardFactory.create_batch(20, author=author.profile))

        voters = AuthUserFactory.create_batch(30)
        for voter in voters:
            batch = sample(cards, randint(10, 50))
            for card in batch:
                Card.objects.vote(up=True, card_id=card.id, profile_id=voter.profile.id)
