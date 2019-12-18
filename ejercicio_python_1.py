'''
Defina una funcion ejercicio python 1
Dado una lista de datos de entrada:
1. Se quiere obtener los ultimos 5 elementos.
2. Los elementos que estan entre 18 y 25 sin repetidos
3. El menor y el mayor elemento
'''


def is_valid_list(list_param):
    return (list_param is None or
            type(list_param) is not list or
            len(list_param) == 0)


def get_last_five_elements(list_param):
    i = -1
    last_five_elements = []
    while(abs(i) <= 5 and abs(i) <= len(list_param)):
        last_five_elements.append(list_param[i])
        i -= 1
    return last_five_elements


def get_elements_between_18_and_25(list_param):
    elements_between_18_and_25 = filter(lambda elem: type(
        elem) in [int, float] and 18 <= elem and elem <= 25, list_param)
    return elements_between_18_and_25


def get_list_of_numbers(list_param):
    numbers_list = []
    [numbers_list.append(item)
     for item in list_param if type(item) in [int, float]]
    return numbers_list


def ejercicio_python_1(list_param):
    print("---------------------------------------")
    if is_valid_list(list_param):
        print("Please, enter a valid list parameter.")
    else:
        # 1. Se quiere obtener los ultimos 5 elementos.
        print("List is fine... Printing last 5 elements:")
        last_five_elements = get_last_five_elements(list_param)
        print(last_five_elements)

        # 2. Los elementos que estan entre 18 y 25 sin repetidos
        print("Getting elements between 18 and 25 without repeated...")
        elements_between_18_and_25 = get_elements_between_18_and_25(list_param)
        set_elements_between_18_and_25 = set(elements_between_18_and_25)
        print(list(set_elements_between_18_and_25))

        # 3. El menor y el mayor elemento
        print("Otaining the minor and major item of the list...")
        numbers_list = get_list_of_numbers(list_param)

        min_value = min(numbers_list)
        max_value = max(numbers_list)
        print(f"The minimum value is {min_value}")
        print(f"The maximum value is {max_value}")
    print("---------------------------------------")


# Tests
ejercicio_python_1(1)
ejercicio_python_1(None)
ejercicio_python_1([])
ejercicio_python_1([1, 2])
ejercicio_python_1([0.9, 1, 2])
ejercicio_python_1([1, {"2": 2}, 3, 4, 5, 6])
ejercicio_python_1([1, 2, 3, 4, 5, 6])
ejercicio_python_1([1, "two", 3, "four", 5, 6])
ejercicio_python_1([1, "two", 3, "four", 5, 6, 19])
ejercicio_python_1([11, 21, 32, 19, 21])
