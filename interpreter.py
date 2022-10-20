"""
Класс интерпретатора
"""

from lexer import Lexer
from const import INTEGER, MUL, DIV


class Interpreter(object):
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        """Вызвать исключение"""
        raise Exception('Неверный синтаксис')

    def eat(self, token_type):
        """
        Проверяем, подходит ли текущий токен под тот, который мы ожидаем
        :param token_type:
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Возвращает интерпретируемое число"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """
        Непосредственно интерпретируем
        :return:
        """
        result = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = int(result * self.factor())
            elif token.type == DIV:
                self.eat(DIV)
                result = int(result / self.factor())
        return result
