from src.masks import get_mask_card_number, get_mask_account


if __name__ == "__main__":
    card_number = "0000000000000000"
    account_number = "0000000000000000000"
    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
