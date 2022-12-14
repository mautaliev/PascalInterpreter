from unittest import TestCase
from parser import Parser
from lexer import Lexer
from interpreter import Interpreter
from bin_digits import BinaryDigit
from testing_const import TEST_TYPES_TEXT, TEST_VARIABLES_TEXT, TEST_PRINT_TEXT, TEST_MANAGEMENT_STATEMENT_TEXT, \
    TEST_OPERATIONS_DATA, TEST_OPTIMIZE_DATA, TEST_ERRORS_DATA, TEST_UNDECLARED_ID


class TestInterpreter(TestCase):
    def test_types(self):
        lexer = Lexer(TEST_TYPES_TEXT)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.declare_scope, {'a': BinaryDigit, 'b': str})

    def test_variables(self):
        lexer = Lexer(TEST_VARIABLES_TEXT)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(
            interpreter.global_scope,
            {'a': BinaryDigit.from_decimal(5), 'b': 'tralala'}
        )

    def test_print(self):
        lexer = Lexer(TEST_PRINT_TEXT)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.print_str, '101\n')

    def test_management_statement_case(self):
        lexer = Lexer(TEST_MANAGEMENT_STATEMENT_TEXT)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.global_scope, {'a': BinaryDigit.from_decimal(6)})

    def test_operations(self):
        for text, result in TEST_OPERATIONS_DATA.items():
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            interpreter.interpret()
            self.assertEqual(interpreter.global_scope, result)

    def test_optimize(self):
        for text, result in TEST_OPTIMIZE_DATA.items():
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            interpreter.interpret()
            self.assertEqual(interpreter.get_optimized_code(), result)

    def test_errors(self):
        for text, result in TEST_ERRORS_DATA.items():
            with self.assertRaises(Exception) as exc:
                lexer = Lexer(text)
                parser = Parser(lexer)
                interpreter = Interpreter(parser)
                interpreter.interpret()
            self.assertEqual(exc.exception.args[0], result)

    def test_undeclared_identify(self):
        with self.assertRaises(Exception) as exc:
            lexer = Lexer(TEST_UNDECLARED_ID)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            interpreter.interpret()
        self.assertEqual(exc.exception.args[0], "???????????????????????? ?????????????????????????? ????????????????????: 'b'")
