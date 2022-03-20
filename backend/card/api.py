import logging

from ninja import Router, NinjaAPI
from ninja.pagination import PageNumberPagination, paginate

from .models import Card
from .schema import (
    CardCreateSchema,
    CardDetailSchema,
    CardListSchema,
    CardUpdateSchema,
    VoteSchema,
)

card_router = Router()
logger = logging.getLogger("debug")


def add_card_exceptions(api: NinjaAPI):
    @api.exception_handler(Card.DoesNotExist)
    def card_not_exist(request, exc):
        return api.create_response(
            request,
            {"detail": "Not a valid card id."},
            status=422,
        )


@card_router.get("{int:card_id}", response=CardDetailSchema, operation_id="card_get")
def get_card(request, card_id: int):
    return Card.objects.outgoing(user=request.user).get(pk=card_id)


@card_router.get("", response=list[CardListSchema], operation_id="card_list")
@paginate(PageNumberPagination)
def list_cards(
    request,
    sort: str = "hot",
    search: str = None,
):
    return Card.objects.outgoing(
        user=request.user,
        sort=sort,
        search=search,
    )


@card_router.get("home", response=list[CardListSchema], operation_id="card_home")
@paginate(PageNumberPagination)
def card_home(request, sort: str = "hot"):
    return Card.objects.home(user=request.user, sort=sort)


@card_router.post("", response=CardCreateSchema, operation_id="card_create")
def create_card(request, payload: CardCreateSchema):
    data = payload.dict()
    data["author"] = request.user.profile
    return Card.objects.create(**data)


@card_router.put("{int:card_id}", operation_id="card_update")
def update_card(request, card_id: int, payload: CardUpdateSchema):
    data = {key: value for key, value in payload.dict().items() if value}
    Card.objects.filter(pk=card_id).update(**data)


@card_router.post("vote", operation_id="vote_card")
def vote_card(request, payload: VoteSchema):
    Card.objects.vote(
        profile_id=request.user.profile.id,
        card_id=payload.card_id,
        up=payload.up,
    )
