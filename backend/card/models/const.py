from typing import Any, Protocol, TypeAlias


class ModelNames:
    CARD = "Card"
    HASHTAG = "Hashtag"
    HASHTAG_CARD = "HashtagToCard"
    HASHTAG_PROFILE = "HashtagSub"
    PROFILE = "user.Profile"
    VOTE = "Vote"


# class UserType(Protocol):
#     is_authenticated: bool
#     profile: Any


class HasAuthenticated(Protocol):
    is_authenticated: bool


class HasProfile(Protocol):
    is_authenticated: bool
    profile: Any


UserType: TypeAlias = HasAuthenticated | HasProfile
