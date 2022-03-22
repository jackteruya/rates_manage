from django.test import TestCase
from model_mommy import mommy

from core.models import Coin, Rates


class CoinTestCase(TestCase):

    def setUp(self):
        self.coin = mommy.make('Coin')

    def test_str(self):
        self.assertEqual(str(self.coin), self.coin.sigla)


class RatesTestCase(TestCase):

    def setUp(self):
        self.rates = mommy.make('Rates')

    def test_str(self):
        self.assertEqual(str(self.rates), f"Quotação {self.rates.coin}")
