from django.test import TestCase

from core.tasks import some_task
from core.models import Rates, Coin


class SomeTaskTestCase(TestCase):

    def setUp(self):
        self.task = some_task

    def test_get_task(self):
        self.task()
        rates = Rates.objects.all()

        self.assertEqual(len(rates), 3)

    def test_get_task_with_coin(self):
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

        self.task()
        rates = Rates.objects.all()
        self.assertEqual(len(rates), 3)

