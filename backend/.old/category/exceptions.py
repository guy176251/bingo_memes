from .models import Category


def add_category_exceptions(api):
    @api.exception_handler(Category.DoesNotExist)
    def category_not_exist(request, exc):
        return api.create_response(request, {"detail": "Not a valid category id."}, status=422)
