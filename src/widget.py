def mask_account_card(card_account_type_and_card_number: str) -> str:
    """Функция общей маскировки карты и счета"""


# card_account_type_and_card_number - тип карты/счета и номер карты/


def get_data(input_info: str) -> str:
    """Возвращает преобразованное значение даты"""

    cut_date = input_info[:10].split("-")
    return ".".join(cut_date[::-1])

Напишите функцию, которая принимает на вход строку вида
2018-07-11T02:26:18.671407
 и возвращает строку с датой в виде
11.07.2018
.