def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера карты."""
    card_number_str = str(card_number)

    if len(card_number_str) != 16 or not card_number_str.isdigit():
        raise ValueError("Неправильно введен номер карты!")

    masked_number = f"{card_number_str[:6]}******{card_number_str[-4:]}"
    return masked_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера счета."""
    account_number_str = str(account_number)

    if len(account_number_str) != 20 or not account_number_str.isdigit():
        raise ValueError("Неправильно введен номер счета!")

    masked_account = "**" + account_number_str[-4:]
    return masked_account

