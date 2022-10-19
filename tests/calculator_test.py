from unittest import TestCase
from main import Interpreter


class TestCalculator(TestCase):
    def test_plus(self):
        data = {
            '2+2': 5,
            '3+7': 10,
            '9+0': 9
        }
        for input_data, waited_result in data.items():
            interpreter = Interpreter(input_data)
            result = interpreter.expr()
            self.assertEqual(waited_result, result)