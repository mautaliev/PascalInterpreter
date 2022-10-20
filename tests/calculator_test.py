from unittest import TestCase
from interpreter import Interpreter
from lexer import Lexer


class TestCalculator(TestCase):
    # def test_plus(self):
    #     data = {
    #         '2+2': 4,
    #         '3+7': 10,
    #         '9+0': 9,
    #         '945+1': 946,
    #         '101+ 11': 112
    #     }
    #     for input_data, waited_result in data.items():
    #         interpreter = Interpreter(input_data)
    #         result = interpreter.expr()
    #         self.assertEqual(waited_result, result)
    #
    # def test_minus(self):
    #     data = {
    #         '22-2': 20,
    #         '1 -3': -2,
    #         '105-100': 5,
    #         '101-11': 90
    #     }
    #     for input_data, waited_result in data.items():
    #         interpreter = Interpreter(input_data)
    #         result = interpreter.expr()
    #         self.assertEqual(waited_result, result)
    #
    # def test_many_operations(self):
    #     data = {
    #         '2+2-2': 2,
    #         '100 - 56+3': 47,
    #         '10': 10
    #     }
    #     for input_data, waited_result in data.items():
    #         interpreter = Interpreter(input_data)
    #         result = interpreter.expr()
    #         self.assertEqual(waited_result, result)
    #
    # def test_single_int_with_operation_sign(self):
    #     with self.assertRaises(Exception) as e:
    #         interpreter = Interpreter('3+')
    #         interpreter.expr()
    #     self.assertEqual('Ошибка разбора строки', e.exception.args[0])

    def test_div_multy(self):
        data = {
            '2*2/3': 1,
            '293 /4': 73,
            '2': 2,
            '3 * 1': 3
        }
        for input_data, waited_result in data.items():
            lexer = Lexer(input_data)
            interpreter = Interpreter(lexer)
            result = interpreter.expr()
            self.assertEqual(waited_result, result)
