"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise IndexError('Список пустой!')

    min_value = arr[0]  # реализовать итеративный линейный поиск

    for value in arr:
        if value < min_value:
            min_value = value

    return min_value


if __name__ == '__main__':
    #arr = []
    #assert min_search(arr)

    arr_1 = [1, 2, 3, 7, 9, 0]
    assert min_search(arr_1) == 0

    arr_2 = [765, 345, 45, 765, 999, 45]
    assert min_search(arr_2) == 45
