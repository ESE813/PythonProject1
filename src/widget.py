from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(num_for_mask: str) -> str:
    """Функция маскирует номер карты или счета"""
    num_for_mask_split = num_for_mask.split()
    if "Счет" in num_for_mask_split:
        return f"Cчет {get_mask_account(num_for_mask_split[1])}"
    else:
        card_num = []
        card_name = []
        for i in num_for_mask_split:
            if i.isdigit():
                card_num.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_num = " ".join(card_num)
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(str_card_num)}"


def get_date(date_str: str) -> str:
    """Функция обрабатывает дату в формате ДД-ММ-ГГ"""
    year_str = date_str[:4]
    month_str = date_str[5:7]
    day_str = date_str[8:10]
    return f"{day_str}.{month_str}.{year_str}"
