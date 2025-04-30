import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("CURRENCY_API_TOKEN")


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму из валюты (USD/EUR) в RUB по текущему курсу.
    """
    if currency == "RUB":
        return float(amount)

    url = f"https://apilayer.com/exchangerates_data-api"
    headers = {"apikey": API_TOKEN}
    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Currency conversion failed: {response.status_code}")

    data = response.json()
    return float(data.get("result"))
