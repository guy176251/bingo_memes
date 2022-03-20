import pytest
from django.test import TestCase

from backend.settings import DEBUG
from user.factories import AuthUserFactory

from .factories import CardFactory
from .models import Card, Hashtag


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_get_card(api_client, count_queries):
    user = AuthUserFactory()
    card = CardFactory(author=user.profile)
    api_client.jwt_login(user)
    api_client.request_or_fail(200, "get", f"/api/card/{card.id}")


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_list_cards(api_client, count_queries):
    author = AuthUserFactory().profile
    token = "iuashjdiuhwieufhwiuhf"
    CardFactory(title=f"search this token: {token}", author=author)
    data = api_client.request_or_fail(200, "get", f"/api/card/?search={token}")
    assert type(data) == dict
    assert "items" in data
    assert len(data["items"]) == 1

    # search should return empty list
    data = api_client.request_or_fail(200, "get", f"/api/card/?search={token}a")
    assert "items" in data
    assert len(data["items"]) == 0


@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_create_card(api_client, count_queries):
    user = AuthUserFactory()
    api_client.jwt_login(user)

    payload = {
        "title": "Created card 1 #blessed",
    }
    payload.update({f"tile_{n}": f"Tile {n} contents" for n in range(1, 26)})
    api_client.request_or_fail(200, "post", "/api/card/", payload)


@pytest.mark.django_db
def test_update_card(api_client):
    user = AuthUserFactory()
    card = CardFactory(author=user.profile)
    api_client.jwt_login(user)
    payload = {"tile_1": "edited field VTQ6uXTSld"}
    api_client.request_or_fail(200, "put", f"/api/card/{card.id}", payload)
    data = api_client.request_or_fail(200, "get", f"/api/card/{card.id}")
    assert data["tile_1"] == payload["tile_1"]


class QueryCountTest(TestCase):
    def test_outgoing_cards(self):
        user = AuthUserFactory()
        CardFactory(
            title="#meme Outgoing Card",
            tile_1="search me",
            author=user.profile,
        )

        with self.assertNumQueries(1):
            print(
                Card.objects.outgoing(
                    user=user,
                    sort="new",
                    search="search me",
                )
            )

    def test_home(self):
        user = AuthUserFactory()
        CardFactory(title="#meme Home Card", author=user.profile)
        Hashtag.objects.subscribe(profile_id=user.profile.id, hashtag_id="meme")
        with self.assertNumQueries(1):
            print(Card.objects.home(user=user))


@pytest.mark.django_db
def test_hashtag_creation():
    user = AuthUserFactory()
    CardFactory(title="#poop Title 1", author=user.profile)
    CardFactory(title="#poop Title 2", author=user.profile)
    assert Hashtag.objects.count() == 1
    hashtag = Hashtag.objects.first()
    assert hashtag.name == "poop"


@pytest.mark.django_db
def test_card_sorting():
    """
    Test card sorting methods based on scoring.
    """

    if not DEBUG:
        return

    voter_1 = AuthUserFactory()
    voter_2 = AuthUserFactory()
    author = AuthUserFactory().profile

    # number corresponds to creation
    # lower = older
    card_1 = CardFactory(author=author)
    card_2 = CardFactory(author=author)
    card_3 = CardFactory(author=author)

    # increase card_1 score
    Card.objects.vote(
        card_id=card_1.id,
        profile_id=voter_1.profile.id,
        up=True,
    )
    Card.objects.vote(
        card_id=card_1.id,
        profile_id=voter_2.profile.id,
        up=True,
    )
    # increase card_2 score
    Card.objects.vote(
        card_id=card_2.id,
        profile_id=voter_1.profile.id,
        up=True,
    )

    # expected scores:
    #   card_1: 3
    #   card_2: 2
    #   card_3: 1

    assert Card.objects.get(pk=card_1.id).score == 3
    assert Card.objects.get(pk=card_2.id).score == 2
    assert Card.objects.get(pk=card_3.id).score == 1

    hot = list(Card.objects.outgoing(sort="hot"))
    hot_manual = sorted(hot, key=lambda c: c.hot, reverse=True)

    assert hot[0].id == hot_manual[0].id
    assert hot[1].id == hot_manual[1].id
    assert hot[2].id == hot_manual[2].id

    assert hot[0].id == card_1.id
    assert hot[1].id == card_2.id
    assert hot[2].id == card_3.id


@pytest.mark.django_db
@pytest.mark.parametrize("up", [True, False])
@pytest.mark.parametrize("double", [True, False])
def test_vote_card(up, double):
    voter = AuthUserFactory()
    author = AuthUserFactory().profile
    card = CardFactory(author=author)

    adjust = 1 if up else -1

    # first vote
    Card.objects.vote(
        card_id=card.id,
        profile_id=voter.profile.id,
        up=up,
    )
    card = Card.objects.outgoing(user=voter).get(pk=card.id)
    score = 1 + adjust
    assert card.score == score
    assert card.is_upvoted is up

    # second vote
    Card.objects.vote(
        card_id=card.id,
        profile_id=voter.profile.id,
        up=up if double else not up,
    )
    card = Card.objects.outgoing(user=voter).get(pk=card.id)
    score = 1 if double else 1 - adjust
    assert card.score == score
    assert card.is_upvoted is (None if double else not up)


@pytest.mark.django_db
def test_get_home():
    subscriber = AuthUserFactory()
    author = AuthUserFactory().profile
    card_1 = CardFactory(author=author, title="#one Card 1")
    card_2 = CardFactory(author=author, title="#two Card 2")
    card_3 = CardFactory(author=author, title="#three Card 3")
    card_4 = CardFactory(author=author, title="#four Card 4 Not Subscribed")
    Hashtag.objects.subscribe(profile_id=subscriber.profile.id, hashtag_id="one")
    Hashtag.objects.subscribe(profile_id=subscriber.profile.id, hashtag_id="two")
    Hashtag.objects.subscribe(profile_id=subscriber.profile.id, hashtag_id="three")
    cards = Card.objects.home(user=subscriber)
    assert cards.count() == 3
    assert cards.filter(id=card_1.id).exists()
    assert cards.filter(id=card_2.id).exists()
    assert cards.filter(id=card_3.id).exists()
    assert not cards.filter(id=card_4.id).exists()


@pytest.mark.django_db
def test_search():
    title = "Title oisjdjbvcjhbsdjchbxcv"
    tile = "Tile kjnxcvmndfkjvnxckvjn"
    author = AuthUserFactory().profile
    CardFactory(author=author, title=title)
    CardFactory(author=author, tile_3=tile)
    assert Card.objects.search(search=title.lower()).exists()
    assert Card.objects.search(search=tile.upper()).exists()


# @pytest.mark.django_db
# @pytest.mark.parametrize("up", [True, False])
# @pytest.mark.parametrize("double", [True, False])
# @pytest.mark.count_queries(autouse=False)
# def test_vote_card_api(api_client, up, double, count_queries):
#     user = ProfileFactory()
#     card = CardFactory()
#
#     # can't vote if not logged in
#     api_client.request_or_fail(
#         401,
#         "post",
#         "/api/card/vote",
#         {"card_id": card.id, "up": True and up},
#     )
#     api_client.jwt_login(user)
#
#     adj = 1 if up else -1
#
#     # first vote
#     api_client.request_or_fail(
#         200,
#         "post",
#         "/api/card/vote",
#         {"card_id": card.id, "up": up},
#     )
#
#     score = 1 + adj
#
#     data = api_client.request_or_fail(200, "get", f"/api/card/{card.id}")
#     assert data["score"] == score  # first card
#     assert data["is_upvoted"] is up
#
#     # second vote
#     api_client.request_or_fail(
#         200,
#         "post",
#         "/api/card/vote",
#         {"card_id": card.id, "up": up if double else not up},
#     )
#
#     score = 1 if double else 1 - adj
#
#     data = api_client.request_or_fail(200, "get", f"/api/card/{card.id}")
#     assert data["score"] == score  # second card
#     assert data["is_upvoted"] is (None if double else not up)
