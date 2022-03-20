from datetime import datetime

from django.conf import settings
from django.core.signing import BadSignature
from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import rotate_token
from django.views.decorators.csrf import ensure_csrf_cookie
from ninja import Router
from ninja.responses import JsonResponse
from ninja_jwt.schema import TokenObtainPairSerializer, TokenRefreshSerializer
from ninja_schema import Schema

SALT = "reallytastysaltedporkribs"
token_router = Router()


def js_timestamp(dt: datetime) -> float:
    return dt.timestamp() * 1000


def token_response(token):
    """Manually creates JsonResponse and adds refresh token cookie to response."""

    resp = JsonResponse({"access": token.access})
    now = datetime.now()
    access_expiration = now + settings.NINJA_JWT["ACCESS_TOKEN_LIFETIME"]
    refresh_expiration = now + settings.NINJA_JWT["REFRESH_TOKEN_LIFETIME"]
    cookie_params = dict(
        secure=True,
        samesite="Strict",
    )

    resp.set_signed_cookie(
        **cookie_params,
        key="refresh",
        value=token.refresh,
        salt=SALT,
        httponly=True,
        expires=refresh_expiration,
    )
    resp.set_cookie(
        **cookie_params,
        key="logged_in",
        value=js_timestamp(refresh_expiration),
        expires=refresh_expiration,
    )
    resp.set_cookie(
        **cookie_params,
        key="access",
        value=js_timestamp(access_expiration),
        expires=access_expiration,
    )
    return resp


class AccessTokenOutput(Schema):
    access: str


@token_router.post(
    "pair",
    response=AccessTokenOutput,
    url_name="token_obtain_pair",
    operation_id="token_obtain_pair",
)
@ensure_csrf_cookie
def obtain_token(request, user_token: TokenObtainPairSerializer):
    token = user_token.output_schema()
    rotate_token(request)
    return token_response(token)


@token_router.post(
    "refresh",
    response=AccessTokenOutput,
    url_name="token_refresh",
    operation_id="token_refresh",
)
@ensure_csrf_cookie
def refresh_token(request: HttpRequest):
    bad_resp = JsonResponse({"detail": "Not authorized"}, status=401)

    try:
        refresh = request.get_signed_cookie("refresh", salt=SALT)
    except (BadSignature, KeyError):
        return bad_resp

    if not refresh:
        return bad_resp

    token = TokenRefreshSerializer(refresh=refresh)
    rotate_token(request)
    return token_response(token)


@token_router.get("check_in", operation_id="get_csrf_token")
@ensure_csrf_cookie
def give_csrf_token(request):
    return HttpResponse()


@token_router.post("unpair", operation_id="token_unpair")
def unpair_token(request):
    resp = HttpResponse()
    resp.delete_cookie("refresh")
    resp.delete_cookie("logged_in")
    resp.delete_cookie("access")
    return resp
