import datetime

from celery import shared_task

from core.utils.api_vatcompy import ServiceUpdateCoin
from core.models import Coin
from core.serializers.serializers import RatesSerializers


@shared_task
def some_task():

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

    date = datetime.datetime.today()
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
