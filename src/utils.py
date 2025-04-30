import json
import os
import logging
from pathlib import Path
from src.external_api import convert_to_rub


log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Путь к лог-файлу
log_file = log_dir / "utils.log"

logger = logging.getLogger("utils_logger")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def read_json_file(file_path):
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.
    Возвращает пустой список, если файл пустой, не содержит список или не найден.
    """
    file_path_to_json = (Path(__file__).resolve().parent / ".." / "data" / "operations.json").resolve()

    if not os.path.exists(file_path_to_json):
        logger.warning(f"Файл не найден: {file_path_to_json}")
        return []

    try:
        with open(file_path_to_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл успешно прочитан и содержит список транзакций")
                return data
            else:
                logger.error("Файл не содержит список.")
                return []
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка чтения файла: {e}")
        return []


def get_transaction_amount(transaction):
    """
    Возвращает сумму транзакции в рублях (float).
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    result = convert_to_rub(transaction)
    logger.info(f"Успешно получена сумма транзакции: {result} руб.")

    if amount is None or currency is None:
        raise ValueError("Неверная транзакция: отсутствует сумма или валюта")
    logger.error(f"Ошибка при получении суммы транзакции")
    return convert_to_rub(transaction)
