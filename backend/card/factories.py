import factory
from random import choice, sample, randint
from factory.django import DjangoModelFactory

from .models import Card, Tile
from user.factories import SiteUserFactory
from category.factories import CategoryFactory

hashtags = [
    "viral",
    "popular",
    "music",
    "art",
    "meme",
]


class TileFactory(DjangoModelFactory):
    class Meta:
        model = Tile

    text = factory.Faker("sentence")


class CardFactory(DjangoModelFactory):
    class Meta:
        model = Card

    name = factory.Sequence(
        lambda n: f"Test Card {n} "
        + " ".join(f"#{name}" for name in sample(hashtags, randint(2, 4)))
    )
    author = factory.SubFactory(SiteUserFactory)
    category = factory.SubFactory(CategoryFactory)
    tiles = factory.RelatedFactoryList(
        TileFactory, factory_related_name="card", size=25
    )
