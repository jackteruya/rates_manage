from django.test import TestCase, Client
from django.urls import reverse_lazy
from rest_framework.test import APIClient
from model_mommy import mommy

from core.api_view.views import RatesApiViews
from core.models import Coin


class RatesApiViewTestCase(TestCase):

    def setUp(self):
        self.data = mommy.make("Rates", _quantity=5)
        self.cliente = APIClient()

    def test_list_rates(self):
        request = self.cliente.get(reverse_lazy('rates'))
        self.assertEqual(request.status_code, 200)


class CreateInitialRatesApiViewTestCase(TestCase):

    def setUp(self):
        self.cliente = APIClient()

    def test_create_rates(self):
        request = self.cliente.get(reverse_lazy('rates-create', args=(1,)))
        self.assertEqual(request.status_code, 200)

    def test_create_rates_with_coin(self):
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

        request = self.cliente.get(reverse_lazy('rates-create', args=(1,)))
        self.assertEqual(request.status_code, 200)
