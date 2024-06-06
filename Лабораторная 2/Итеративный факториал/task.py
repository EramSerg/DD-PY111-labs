def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    factorial_value = 1

    if n < 0:
        raise ValueError('Число должно быть больше либо равно нулю!')

    if n == 0:
        return factorial_value

    for value in range(1, n+1):  # реализовать итеративный алгоритм нахождения факториала
        factorial_value *= value

    return factorial_value


if __name__ == '__main__':
    #assert factorial_iterative(-5)
    assert factorial_iterative(0) == 1
    assert factorial_iterative(3) == 6
    assert factorial_iterative(4) == 24
    assert factorial_iterative(5) == 120