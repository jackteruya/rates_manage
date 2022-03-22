import datetime

from django.views.generic import ListView
from core.models import Rates, Coin


class GraphicView(ListView):
    template_name = 'graphic.html'

    def get_context_data(self, **kwargs):
        context = {}
        coin = self.queryset[0].coin
        context['coin_select'] = coin

        date = datetime.date.today()
        if date.month < 10:
            month = f'0{date.month}'
        else:
            month = date.month
        if date.day < 10:
            day = f'0{date.day}'
        else:
            day = date.day
        context['date_select'] = f'{date.year}-{month}-{day}'

        if self.request.GET:
            if not self.request.GET['date']:
                pass
            else:
                context['date_select'] = self.request.GET['date']
            if not self.request.GET['coin']:
                pass
            else:
                context['coin_select'] = Coin.objects.get(id=int(self.request.GET['coin']))

        data_quote = [float(rate.value) for rate in self.queryset]
        data_quote.reverse()
        data_days = [float(rate.date_rate.day) for rate in self.queryset]
        data_days.reverse()
        context['data_quote'] = data_quote
        context['data_days'] = data_days
        context['coins'] = Coin.objects.all()
        context['days_view'] = len(data_quote)
        return context

    def get_queryset(self):
        coin = Coin.objects.order_by('?').all()[:1]
        coin = coin[0].id
        date = datetime.date.today()
        days_view = 5
        if self.request.GET:
            if not self.request.GET['date']:
                pass
            else:
                date = datetime.date.fromisoformat(self.request.GET['date'])
            if not self.request.GET['coin']:
                pass
            else:
                coin = self.request.GET['coin']
            if not self.request.GET['days_view']:
                pass
            else:
                days_view = int(self.request.GET['days_view'])
        print(date)
        queryset = Rates.objects.order_by("-date_rate").filter(coin=int(coin), date_rate__lte=date).all()[:days_view]

        print(queryset)
        self.queryset = queryset
