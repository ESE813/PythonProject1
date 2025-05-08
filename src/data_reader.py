import csv
import pandas as pd
from typing import List, Dict
import re
from collections import Counter


def read_transactions_from_csv(csv_path: str) -> List[Dict]:
    """
    Читает финансовые транзакции из CSV-файла и возвращает список словарей.
    """
    transactions = []
    csv_file = "data/transactions.csv"

    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(dict(row))
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []

    return transactions


def read_transactions_from_excel(excel_path: str) -> List[Dict]:
    """
    Читает финансовые транзакции из Excel-файла и возвращает список словарей.
    """
    excel_file = "data/transactions_excel.xlsx"

    try:
        df = pd.read_excel(excel_file)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка чтения Excel: {e}")
        return []


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует транзакции по строке поиска в описании.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка поиска.
    :return: Список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Компилируем шаблон
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    category_count = Counter()
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1
    return dict(category_count)
