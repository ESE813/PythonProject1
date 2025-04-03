import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture
def input_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(input_date):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(input_date, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(input_date, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "input_date",
    [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
)
def test_filter_by_state_no_state(input_date):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(Exception, match="Словарь с указанным статусом state отсутствует"):
        filter_by_state(
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )


def test_sort_by_date(input_date):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания"""
    assert sort_by_date(input_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "date_string",
    [
        "invalid date",
        "2024/01/01T12:00:00.000000",  # Неверный формат
        "2024-01-01 12:00:00",  # Неверный формат
        "2024-01-01T12:60:00.000000",  # Неверная минута
    ],
)
def test_sort_by_date_incorrect(input_date, date_string):
    """Тест на работу функции с некорректными или нестандартными форматами дат"""
    with pytest.raises(ValueError):
        sort_by_date(input_date + [{"date": date_string}])
