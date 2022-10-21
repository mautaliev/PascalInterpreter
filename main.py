"""
Запуск интерпретатора
"""

from interpreter import Interpreter
from lexer import Lexer


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
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
