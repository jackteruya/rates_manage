import datetime

from django.test import TestCase, Client
from django.http.request import HttpRequest

from core.utils.api_vatcompy import ServiceUpdateCoin


class ServiceUpdateCoinTestCase(TestCase):
    def setUp(self):
        self.coin = "BRL"
        self.date = datetime.date.today()

        self.service = ServiceUpdateCoin(coin=self.coin, date=self.date)

    def test_get_url(self):
        self.service.get_url()
        url = f"{self.service._api}?base={self.coin}&date={self.date}"
        self.assertEqual(self.service.url, url)

    def test_get_api(self):
        self.service.get_url()
        self.service.get_api()
        response = self.service.response

        self.assertEqual(response['base'], 'USD')
        self.assertEqual(response['coin'], self.coin)

    def test_get_response(self):
        self.service.get_response()

        self.assertEqual(self.service.response['base'], 'USD')
        self.assertEqual(self.service.response['coin'], self.coin)

