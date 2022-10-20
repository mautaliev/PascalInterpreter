"""
Класс интерпретатора
"""

from token_class import Token
from const import EOF, INTEGER, PLUS, MINUS


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        """Вызвать исключение"""
        raise Exception('Ошибка разбора строки')

    def advance(self):
        """Передвинуть текущую позицию и установить текущий символ"""
        self.pos += 1
        self.current_char = None if self.pos > len(self.text) - 1 else self.text[self.pos]

    def skip_whitespace(self):
        """Пропустить пробел"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """
        Получить число. Позволяет получать многозначные числа путём чтения, пока символы не перестанут быть цифрами
        """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """
        Лексический анализатор
        Метод разбивает входную строку на токены. Один токен за раз
        :return:
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            # дошли досюда = ошибка
            self.error()
        return Token(EOF, None)

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
        self.eat(PLUS) if op.type == PLUS else self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value if op.type == PLUS else left.value - right.value
        return result
