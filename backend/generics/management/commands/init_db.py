from django.core.management.base import BaseCommand
from django.db.transaction import atomic

from user.factories import SiteUserFactory
from category.factories import CategoryFullFactory


class Command(BaseCommand):
    @atomic
    def handle(self, *args, **options):
        for _ in range(10):
            CategoryFullFactory()
