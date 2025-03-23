def filter_by_state(bank_data, state="EXECUTED"):
    """Фильтрует словарь по значению ключа state"""
    return [item for item in bank_data if item.get("state") == state]
