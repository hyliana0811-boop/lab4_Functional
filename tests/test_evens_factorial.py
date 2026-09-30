import math
import types
import unittest

from evens import get_even, iter_even
from factorial import factorial, factorial_table


class TestEvens(unittest.TestCase):
    def test_get_even(self):
        self.assertEqual(get_even([1, 2, 3, 4, 10, 11]), [2, 4, 10])
        self.assertEqual(get_even([-2, -1, 0]), [-2, 0])
        self.assertEqual(get_even([1, 3]), [])

    def test_iter_even_is_lazy(self):
        result = iter_even(range(10))
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [0, 2, 4, 6, 8])


class TestFactorial(unittest.TestCase):
    def test_values(self):
        for n in range(15):
            with self.subTest(n=n):
                self.assertEqual(factorial(n), math.factorial(n))

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_invalid(self):
        for bad in (-1, 2.5, "3"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    factorial(bad)

    def test_table(self):
        self.assertEqual(factorial_table(5), [1, 1, 2, 6, 24, 120])


if __name__ == "__main__":
    unittest.main()
