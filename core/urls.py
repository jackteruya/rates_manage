from django.contrib import admin
from django.urls import path, include
from core.views import GraphicView
from core.api_view.views import RatesApiViews, CreateIntialRatesApiViews

urlpatterns = [
    path('', GraphicView.as_view(), name='graphic'),
    path('api/', include([
        path('rates/', RatesApiViews.as_view(), name='rates'),
        path('rates/create/<int:days>', CreateIntialRatesApiViews.as_view(), name='rates-create'),
    ]))
]
