import factory
from django.contrib.auth.hashers import make_password
from factory.django import DjangoModelFactory

from .models import AuthUser


class AuthUserFactory(DjangoModelFactory):
    class Meta:
        model = AuthUser

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.LazyFunction(lambda: make_password("pass"))
