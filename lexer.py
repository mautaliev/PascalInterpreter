"""
Лексический анализатор
Разбирает, что написано
"""

from token_class import Token
from const import PLUS, MINUS, MUL, DIV, EOF, INTEGER, LPAREN, RPAREN, RESERVED_KEYWORDS, ID, ASSIGN, SEMI, DOT


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        """Вызвать исключение"""
        raise Exception('Неверный символ')

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

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            if self.current_char.isalpha():
                return self._id()

            if self.current_char == ':' and self.peek() == '=':
                self.advance()
                self.advance()
                return Token(ASSIGN, ':=')

            if self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            if self.current_char == '.':
                self.advance()
                return Token(DOT, '.')
            # дошли досюда = ошибка
            self.error()
        return Token(EOF, None)

    def peek(self):
        """
        Прочитать следующий символ без инкрементирования позиции чтения по тексту
        :return:
        """
        peek_pos = self.pos + 1
        return None if peek_pos > len(self.text) - 1 else self.text[peek_pos]

    def _id(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token
