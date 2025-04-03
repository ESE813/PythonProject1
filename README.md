# ПРОЭКТ


** IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
** Это виджет, который показывает несколько последних успешных банковских операций клиента.
** Проект, который на бэкенде будет готовить данные для отображения в новом виджете.


### Зависимости, необходимые для работы проэкта:

** poetry-core==1.9.1 
** python_version >= "3.12"
** requests==2.31.0



## ЗАДАНИЕ 1

1. Создание основные пакеты: src — для исходного кода, tests — для тестов.
2. Установите инструменты для проверки качества кода (Flake8, black, isort, mypy) в группу lint через Poetry.
3. Настройка файла .flake8 для конфигурации линтера Flake8.
4. Добавление конфигурации для black, isort и mypy в файл pyproject.toml.
5. В пакете src создайте модуль с названием masks, в котором реализовано две функции:
- Функцию маскировки номера банковской карты get_mask_card_number
- Функцию маскировки номера банковского счета get_mask_account


## ЗАДАНИЕ 2

1. Инициализирован новый локальный Git-репозиторий в папке проекта, с помощью команды git init.
2. Создан файл .gitignore в корне проекта и добавлены в него стандартные шаблоны для Python, чтобы исключить системные и временные файлы, такие как__pycache__, .idea и другие.
3. Создано минимум три коммита в процессе разработки кода, зафиксированы основные этапы создания проекта.
4. В пакете src создан новый модуль с именем widget. Этот модуль содержит функции для работы с новыми возможностями приложения.
5. В модуле widget создана функция mask_account_card, которая умеет обрабатывать информацию как о картах, так и о счетах.
6. Функция принимает один аргумент — строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером.
7. В том же модуле создана функция get_date, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"


## ЗАДАНИЕ 3

1. В директории \src проекта создан модуль processing, который будет содержать новые функции обработки данных.
2. В модуле processing реализована функция filter_by_state, которая принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'). 
3. Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
4. В том же модуле реализована функция sort_by_date, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date).

## ТЕСТИРОВАНИЕ

1. В папке **test** созданы три тест-кейса **(test_masks.py, test_widget.py, test_processing.py)** для тестирования модулей: **masks, widget, processing**.
2. В **test_masks.py** созданы функции для тестирования:
- **mask_account_card**:
            - Функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
            - Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
            - Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
- **get_data**:
            - Тестирование правильности преобразования даты.
            - Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
            - Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
3. В **test_widget.py**:
- **mask_account_card**:
            - Функция корректно распознает и применяет нужный тип маскировки в зависимости от типа
            входных данных (карта или счет).
            - Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
            - Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
- **get_data**:
            Тестирование правильности преобразования даты.
            Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
            Функция корректно обрабатывает входные строки, где отсутствует дата.
4. В **test_processing.py** созданы условия для тестирования: 
- **filter_by_state**:
            - Тестирование фильтрации списка словарей по заданному статусу state.
            - Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
            - Параметризация тестов для различных возможных значений статуса state.
- **sort_by_date**:
            - Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
            - Проверка корректности сортировки при одинаковых датах.
            - Тесты на работу функции с некорректными или нестандартными форматами дат.
5.  Созданы условия для проверки покрытия с помощью **Code coverage**. Отчет сгенерирован в папке **htmlcov** и храниться в файле с названием **index.html**.
## ГЕНЕРАТОРЫ 

1. Создание нового модуля в проекте под названием **generators**. Этот модуль будет содержать все новые функции,
    реализующие генераторы для обработки данных.
   - Создание функции **filter_by_currency**, которая принимает на вход список словарей, представляющих транзакции.
     Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
     (например, USD).

2. Создание генератора **transaction_descriptions**, который принимает список словарей с транзакциями и возвращает
     описание каждой операции по очереди.

3. Создание генератора **card_number_generator**, который выдает номера банковских карт в формате 
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999. Генератор принимает начальное и конечное значения для
    генерации диапазона номеров. 

4. Создан тест для нового функционала проекта, **test_generators**. Данный функционал размещен в папке **tests**.
    Тестируются весь модуль **generators**, в нем две функции **filter_by_currency**  **transaction_descriptions** 
    и генератор **card_number_generator**.

### Пример входных данных
\```
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
\```