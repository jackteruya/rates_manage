from django.contrib import admin

from core.models import Coin, Rates


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ("name", "sigla", )


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    list_display = ("rate_base", "coin", "date_rate", "value",)
    list_filter = ("coin",)
