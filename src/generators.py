def filter_by_currency(transactions, currency):
    """Генератор, который фильтрует транзакции по заданной валюте"""
    for i in transactions:
        if i['operationAmount']['currency']['name'] == currency:
            yield i


def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции по очереди"""
    for i in transactions:
        yield i['description']



def card_number_generator(start, end):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    start = int(start)
    end = int(end)
    # Генерируем номера карт в диапазоне от start до end
    for num in range(start, end + 1):
        # Форматируем номер с ведущими нулями, если это необходимо
        card_number = f"{num:016d}"
        # Форматируем номер с пробелами
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

