from unittest import TestCase
from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


# class TestCalculator(TestCase):
#     def test_plus(self):
#         data = {
#             '2+2': 4,
#             '3+7': 10,
#             '9+0': 9,
#             '945+1': 946,
#             '101+ 11': 112
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     def test_minus(self):
#         data = {
#             '22-2': 20,
#             '1 -3': -2,
#             '105-100': 5,
#             '101-11': 90
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     def test_many_operations(self):
#         data = {
#             '2+2-2': 2,
#             '100 - 56+3': 47,
#             '10': 10
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     # def test_single_int_with_operation_sign(self):
#     #     with self.assertRaises(Exception) as e:
#     #         lexer = Lexer('3+3+')
#     #         interpreter = Parser(lexer)
#     #         result = interpreter.expr()
#     #     self.assertEqual('Неверный синтаксис', e.exception.args[0])
#
#     def test_div_multy(self):
#         data = {
#             '2*2/3': 1,
#             '293 /4': 73,
#             '2': 2,
#             '3 * 1': 3
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     def test_different_operations(self):
#         data = {
#             '2+2*2': 6,
#             '3 - 3 * 100': -297,
#             '3-3+ 0': 0
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     def test_with_brackets(self):
#         data = {
#             '26+(2*2)': 30,
#             '2*(3-3)+6': 6,
#             '2+3*(100+2)': 308
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
#
#     def test_unary_operators(self):
#         data = {
#             '-----3': -3,
#             '5+ --1': 6,
#             '+30/-3': -10
#         }
#         for input_data, waited_result in data.items():
#             lexer = Lexer(input_data)
#             parser = Parser(lexer)
#             interpreter = Interpreter(parser)
#             result = interpreter.interpret()
#             self.assertEqual(waited_result, result)
