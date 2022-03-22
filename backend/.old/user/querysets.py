from django.db.models import Exists, OuterRef, QuerySet

from .models import Follow, Profile


def annotated_users(users: QuerySet, user: Profile):
    users = users.annotate(
        is_following=Exists(
            Follow.objects.filter(followed=OuterRef("pk"), follower=user, is_following=1)
        )
    )
    return users


def outgoing_users(auth, detail=False):
    users = Profile.objects.all()

    if detail:
        users = users.prefetch_related("followers", "following")

    if auth.is_authenticated:
        return annotated_users(users, auth.profile)
    else:
        return users
