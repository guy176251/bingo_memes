from django.core.management.base import BaseCommand
from django.db.transaction import atomic

from category.factories import CategoryFullFactory
from user.factories import ProfileFactory


class Command(BaseCommand):
    @atomic
    def handle(self, *args, **options):
        for _ in range(10):
            CategoryFullFactory()
