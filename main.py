"""Лабораторная работа №4, вариант 2 — демонстрация."""

import logging
import random
import sys
from itertools import islice

from call_logger import log_calls
from evens import get_even, iter_even
from factorial import factorial, factorial_table
from memoize import fibonacci
from retry import retry


@log_calls
def average(values):
    return sum(values) / len(values)


@retry(attempts=5, exceptions=(ConnectionError,))
def unstable_request():
    """Имитация запроса к серверу, который отвечает через раз."""
    if random.random() < 0.5:
        raise ConnectionError("сервер не ответил")
    return "данные получены"


def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="  [LOG] %(message)s")

    data = [7, 12, 5, 8, 3, 20, 14, 1]
    print("Список:", data)
    print("Чётные (filter + lambda):", get_even(data))
    print("Первые два чётных из генератора:", list(islice(iter_even(data), 2)))

    print("\nФакториал через reduce:")
    print("  10! =", factorial(10))
    print("  таблица 0!..7!:", factorial_table(7))

    print("\nДекоратор логирования:")
    average([2, 4, 9])
    try:
        average([])
    except ZeroDivisionError:
        print("  исключение проброшено дальше")

    print("\nМемоизация:")
    print("  fibonacci(90) =", fibonacci(90))
    print("  статистика кэша:", fibonacci.cache_info())

    print("\nДекоратор с параметрами @retry(attempts=5):")
    random.seed(3)
    print("  результат:", unstable_request())
    print("  неудачных попыток до успеха:", unstable_request.failures)


if __name__ == "__main__":
    main()
