"""
Запуск интерпретатора
"""

from parser import Parser
from lexer import Lexer
from interpreter import Interpreter


# TODO: обернуть интерпретатор во фласк
#  + сделать историю ввода (через записи в БД)
def main():
    while True:
        try:
            text = input('> ')
        except EOFError:
            break
        if not text: continue
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
