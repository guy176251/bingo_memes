import factory
from random import choice, sample, randint
from factory.django import DjangoModelFactory

from .models import Card  # , Tile
from user.factories import SiteUserFactory

HASHTAGS = [
    "viral",
    "popular",
    "music",
    "art",
    "meme",
]

tile_field = factory.Faker("sentence")


class CardFactory(DjangoModelFactory):
    class Meta:
        model = Card

    name = factory.Sequence(
        lambda n: f"Test Card {n} "
        + " ".join(f"#{name}" for name in sample(HASHTAGS, randint(2, 4)))
    )
    author = factory.SubFactory(SiteUserFactory)
    category = factory.SubFactory("category.factories.CategoryFactory")

    tile_1 = tile_field
    tile_2 = tile_field
    tile_3 = tile_field
    tile_4 = tile_field
    tile_5 = tile_field
    tile_6 = tile_field
    tile_7 = tile_field
    tile_8 = tile_field
    tile_9 = tile_field
    tile_10 = tile_field
    tile_11 = tile_field
    tile_12 = tile_field
    tile_13 = tile_field
    tile_14 = tile_field
    tile_15 = tile_field
    tile_16 = tile_field
    tile_17 = tile_field
    tile_18 = tile_field
    tile_19 = tile_field
    tile_20 = tile_field
    tile_21 = tile_field
    tile_22 = tile_field
    tile_23 = tile_field
    tile_24 = tile_field
    tile_25 = tile_field
