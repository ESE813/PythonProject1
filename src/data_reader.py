import csv
import pandas as pd
from typing import List, Dict


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
