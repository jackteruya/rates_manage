from rest_framework.serializers import ModelSerializer

from core.models import Rates, Coin


# class CoinSerialisers(ModelSerializer):
#
#     class Meta:
#         model = Coin
#         fields = (
#             'sigla',
#         )
#

class RatesSerializers(ModelSerializer):

    class Meta:
        model = Rates
        fields = (
            'date_rate',
            'coin',
            'rate_base',
            'value'
        )
