import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 594226727,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "112548.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }]


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert {i["id"] for i in usd_transactions} == {939719570, 142264268}

    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert {i["id"] for i in rub_transactions} == {594226727}

    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 3

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    assert descriptions == expected_descriptions

    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0


