from django.db.models import Case, Count, Exists, F, OuterRef, Q, Subquery, When

from core.db import Abs, Log10, Sign, Sqrt

from .models import Card, Vote


def hot_score():
    """Scoring equation that emulates reddit's "hot" scoring."""

    score_or_1 = Case(When(Q(score=0), then=1), default=F("score"))

    return Sign(F("score")) * Log10(Abs(score_or_1)) + (F("created_timestamp") - 1134028003) / 45000


def best_score():
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


def is_upvoted(user):
    """Evaluates whether a user has voted on a card."""

    def vote_exists(up: int):
        return Exists(Vote.objects.filter(card=OuterRef("pk"), user=user, up=up))

    return Case(
        When(vote_exists(0), then=None),
        When(vote_exists(1), then=True),
        When(vote_exists(-1), then=False),
        default=None,
    )


def vote_on_card(up, card_id, user_id):
    """Updates the state of a card vote. Creates new vote if it doesn't exist."""

    up_state = F("up_state")
    down_state = F("down_state")

    if up:
        up_query = Case(When(Q(up_state=0), then=1), default=0)
        up_state = (up_state + 1) % 2
    else:
        up_query = Case(When(Q(down_state=0), then=-1), default=0)
        down_state = (down_state + 1) % 2

    votes_updated = Vote.objects.filter(user_id=user_id, card_id=card_id).update(
        up_state=up_state,
        down_state=down_state,
        up=up_query,
    )

    if not votes_updated:
        field = "up_state" if up else "down_state"
        data = {field: 1, "up": 1 if up else -1}
        Vote.objects.create(**data, user_id=user_id, card_id=card_id)


def adjust_card_score(card_id: int):
    """Calculates the score of a card and updates the author's score."""

    # https://stackoverflow.com/a/65613047
    def vote(query):
        return Subquery(
            Vote.objects.filter(card_id=OuterRef("pk"))
            .values("card")
            .annotate(count=query)
            .values("count")
        )

    def count(query):
        return Count("card_id", filter=query)

    up = count(Q(up=1))
    down = count(Q(up=-1))
    total = count(~Q(up=0))

    cards_updated = Card.objects.filter(id=card_id).update(
        up=vote(up),
        total=vote(total),
        score=vote(up - down),
    )

    # author_score = Subquery(
    #     Card.objects.filter(author_id=OuterRef("pk"))
    #     .values("author")
    #     .annotate(author_score=Sum("score"))
    #     .values("author_score")
    # )

    # new_score = Subquery(
    #     Profile.objects.filter(id=OuterRef("id"))
    #     .annotate(score_sum=Sum("cards_created__score"))
    #     .values_list("score_sum", flat=True)
    # )

    # users_updated = Profile.objects.filter(cards_created__id=card_id).update(score=new_score)
    print(f"{cards_updated = }")
