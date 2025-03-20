from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card


if __name__ == "__main__":
    card_number = "0000000000000000"
    account_number = "0000000000000000000"
    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
    date = "2024-03-11T02:26:18.671407"
    print(get_date(date))
    print(mask_account_card('Maestro 1596837868705199'))
    print(mask_account_card('Счет 64686473678894779589'))
    print(mask_account_card('MasterCard 7158300734726758'))
    print(mask_account_card('Счет 35383033474447895560'))
    print(mask_account_card('Visa Classic 6831982476737658'))
    print(mask_account_card('Visa Platinum 8990922113665229'))
