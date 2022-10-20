"""
Класс интерпретатора
"""

from token_class import Token
from const import EOF, INTEGER, PLUS


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        """Вызвать исключение"""
        raise Exception('Ошибка разбора строки')

    def get_next_token(self):
        """
        Лексический анализатор
        Метод разбивает входную строку на токены. Один токен за раз
        :return:
        """
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]
        if current_char.isdigit():
            self.pos += 1
            return Token(INTEGER, int(current_char))

        if current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)

        # дошли досюда = ошибка
        self.error()

    def eat(self, token_type):
        """
        Проверяем, подходит ли текущий токен под тот, который мы ожидаем
        :param token_type:
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """
        Непосредственно интерпретируем
        :return:
        """
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result