import unittest

from memoize import fibonacci, memoize


class TestMemoize(unittest.TestCase):
    def test_function_called_once_per_argument(self):
        calls = []

        @memoize
        def square(x):
            calls.append(x)
            return x * x

        self.assertEqual(square(4), 16)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(5), 25)
        self.assertEqual(calls, [4, 5])
        self.assertEqual(square.cache_info(),
                         {"hits": 1, "misses": 2, "size": 2})

    def test_kwargs_order_does_not_matter(self):
        @memoize
        def area(width, height):
            return width * height

        area(width=2, height=3)
        area(height=3, width=2)
        self.assertEqual(area.cache_info()["hits"], 1)

    def test_cache_clear(self):
        @memoize
        def double(x):
            return 2 * x

        double(1)
        double.cache_clear()
        self.assertEqual(double.cache_info(),
                         {"hits": 0, "misses": 0, "size": 0})

    def test_fast_recursive_fibonacci(self):
        fibonacci.cache_clear()
        self.assertEqual(fibonacci(100), 354224848179261915075)
        # каждое значение 0..100 считалось ровно один раз
        self.assertEqual(fibonacci.cache_info()["misses"], 101)


if __name__ == "__main__":
    unittest.main()
