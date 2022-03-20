from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    fields = ["title", *Card.TILE_FIELDS]


admin.site.register(Card, CardAdmin)
