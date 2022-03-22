from random import choice, randint, sample

import factory
from factory.django import DjangoModelFactory

from card.factories import HASHTAGS, CardFactory
from user.factories import ProfileFactory

from . import models

CATEGORY_NAMES = [
    "POP_CULTURE",
    "POLITICS",
    "ART",
    "SPORTS",
    "NEWS",
]


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.LazyAttributeSequence(lambda category, n: f"{choice(CATEGORY_NAMES)}_{n}")
    banner_url = (
        "https://previews.123rf.com/images/roxanabalint/roxanabalint1610/roxanabalint161000101/"
        "63650664-bingo-banner-or-label-for-business-promotion-on-white-background-vector-illustration.jpg"
    )
    icon_url = "https://cdn.iconscout.com/icon/premium/png-256-thumb/bingo-ball-3768448-3142190.png"
    description = factory.LazyAttribute(
        lambda category: f'Description for Test Category "{category.name}", which is an automatically generated bingo card category.'
    )
    author = factory.SubFactory(ProfileFactory)


class CategoryFullFactory(CategoryFactory):
    class Meta:
        model = models.Category

    cards = factory.RelatedFactoryList(
        CardFactory,
        factory_related_name="category",
        size=10,
        title=factory.LazyAttributeSequence(
            lambda card, n: f"{card.category.name} CARD_{n} "
            + " ".join(f"#{name}" for name in sample(HASHTAGS, randint(2, 4)))
        ),
    )
