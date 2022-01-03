import factory
from factory.django import DjangoModelFactory

from . import models
from user.factories import SiteUserFactory


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: f"Test Category {n}")
    banner_url = (
        "https://previews.123rf.com/images/roxanabalint/roxanabalint1610/roxanabalint161000101/"
        "63650664-bingo-banner-or-label-for-business-promotion-on-white-background-vector-illustration.jpg"
    )
    icon_url = "https://cdn.iconscout.com/icon/premium/png-256-thumb/bingo-ball-3768448-3142190.png"
    description = factory.Sequence(
        lambda n: f"Description for Test Category {n}, which is an automatically generated bingo card category."
    )
    author = factory.SubFactory(SiteUserFactory)
