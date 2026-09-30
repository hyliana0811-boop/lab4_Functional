"""Средняя сложность №2. Отфильтровать чётные числа из списка."""


def get_even(numbers):
    """Список чётных чисел: filter + lambda."""
    return list(filter(lambda n: n % 2 == 0, numbers))


def iter_even(numbers):
    """Ленивый вариант: генераторное выражение, числа выдаются по одному."""
    return (n for n in numbers if n % 2 == 0)
