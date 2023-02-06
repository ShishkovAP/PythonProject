
def get_list_of_wagon(*dargs):
    list_to_return = []
    for dict_element in dargs:
        list_to_return.append(dict_element)
    return list_to_return


def fix_list_of_wagons(list1, list2):
    # функция расставляет вагоны по своим местам:
    #   на первое место ставится локомотив (вагон с ID = 1)
    #   первые 2 элемента из list1 переносятчя в конец списка
    #   элементы list2 ставятся после локомотива

    # копируем элементы list2 в новый список
    list_to_return = list2.copy()
    # вставляем идентификатор локомотива на первое место
    list_to_return.insert(0, list1[2])
    # удаляем идентификатор локомотива из list1
    list1.pop(2)
    list2_count = len(list2)
    # вставляем элементы list1 в общий список
    list_to_return.extend(list1)
    # переносим первые 2 элемента list1 в конец общего списка
    list_to_return.append(list_to_return[list2_count + 1])
    list_to_return.append(list_to_return[list2_count + 2])
    # удаляем первые 2 элемента list1 из общего списка (они перенесены в конец)
    list_to_return.pop(list_to_return[list2_count + 2])
    list_to_return.pop(list_to_return[list2_count + 1])
    if list_to_return[0] != 1:
        print("Исходные данные некорректны. Проверьте элементы списка list1.")
    return list_to_return


def add_missing_stops(from_to, **dargs):
    # первый параметр является словарем - копируем его в словарь, который возвращает функция
    dict_return = from_to.copy()
    list_to_dict = []
    # для каждого параметра из dargs добавляем значение в список
    for stop in dargs:
        list_to_dict.append(dargs[stop])
    dict_return["stops"] = list_to_dict
    return dict_return


def fix_wagon_depot(tuples):
    # функция формирует список вагонов разных цветов так, чтобы получились столбцы из одинаковых вагонов.
    list_return = []
    red_list    = tuples[0]
    blue_list   = tuples[1]
    orange_list = tuples[2]
    list_one    = [red_list[0], blue_list[0], orange_list[0]]
    list_two    = [red_list[1], blue_list[1], orange_list[1]]
    list_three  = [red_list[2], blue_list[2], orange_list[2]]

    list_return.append(list_one)
    list_return.append(list_two)
    list_return.append(list_three)
    return list_return


def extend_route_information(dict_one, dict_two):
    dict_return = dict_one.copy()
    # перебираем элементы второго параметра (словаря) и добавляем каждый элемент в возвращаемый словарь
    for key, value in dict_two.items():
        dict_return[key] = value
    return dict_return


if __name__ == '__main__':
    list_to_print = get_list_of_wagon(1, 5, 7, 8, 4, 9)
    fix_list_wagons = fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    add_missing = add_missing_stops({"from": "Larnaka", "to": "Novosibirsk"},
                                    stop_1="Dubai", stop_2="Bishkek",
                                    stop_3="Kuala-Lumpur", stop_4="Tbilisi",
                                    stop_5="Sochi")
    extend_route = extend_route_information({"from": "Larnaka", "to": "Novosibirsk"}, {"length": "100", "speed": "50"})
    wagon_depot = fix_wagon_depot([
                                [(2, "red"), (4, "red"), (8, "red")],
                                [(5, "blue"), (9, "blue"), (13, "blue")],
                                [(3, "orange"), (7, "orange"), (11, "orange")],
                                ])
    print(list_to_print)
    print(fix_list_wagons)
    print(add_missing)
    print(extend_route)
    for list_of_list in wagon_depot:
        print(list_of_list, sep = '\n')