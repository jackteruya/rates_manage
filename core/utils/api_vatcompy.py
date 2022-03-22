import requests

from quote_management.settings import API_VATCOMPLY


class ServiceUpdateCoin:

    def __init__(self, coin, date=None):
        self._api = "https://api.vatcomply.com/rates" #API_VATCOMPLY
        self.response = None
        self.date = date
        self.url = None
        self.coin = coin

    def get_url(self):
        url = f'{self._api}?'
        if self.coin:
            url += f'base={self.coin}'
        if self.date:
            url += f'&date={self.date}'

        self.url = url

    def get_api(self):
        data = requests.get(self.url)
        data = data.json()
        response = {
            'date': data['date'],
            'base': 'USD',
            'coin': data['base'],
            'rate': data['rates']['USD']
        }

        self.response = response

    def get_response(self):
        self.get_url()
        self.get_api()
        return self.response




