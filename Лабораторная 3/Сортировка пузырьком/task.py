import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    count = 1

    while count != 0:
        count = 0
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                count += 1

    return container


if __name__ == '__main__':
    lst = [2, 3, 6, 1, 8, 1, 6, 8, 4, 7]
    assert sort(lst) == [1, 1, 2, 3, 4, 6, 6, 7, 8, 8]

    lst1 = [0, 2, 9, 1, 9, 7, 8, 3, 0, 0]
    assert sort(lst1) == [0, 0, 0, 1, 2, 3, 7, 8, 9, 9]

    lst2 = []
    assert sort(lst2) == []

    lst_rand = [random.randint(0, 9) for x in range(10)]
    assert sort(lst_rand) == sorted(lst_rand)
