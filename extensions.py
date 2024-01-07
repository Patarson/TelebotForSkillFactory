import requests
import json
from config import keys,APIkey

class ConvertionException(Exception):
    pass


class СurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/{APIkey}/pair/{quote_ticker}/{base_ticker}/{amount}')
        total_base = round(float(json.loads(r.content)['conversion_result']), 2)

        return total_base