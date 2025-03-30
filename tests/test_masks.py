import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected",
                         [(1234123412341234, "123412******1234"),
                          (1234567812345678, "123456******5678")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number",
                         [12345678, "abcdabcdabcdabcd"])
def test_get_mask_card_number_error(card_number):
    with pytest.raises(ValueError, match="Неправильно введен номер карты!"):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("account_number, expected",
                         [(12345648123456781234, "**1234"),
                          (12341234567812345678, "**5678")])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("account_number",
                         [12345678, "abcdabcdabcdabcd", 1234567812345781234])
def test_get_mask_account_error(account_number):
    with pytest.raises(ValueError, match="Неправильно введен номер счета"):
        get_mask_account(account_number)
