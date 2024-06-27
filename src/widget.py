from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(
        card_account_type_and_card_number: str) -> str:  # card_account_type_and_card_number - тип карты/счета и номер карты/
    """Функция общей маскировки карты и счета"""
    # card_account_type_and_card_number.split()
    card_data = card_account_type_and_card_number.split()
    if card_data[0].lower() == "счет":
        return "Счет " + get_mask_account(card_data[1])
    else:
        card_number = "".join(card_data[-4:])
        card_type = " ".join(card_data[:-4])
        # return card_type + " " + get_mask_card_number(card_number)
        return f"{card_type} {get_mask_card_number(card_number)}"

    # Visa Platinum 7000 7922 8960 6361

    # Maestro 7000 7922 8960 6361

    # Счет 73654108430135874305


def get_data(input_info: str) -> str:
    """Возвращает преобразованное значение даты"""

    cut_date = input_info[:10].split("-")
    return ".".join(cut_date[::-1])

# Напишите функцию, которая принимает на вход строку вида
# 2018-07-11T02:26:18.671407
#  и возвращает строку с датой в виде
# 11.07.2018.
