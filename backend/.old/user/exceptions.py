from .models import Profile


def add_user_exceptions(api):
    @api.exception_handler(Profile.DoesNotExist)
    def user_not_exist(request, exc):
        return api.create_response(request, {"detail": "Not a valid user id."}, status=422)
