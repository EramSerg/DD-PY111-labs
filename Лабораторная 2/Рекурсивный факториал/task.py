def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # реализовать рекурсивный алгоритм нахождения факториала

    if n < 0:
        raise ValueError('Число должно быть больше либо равно нулю!')

    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    #assert factorial_recursive(-5)
    assert factorial_recursive(0) == 1
    assert factorial_recursive(3) == 6
    assert factorial_recursive(4) == 24
    assert factorial_recursive(5) == 120
