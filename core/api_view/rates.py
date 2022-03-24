import datetime

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.models import Rates, Coin
from core.serializers.serializers import RatesSerializers
from core.utils.api_vatcompy import ServiceUpdateCoin


class RatesListApiViews(ListAPIView):

    # ´v1/ap1/rates/´  -- List rates

    queryset = Rates.objects.order_by("-date_rate").all()
    serializer_class = RatesSerializers


class RateApiViews(RetrieveAPIView):

    # ´v1/ap1/rates/´  -- List rates

    queryset = Rates.objects.all()
    serializer_class = RatesSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CreateIntialRatesApiViews(APIView):

    # ´v1/ap1/rates/create/{{days}}´  -- Initial creation of rates
    # days: number of days called in rate creation

    parser_classes = [JSONParser]
    queryset = Rates.objects.all()
    serializer_class = RatesSerializers

    def get(self, request, format=None, *args, **kwargs):

        coins = self._get_coin()

        for count in range(kwargs['days']):
            date = (datetime.datetime.today() - datetime.timedelta(days=count))
            year = date.year
            month = date.month
            day = date.day
            for coin in coins:
                get_coin = Coin.objects.get(sigla=coin)
                service = ServiceUpdateCoin(coin=coin, date=f'{year}-{month}-{day}')
                response = service.get_response()
                data = {
                    'date_rate': response['date'],
                    'rate_base': 'USD',
                    'coin': get_coin.id,
                    'value': round(response['rate'], 7)
                }

                serializer = RatesSerializers(data=data)
                serializer.is_valid()
                serializer.save()

        return Response({"status code": 200, "message": "rates created successfully"})

    def _get_coin(self):

        coins = Coin.objects.all()

        if coins:
            coins = [coin.sigla for coin in Coin.objects.all()]
        else:
            real = Coin()
            real.name = "Real"
            real.sigla = "BRL"
            real.save()

            iene = Coin()
            iene.name = "Iene"
            iene.sigla = "JPY"
            iene.save()

            euro = Coin()
            euro.name = "Euro"
            euro.sigla = "EUR"
            euro.save()

            coins = [coin.sigla for coin in Coin.objects.all()]

        return coins
