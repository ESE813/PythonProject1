import logging
from pathlib import Path
from typing import Union


log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "masks.log"

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Удаляем старые хендлеры, если уже есть
if logger.hasHandlers():
    logger.handlers.clear()

# Настройка file handler
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Маскирует номер карты."""
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.debug(f"Успешная маскировка карты: {masked_number}")
        return masked_number
    else:
        logger.error(f"Ошибка маскировки карты: входные данные — {card_number}")
        return "Неправильно введен номер карты!"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Маскирует номер счёта."""
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[-4:]
        logger.debug(f"Успешная маскировка счёта: {masked_account}")
        return masked_account
    else:
        logger.error(f"Ошибка маскировки счёта: входные данные — {account_number}")
        return "Неправильно введен номер счета!"
