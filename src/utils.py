import json
import os

from src.external_api import convert_to_rub
from pathlib import Path

def read_json_file(file_path):
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.
    Возвращает пустой список, если файл пустой, не содержит список или не найден.
    """
    file_path_to_json = (Path(__file__).resolve().parent / '..' / 'data' / 'operations.json').resolve()

    if not os.path.exists(file_path_to_json):
        return []

    try:
        with open(file_path_to_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []



def get_transaction_amount(transaction):
    """
    Возвращает сумму транзакции в рублях (float).
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if amount is None or currency is None:
        raise ValueError("Неверная транзакция: отсутствует сумма или валюта")

    return convert_to_rub(float(amount), currency)