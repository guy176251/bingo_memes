import logging
from typing import Any, Optional, Tuple
from abc import ABC, abstractmethod

from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.http import HttpRequest

from ninja.compatibility import get_headers
from ninja.security.http import HttpAuthBase
from ninja_jwt.authentication import JWTBaseAuthentication
from ninja_jwt.exceptions import InvalidToken


logger = logging.getLogger("django")


class HttpBearerOrReadOnly(HttpAuthBase, ABC):
    """
    Copies ninja's `HttpBearer` but safe methods are allowed without a token.
    """

    openapi_scheme: str = "bearer"
    header: str = "Authorization"
    safe_methods: list[str] = ["GET", "HEAD", "OPTIONS"]

    def __call__(self, request: HttpRequest) -> Optional[Any]:
        headers = get_headers(request)
        auth_value = headers.get(self.header)
        if not auth_value:
            if request.method in self.safe_methods:
                return AnonymousUser()
            else:
                return None

        parts = auth_value.split(" ")

        if parts[0].lower() != self.openapi_scheme:
            if settings.DEBUG:
                logger.error(f"Unexpected auth - '{auth_value}'")
            return None
        token = " ".join(parts[1:])
        return self.authenticate(request, token)

    @abstractmethod
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        pass  # pragma: no cover


class JWTOrReadOnlyAuth(JWTBaseAuthentication, HttpBearerOrReadOnly):
    """
    Same as `JWTAuth` but allows safe methods without a token.
    TODO: change how it handles token expiration.
    """

    def authenticate(self, request: HttpRequest, token: str) -> Any:
        return self.jwt_authenticate(request, token)
