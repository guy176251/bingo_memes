from .models import Card


def add_card_exceptions(api):
    @api.exception_handler(Card.DoesNotExist)
    def card_not_exist(request, exc):
        return api.create_response(request, {"detail": "Not a valid card id."}, status=422)
