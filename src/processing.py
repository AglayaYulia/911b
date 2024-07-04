def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    # list_of_dictionaries - список словарей (перевод), state - состояние (перевод),
    """Функция фильтрации операций по ключу "state" """

    list_by_state = []
    for data_dict in list_of_dictionaries:
        if data_dict["state"] == state:
            list_by_state.append(data_dict)
    return list_by_state


def sort_by_date(data_list: list[dict], is_sort_reverse: bool = True) -> list[dict]:
    """Функция сортировки операций по дате"""

    return sorted(data_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
                  reverse=is_sort_reverse)

# напишите функцию filter_by_state, которая принимает список словарей и опционально значение для ключа
# state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
# у которых ключstate соответствует указанному значению.
# В том же модуле напишите функцию sort_by_date,
# которая принимает список словарей и необязательный параметр,
# задающий порядок сортировки (по умолчанию — убывание).
# Функция должна возвращать новый список, отсортированный по дате (date).
