from src.data_reader import count_transactions_by_category


def test_count_transactions_by_category():
    """Тестирование подсчета транзакций по категориям."""
    transactions = [
        {"description": "Перевод с карты на карту", "amount": 1000, "currency": "RUB"},
        {"description": "Открытие вклада", "amount": 5000, "currency": "RUB"},
        {"description": "Перевод на счет", "amount": 2000, "currency": "USD"},
    ]
    categories = ["перевод", "вклад"]
    result = count_transactions_by_category(transactions, categories)
    assert result["вклад"] == 1
    assert result["перевод"] == 2
