from django.test import TestCase, Client
from django.urls import reverse_lazy
from model_mommy import mommy

from core.views import GraphicView


class GraphicViewTestCase(TestCase):

    def setUp(self):
        self.data = mommy.make("Rates", _quantity=10)
        self.cliente = Client()

    def test_get_graphic(self):
        request = self.cliente.get(reverse_lazy('graphic'))
        self.assertEqual(request.status_code, 200)
