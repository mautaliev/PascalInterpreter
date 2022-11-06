"""
Лексический анализатор
Разбирает, что написано
"""

from token_class import Token
from const import PLUS, MINUS, MUL, DIV, EOF, INT, LPAREN, RPAREN, RESERVED_KEYWORDS, ID, ASSIGN, SEMI, DOT, COLON, \
    POSSIBLE_DIGITS, TEXT_CONSTANT
from bin_digits import BinaryDigit


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        """Вызвать исключение"""
        raise Exception(f'Ошибка в строке {self.current_line}: неверный символ')

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
        while self.current_char is not None and self.current_char in POSSIBLE_DIGITS:
            result += self.current_char
            self.advance()
        return BinaryDigit(result)

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

            if self.current_char in POSSIBLE_DIGITS:
                return Token(INT, self.integer())

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

            if self.current_char == ':':
                self.advance()
                return Token(COLON, ':')

            if self.current_char == "'":
                self.advance()
                return self.text_constant()
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
        """
        Понять, что читаем: зарезервированное слово или идентификатор
        :return:
        """
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        token = RESERVED_KEYWORDS.get(result, Token(ID, result))
        return token

    def text_constant(self):
        """
        Понять, что читаем текстовую константу
        :return:
        """
        result = ''
        while self.current_char not in (None, "'"):
            result += self.current_char
            self.advance()
        self.advance()
        return Token(TEXT_CONSTANT, result)

    @property
    def current_line(self):
        data = self.text.split('\n')

        next_endline = self.text[self.pos:].find('\n')
        next_endline = self.pos + next_endline if next_endline != -1 else len(self.text)

        last_endline = self.text[:self.pos][::-1].find('\n')
        last_endline = self.pos - last_endline if last_endline != -1 else 0

        current_line = self.text[last_endline:next_endline if next_endline else next_endline]
        try:
            current_line_num = data.index(current_line) + 1
        except:
            current_line_num = -1
        return current_line_num if current_line_num != -1 else 'undefined'
