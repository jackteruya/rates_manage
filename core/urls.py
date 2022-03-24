from django.contrib import admin
from django.urls import path, include
from core.views import GraphicView, IndexView
from core.api_view.rates import (
    RatesListApiViews,
    CreateIntialRatesApiViews,
    RateApiViews
)
from core.api_view.coins import (
    CoinApiViews,
    CoinsListApiViews
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('graphic/', GraphicView.as_view(), name='graphic'),
    path('api/', include([
        path('rates/', RatesListApiViews.as_view(), name='rates-list'),
        path('rates/<int:pk>/', RateApiViews.as_view(), name='rate-view'),
        path('rates/<int:days>/create/', CreateIntialRatesApiViews.as_view(), name='rates-create'),

        path('coins/', CoinsListApiViews.as_view(), name='coins-list'),
        path('coins/<int:pk>/', CoinApiViews.as_view(), name='coin-view')
    ]))
]
