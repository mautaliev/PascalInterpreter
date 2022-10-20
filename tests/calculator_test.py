from unittest import TestCase
from interpreter import Interpreter


class TestCalculator(TestCase):
    def test_plus(self):
        data = {
            '2+2': 4,
            '3+7': 10,
            '9+0': 9,
            '945+1': 946,
            '101+11': 112
        }
        for input_data, waited_result in data.items():
            interpreter = Interpreter(input_data)
            result = interpreter.expr()
            self.assertEqual(waited_result, result)

    def minus_test(self):
        data = {
            '22-2': 20,
            '1-3': -2,
            '105-100': 5,
            '101-11': 90
        }
        for input_data, waited_result in data.items():
            interpreter = Interpreter(input_data)
            result = interpreter.expr()
            self.assertEqual(waited_result, result)
