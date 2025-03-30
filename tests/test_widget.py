import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("num_for_mask, expected", [("Visa Platinum 1234123412341234", "Visa Platinum 123412******1234"),
                                                    ("MasterCard 5185373029202738", "MasterCard 518537******2738"),
                                                    ("Счет 12345678901234567890", "Счет **7890"),
                                                    ("Invalid Card 1234",
                                                     "Ошибка: Неверный формат номера счета или карты")
                                                    ])
def test_mask_account_card(num_for_mask, expected):
    assert mask_account_card(num_for_mask) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == ""
    assert get_date("2024-02-30T12:00:00.000000") == ""


