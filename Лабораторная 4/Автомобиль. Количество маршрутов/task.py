from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    result_lst = [[0] * n for m in range(m)]
    for y in range(m):
        for x in range(n):
            if (x - 1) >= 0:
                result_lst[y][x] += 1 + y
            if (y - 1) >= 0:
                result_lst[y][x] += 1 + x
            if (x - 1) >= 0 and (y - 1) >= 0:
                result_lst[y][x] += 1

    return result_lst


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
