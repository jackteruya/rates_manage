from datetime import date, datetime

from django.test import TestCase, Client
from django.urls import reverse_lazy
from model_mommy import mommy

from core.serializers.serializers import RatesSerializers


class RatesSerializerTestCase(TestCase):

    def setUp(self):
        # self.rates = mommy.make('Rates', _quantity=5)
        self.coin = mommy.make('Coin')

    def test_rate_data_valid(self):

        rate_serializer = RatesSerializers(data={"date_rate": date.today(),
                                                 "coin": self.coin.id,
                                                 "rate_base": "USD",
                                                 "value": 5.555555})
        self.assertTrue(rate_serializer.is_valid())

    def test_data_date_rate_not_valid(self):
        rate_serializer = RatesSerializers(data={"date_rate": datetime.today(),
                                                 "coin": self.coin.id,
                                                 "rate_base": "USD",
                                                 "value": 5.555555})
        self.assertFalse(rate_serializer.is_valid())

    def test_data_coin_not_valid(self):
        rate_serializer = RatesSerializers(data={"date_rate": date.today(),
                                                 "coin": "self.coin.id",
                                                 "rate_base": "USD",
                                                 "value": 5.555555})
        self.assertFalse(rate_serializer.is_valid())

    def test_data_base_not_valid(self):
        rate_serializer = RatesSerializers(data={"date_rate": date.today(),
                                                 "coin": self.coin.id,
                                                 "rate_base": 1,
                                                 "value": 5.555555})
        self.assertFalse(rate_serializer.is_valid())

    def test_data_value_not_valid(self):
        rate_serializer = RatesSerializers(data={"date_rate": date.today(),
                                                 "coin": self.coin.id,
                                                 "rate_base": 1,
                                                 "value": 5.55555555555})
        self.assertFalse(rate_serializer.is_valid())
