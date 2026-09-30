"""Повышенная сложность №2. Мемоизация функции через декоратор."""

import functools


def memoize(func):
    """Запоминает результаты вызовов в словаре.

    Ключ — кортеж позиционных аргументов и отсортированных именованных,
    поэтому аргументы должны быть хешируемыми. У обёртки есть:
      cache        — сам словарь с результатами;
      cache_info() — сколько было попаданий и промахов;
      cache_clear() — очистить кэш.
    """
    cache = {}
    stats = {"hits": 0, "misses": 0}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            stats["hits"] += 1
            return cache[key]
        stats["misses"] += 1
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    def cache_info():
        return {"hits": stats["hits"], "misses": stats["misses"],
                "size": len(cache)}

    def cache_clear():
        cache.clear()
        stats["hits"] = stats["misses"] = 0

    wrapper.cache = cache
    wrapper.cache_info = cache_info
    wrapper.cache_clear = cache_clear
    return wrapper


@memoize
def fibonacci(n):
    """Рекурсивный Фибоначчи: без мемоизации растёт экспоненциально."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
