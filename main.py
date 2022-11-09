"""
Запуск интерпретатора
"""

from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


def interpret(text: str):
    """
    Интерпретировать исходный код
    :param text: исходный код
    :return: объект интепретатора
    """
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.interpret()
    return interpreter
