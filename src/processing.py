from datetime import datetime
from typing import Any
from typing import Dict
from typing import List


def filter_by_state(bank_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует словарь по значению ключа state"""
    new_list = []
    for item in bank_data:
        if item.get("state") == state:
            new_list.append(item)
        else:
            raise Exception("Словарь с указанным статусом state отсутствует")
    return new_list


def sort_by_date(new_list_date: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Сортирует список словарей по дате в порядке убывания"""
    return sorted(new_list_date, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
