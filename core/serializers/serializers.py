from rest_framework.serializers import ModelSerializer

from core.models import Rates, Coin


class CoinsSerializers(ModelSerializer):

    class Meta:
        model = Coin
        fields = (
            'sigla',
            'name'
        )


class RatesSerializers(ModelSerializer):

    class Meta:
        model = Rates
        fields = (
            'date_rate',
            'coin',
            'rate_base',
            'value'
        )
