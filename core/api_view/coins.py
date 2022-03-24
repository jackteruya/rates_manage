import datetime

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.models import Rates, Coin
from core.serializers.serializers import CoinsSerializers


class CoinsListApiViews(ListAPIView):

    # ´v1/ap1/rates/´  -- List rates

    queryset = Coin.objects.all()
    serializer_class = CoinsSerializers


class CoinApiViews(RetrieveAPIView):

    # ´v1/ap1/rates/´  -- List rates

    queryset = Coin.objects.all()
    serializer_class = CoinsSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
