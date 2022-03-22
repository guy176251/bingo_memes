from .db import best_score, hot_score, is_upvoted
from .models import Card


def outgoing_cards(user, **list_kwargs):
    """
    Annotates `upvoted` to all cards in queryset, and prefetchs things
    that are in the `CardOutSchema`. Meant for outgoing cards.
    """

    queries = {}
    sort_types = {
        "hot": "-hot",
        "best": "-best",
        "new": "-created_at",
    }

    if user.is_authenticated:
        queries["is_upvoted"] = is_upvoted(user.profile)

    sort_raw = list_kwargs.pop("sort", "hot")
    sort_by = sort_types.get(sort_raw, sort_types["hot"])

    return (
        Card.objects.filter(**list_kwargs)
        .select_related(
            "author",
            # "category"
        )
        # .prefetch_related("hashtags")
        .annotate(
            **queries,
            hot=hot_score(),
            best=best_score(),
        )
        .order_by(sort_by)
        .distinct()
    )
