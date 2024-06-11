import random

from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    sort_lst = []

    counting_elem = [0] * len(container)

    for i in container:
        counting_elem[i] += 1

    for ind, value in enumerate(counting_elem):
        if value > 0:
            sort_lst.extend([ind] * value)

    return sort_lst


if __name__ == '__main__':
    lst = [5, 2, 6, 7, 8, 4, 3, 0, 4, 9]
    assert sort(lst) == [0, 2, 3, 4, 4, 5, 6, 7, 8, 9]

    lst1 = [8, 4, 8, 4, 2, 7, 7, 4, 4, 0]
    assert sort(lst1) == [0, 2, 4, 4, 4, 4, 7, 7, 8, 8]

    lst2 = []
    assert sort(lst2) == []

    lst_rand = [random.randint(0, 9) for x in range(10)]
    assert sort(lst_rand) == sorted(lst_rand)
