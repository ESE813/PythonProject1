from datetime import datetime


def filter_by_state(bank_data, state="EXECUTED"):
    """Фильтрует словарь по значению ключа state"""
    return [item for item in bank_data if item.get("state") == state]


def sort_by_date(new_list_date):
    """Сортирует список словарей по дате в порядке убывания"""
    return sorted(new_list_date, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
