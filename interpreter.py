"""
Класс интерпретатора
"""

from lexer import Lexer
from const import INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN


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
        """Нетерминальное слово factor"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        """Нетерминальное слово term"""
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

    def expr(self):
        """Нетерминальное слово expr"""
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
        return result
