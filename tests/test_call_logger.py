import unittest

from call_logger import log_calls


@log_calls
def divide(a, b):
    """Деление."""
    return a / b


class TestLogCalls(unittest.TestCase):
    def test_logs_call_and_result(self):
        with self.assertLogs("lab4", level="INFO") as logs:
            self.assertEqual(divide(6, b=3), 2.0)
        self.assertEqual(logs.output, [
            "INFO:lab4:вызов divide(6, b=3)",
            "INFO:lab4:divide(6, b=3) вернула 2.0",
        ])

    def test_logs_exception_and_reraises(self):
        with self.assertLogs("lab4", level="INFO") as logs:
            with self.assertRaises(ZeroDivisionError):
                divide(1, 0)
        self.assertTrue(logs.output[-1].startswith(
            "ERROR:lab4:divide(1, 0) завершилась ошибкой"))

    def test_metadata(self):
        self.assertEqual(divide.__name__, "divide")
        self.assertEqual(divide.__doc__, "Деление.")


if __name__ == "__main__":
    unittest.main()
