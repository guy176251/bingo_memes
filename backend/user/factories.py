from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.models import User
from factory.django import DjangoModelFactory, mute_signals
import factory

from .models import SiteUser, AuthUser


@mute_signals(post_save)
class AuthUserFactory(DjangoModelFactory):
    class Meta:
        model = AuthUser

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.LazyFunction(lambda: make_password("pass"))
    site_user = factory.SubFactory(
        "user.factories.SiteUserFactory",
        auth=None,
    )


@mute_signals(post_save)
class SiteUserFactory(DjangoModelFactory):
    class Meta:
        model = SiteUser

    score = 0
    username = factory.Faker("user_name")
    auth = factory.RelatedFactory(
        AuthUserFactory,
        factory_related_name="site_user",
        username=factory.LazyAttribute(lambda auth: auth.site_user.username),
    )


# @mute_signals(post_save)
# class SiteUserFactory(DjangoModelFactory):
#     class Meta:
#         model = SiteUser
#
#     score = 0
#     username = factory.Faker("user_name")
#     auth = factory.SubFactory(
#         "user.factories.AuthUserFactory",
#         # site_user=None,
#     )
#
#
# @mute_signals(post_save)
# class AuthUserFactory(DjangoModelFactory):
#     class Meta:
#         model = AuthUser
#
#     email = factory.Faker("email")
#     username = factory.Faker("user_name")
#     password = factory.LazyFunction(lambda: make_password("pass"))
#     site_user = factory.RelatedFactory(
#         SiteUserFactory, factory_related_name="auth",
#         username=factory.LazyAttribute(lambda site_user: site_user.auth.username)
#     )
