"""Повышенная сложность №6. Декоратор с параметрами.

@retry(attempts=3, exceptions=(ConnectionError,), delay=0.5)
повторяет вызов функции, если она выбросила одно из указанных
исключений. Декоратор с параметрами — это функция, которая возвращает
обычный декоратор, поэтому уровней вложенности три:
retry(параметры) -> decorator(func) -> wrapper(*args, **kwargs).
"""

import functools
import time


def retry(attempts=3, exceptions=(Exception,), delay=0.0):
    if attempts < 1:
        raise ValueError("attempts должно быть не меньше 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    wrapper.failures += 1
                    if attempt == attempts:
                        raise
                    if delay:
                        time.sleep(delay)

        wrapper.failures = 0
        return wrapper

    return decorator
