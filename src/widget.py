from calendar import month
from typing import Union


def mask_account_card(card_number: Union[str]) -> Union[str]:
    """Функция принимает тип и номер карты или счета и маскирует его"""

    if card_number.isdigit() and len(card_number) == 16:
        masked_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return masked_number
    else:
        return "Неправильно введен номер карты!"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера счета."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[-4:]
        return masked_account
    else:
        return "Неправильно введен номер счета!"


def get_date(date_str: str) -> str:
    """Функция обрабатывает дату в формате ДД-ММ-ГГ"""
    year_str = date_str[:4]
    month_str = date_str[5:7]
    day_str = date_str[8:10]
    return f"{day_str}.{month_str}.{year_str}"
