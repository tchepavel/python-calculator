import operator
import typing as tp

_NUM2STR: dict[int, str] = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто",
    100: "сто"
}

_STR2NUM: dict[str, int] = {v: k for k, v in _NUM2STR.items()}

_BINARY_OPERATORS: dict[str, tp.Callable[[tp.Any, tp.Any], tp.Any]] = {
        'умножить': operator.mul,
        'разделить': operator.truediv,
        'плюс': operator.add,
        'минус': operator.sub,
        'и': operator.and_,
        'ксор': operator.xor,
        'или': operator.or_,
}


def get_str_from_int(n: int) -> str:
    res = []
    deg10 = 1
    while deg10 < n:
        deg10 *= 10
    deg10 /= 10
    while n > 0:
        if n in _NUM2STR:
            res.append(_NUM2STR[n])
            break
        new_n = n % deg10
        digit = n - new_n
        n = new_n
        assert digit in _NUM2STR, f"Такого числа {digit} нет в словаре чисел"
        res.append(_NUM2STR[digit])

    return " ".join(res)


def get_int_from_str(string: str) -> int:
    tokens = string.split(' ')
    first_num = 0
    second_num = 0
    op = None
    add_to_second = False
    for token in tokens:
        if token == "на":
            continue
        if token in _BINARY_OPERATORS:
            op = _BINARY_OPERATORS[token]
            add_to_second = True
            continue
        assert token in _STR2NUM, f"Такого названия числа {token} нет в словаре названий"
        if add_to_second:
            second_num += _STR2NUM[token]
        else:
            first_num += _STR2NUM[token]
    assert op is not None, "В выражении не было операции"
    return op(first_num, second_num)




