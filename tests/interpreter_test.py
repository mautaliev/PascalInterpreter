from unittest import TestCase
from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


class TestInterpreter(TestCase):
    def test_types(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 2+3
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.declare_scope, {'a': int})

    def test_variables(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 2+3
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.global_scope, {'a': 5})

    def test_print(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 2+3;
            WRITELN(a)
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.print_str, '5\n')

    def test_management_statement_case(self):
        text = """
        VAR
            a : INTEGER
        BEGIN
            a := 2+3;
            CASE a OF
                5: a := a+1;
                10: a := a+2
            END
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.global_scope, {'a': 6})
