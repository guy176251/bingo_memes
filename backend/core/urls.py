from django.http import HttpResponse
from django.urls import include, path
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from ninja import NinjaAPI

test_api = NinjaAPI(csrf=True, urls_namespace="csrf")


@test_api.get("")
@csrf_protect
def test_csrf(request):
    return {"detail": "csrf works?"}


@csrf_protect
def csrf_thing(request):
    print("regular view")
    return HttpResponse()


@ensure_csrf_cookie
def give_csrf_token(request):
    return HttpResponse()


urlpatterns = [path("", give_csrf_token)]
