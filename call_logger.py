"""Средняя сложность №7. Декоратор для логирования вызова функции.

Используется стандартный модуль logging: сообщения можно направить
в консоль или файл настройкой logging, не меняя сам декоратор.
"""

import functools
import logging

logger = logging.getLogger("lab4")


def log_calls(func):
    """Логирует аргументы, результат и исключения функции."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arguments = [repr(a) for a in args]
        arguments += [f"{key}={value!r}" for key, value in kwargs.items()]
        call = f"{func.__name__}({', '.join(arguments)})"
        logger.info("вызов %s", call)
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            logger.error("%s завершилась ошибкой: %r", call, error)
            raise
        logger.info("%s вернула %r", call, result)
        return result

    return wrapper
