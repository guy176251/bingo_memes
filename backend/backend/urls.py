"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from core.auth import JWTOrReadOnlyAuth
from user.api import add_user_exceptions, router as user_router
from category.api import add_category_exceptions, router as category_router
from card.api import add_card_exceptions, router as card_router

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

jwt_read_only = JWTOrReadOnlyAuth()

api.add_router("/user/", user_router, auth=jwt_read_only)
api.add_router("/category/", category_router, auth=jwt_read_only)
api.add_router("/card/", card_router, auth=jwt_read_only)

exception_handlers = [
    add_user_exceptions,
    add_card_exceptions,
    add_category_exceptions,
]

for add_handler in exception_handlers:
    add_handler(api)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
