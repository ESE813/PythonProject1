from src.data_reader import filter_transactions

def test_filter_transactions():
    """Тестирование фильтрации транзакций по строке поиска."""
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
        {"description": "Перевод на счет", "amount": 2000, "currency": "USD"},
    ]
    search_string = "Вклад"
    result = filter_transactions(transactions, search_string)
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"

def test_filter_transactions_no_match():
    """Тестирование фильтрации транзакций, когда нет совпадений."""
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
        {"description": "Перевод на счет", "amount": 2000, "currency": "USD"},
    ]
    search_string = "Несуществующая операция"
    result = filter_transactions(transactions, search_string)
    assert len(result) == 0
