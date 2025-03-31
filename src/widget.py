from datetime import datetime

from src import masks


def mask_account_card(num_for_mask: str) -> str:
    """Функция маскирует номер карты или счета в зависимости от типа"""
    num_parts = num_for_mask.split()
    card_type = " ".join(num_parts[:-1])
    card_number_str = num_parts[-1]

    try:
        card_number_int = int(card_number_str)
        if "Счет" in card_type:
            masked_number = masks.get_mask_account(card_number_int)
        elif len(card_number_str) == 16:
            masked_number = masks.get_mask_card_number(card_number_int)
        else:
            raise ValueError("Неверный формат номера счета или карты")
        return f"{card_type} {masked_number}"
    except ValueError:
        return f"Ошибка: Неверный формат номера счета или карты"


def get_date(date_str: str) -> str:
    """Функция обрабатывает дату в формате ДД-ММ-ГГ"""
    date_str = date_str.strip()

    if not date_str:
        return ""

    try:
        date_object = datetime.fromisoformat(date_str[:-7])  # Убираем последние 7 символов
        return date_object.strftime("%d.%m.%Y")
    except ValueError:
        return ""
