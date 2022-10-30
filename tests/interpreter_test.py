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
        self.assertEqual(interpreter.DECLARE_SCOPE, {'a': int})

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
        self.assertEqual(interpreter.GLOBAL_SCOPE, {'a': 5})
