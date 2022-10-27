from unittest import TestCase
from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


class TestInterpreter(TestCase):
    def test_variables(self):
        text = """
        BEGIN
            BEGIN
                number := 2;
                a := number;
                b := 10 * a + 10 * number / 4;
                c := a - - b
            END;
            x := 11;
        END.
        """
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        self.assertEqual(interpreter.GLOBAL_SCOPE, {'a': 2, 'x': 11, 'c': 27, 'b': 25, 'number': 2})
