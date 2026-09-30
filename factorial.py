"""Средняя сложность №4. Факториал через reduce."""

import operator
from functools import reduce


def factorial(n):
    """n! = 1 * 2 * ... * n, посчитанный свёрткой reduce.

    Начальное значение 1 нужно, чтобы 0! = 1 (range(1, 1) пустой).
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определён для целых n >= 0")
    return reduce(operator.mul, range(1, n + 1), 1)


def factorial_table(limit):
    """Список факториалов 0!..limit! через map."""
    return list(map(factorial, range(limit + 1)))
