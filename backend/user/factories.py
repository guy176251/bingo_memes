from django.db.models.signals import post_save
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.models import User
from factory.django import DjangoModelFactory, mute_signals
import factory

from .models import SiteUser, AuthUser


# email, username, password
@mute_signals(post_save)
class SiteUserFactory(DjangoModelFactory):
    class Meta:
        model = SiteUser

    score = 0
    username = factory.Faker("first_name")
    auth_user = factory.SubFactory("user.factories.AuthUserFactory", site_user=None)


@mute_signals(post_save)
class AuthUserFactory(DjangoModelFactory):
    class Meta:
        model = AuthUser

    email = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password("pass"))
    site_user = factory.RelatedFactory(
        SiteUserFactory, factory_related_name="auth_user"
    )
