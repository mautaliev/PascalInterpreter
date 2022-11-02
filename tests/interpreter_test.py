from unittest import TestCase
from parser import Parser
from lexer import Lexer
from interpreter import Interpreter
from bin_digits import BinaryDigit


class TestInterpreter(TestCase):
    def test_types(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.declare_scope, {'a': BinaryDigit})

    def test_variables(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.global_scope, {'a': BinaryDigit.from_decimal(5)})

    def test_print(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11;
            WRITELN(a)
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.print_str, '101\n')

    def test_management_statement_case(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11;
            CASE a OF
                101: a := a+1;
                1010: a := a+10
            END
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.global_scope, {'a': BinaryDigit.from_decimal(6)})
