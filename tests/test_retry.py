import unittest
from unittest import mock

from retry import retry


def make_flaky(fail_times, error=ConnectionError):
    """Функция, которая падает первые fail_times раз, потом отвечает 'ok'."""
    state = {"calls": 0}

    def flaky():
        state["calls"] += 1
        if state["calls"] <= fail_times:
            raise error("сбой")
        return "ok"

    return flaky, state


class TestRetry(unittest.TestCase):
    def test_succeeds_after_failures(self):
        flaky, state = make_flaky(2)
        wrapped = retry(attempts=3)(flaky)
        self.assertEqual(wrapped(), "ok")
        self.assertEqual(state["calls"], 3)
        self.assertEqual(wrapped.failures, 2)

    def test_gives_up_after_attempts(self):
        flaky, state = make_flaky(5)
        wrapped = retry(attempts=2)(flaky)
        with self.assertRaises(ConnectionError):
            wrapped()
        self.assertEqual(state["calls"], 2)

    def test_other_exceptions_not_retried(self):
        flaky, state = make_flaky(1, error=KeyError)
        wrapped = retry(attempts=3, exceptions=(ConnectionError,))(flaky)
        with self.assertRaises(KeyError):
            wrapped()
        self.assertEqual(state["calls"], 1)

    def test_delay_between_attempts(self):
        flaky, _ = make_flaky(2)
        with mock.patch("retry.time.sleep") as sleep:
            retry(attempts=3, delay=0.5)(flaky)()
        self.assertEqual(sleep.call_count, 2)
        sleep.assert_called_with(0.5)

    def test_decorator_syntax_and_arguments(self):
        @retry(attempts=2)
        def add(a, b):
            """Сумма."""
            return a + b

        self.assertEqual(add(2, b=3), 5)
        self.assertEqual(add.__name__, "add")

    def test_invalid_attempts(self):
        with self.assertRaises(ValueError):
            retry(attempts=0)


if __name__ == "__main__":
    unittest.main()
