from django.db.models import Exists, OuterRef, QuerySet

from .models import Category, Subscription


def annotated_categories(categories: QuerySet, user):
    categories = categories.annotate(
        is_subscribed=Exists(
            Subscription.objects.filter(category=OuterRef("pk"), user=user, is_subscribed=1)
        ),
    )
    return categories


def outgoing_categories(user, detail=False):
    categories = Category.objects.all()

    if detail:
        categories = categories.select_related("author").prefetch_related("hashtags")

    if user.is_authenticated:
        return annotated_categories(categories, user.profile)
    else:
        return categories
