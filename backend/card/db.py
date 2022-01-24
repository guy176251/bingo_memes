from core.db import Abs, Log10, Sign, Sqrt
from django.db.models import (Case, Count, Exists, F, Func, OuterRef, Q, Sum,
                              When)

from .models import Vote


def hot_query():
    """Scoring equation that emulates reddit's "hot" scoring."""

    score_or_1 = Case(When(Q(score=0), then=1), default=F("score"))

    return (
        Sign(F("score")) * Log10(Abs(score_or_1))
        + (F("created_timestamp") - 1134028003) / 45000
    )


def best_query():
    """Scoring equation that emulates reddit's "best" scoring."""

    up = F("up")
    total = F("total")

    # z = 1.96
    z = 1.28  # 80% confidence
    p = up / total

    left = p + z * z / (2.0 * total)
    s = (p * (1.0 - p) + z * z / (4.0 * total)) / total
    right = z * Sqrt(s)
    under = 1.0 + z * z / total

    best = (left - right) / under

    return Case(When(score=0, then=0.0), default=best)


def upvote_query(user):
    """Adds an `upvoted` field to `Card` querysets."""

    def vote_exists(up: int):
        return Exists(Vote.objects.filter(card=OuterRef("pk"), user=user, up=up))

    return Case(
        When(vote_exists(0), then=None),
        When(vote_exists(1), then=True),
        When(vote_exists(-1), then=False),
        default=None,
    )
