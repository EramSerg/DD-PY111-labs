def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    bracket_meetings = 0
    for bracket in brackets_row:
        if bracket == '(':
            bracket_meetings += 1
        elif bracket == ')':
            bracket_meetings -= 1
            if bracket_meetings < 0:
                return False

    return bracket_meetings == 0


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False