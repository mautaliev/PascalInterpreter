"""
Работа с бинарными числами
"""


def is_binary_digit(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, BinaryDigit):
                raise Exception("Ошибка: попытка работы с небинарными числами")
        return func(*args)
    return wrapper


class BinaryDigit:
    def __init__(self, string, negative=False):
        if string[0] == '-':
            negative = True
            string = string[1:]
        self.data = string
        self.negative = negative
        self.dec = None
        self.calculate()
        self.test_max_length()

    def calculate(self):
        self.dec = 0
        reversed_string = self.data[::-1]
        for index in range(len(self.data)):
            self.dec += 2**index*int(reversed_string[index])
        self.dec *= -1 if self.negative else 1

    def __str__(self):
        return f'{"-" if self.negative else ""}{self.data}'

    def __repr__(self):
        return f'{"negative" if self.negative else ""} {self.data}: {self.dec}'

    @is_binary_digit
    def __add__(self, other):
        return BinaryDigit.from_decimal(self.dec + other.dec)

    @is_binary_digit
    def __sub__(self, other):
        return BinaryDigit.from_decimal(self.dec - other.dec)

    @is_binary_digit
    def __mul__(self, other):
        return BinaryDigit.from_decimal(self.dec * other.dec)

    @is_binary_digit
    def __truediv__(self, other):
        if not other.dec:
            raise Exception('Деление на ноль')
        return BinaryDigit.from_decimal(int(self.dec / other.dec))

    @is_binary_digit
    def __lshift__(self, other):
        return BinaryDigit.from_decimal(int(self.dec << other.dec))

    @is_binary_digit
    def __rshift__(self, other):
        return BinaryDigit.from_decimal(int(self.dec >> other.dec))

    @is_binary_digit
    def __bool__(self):
        return bool(self.dec)

    @is_binary_digit
    def binary_or(self, other):
        negative_flag = self.negative or other.negative
        first_len, second_len = len(self.data), len(other.data)
        first_diff, second_diff = second_len - first_len, first_len - second_len
        first_bin, second_bin = f'{"0"*first_diff}{self.data}', f'{"0"*second_diff}{other.data}'
        result_bin = ''
        for index in range(max([first_len, second_len])):
            result_bin += '1' if int(first_bin[index]) or int(second_bin[index]) else '0'
        return BinaryDigit(result_bin, negative_flag)

    @is_binary_digit
    def binary_and(self, other):
        negative_flag = self.negative and other.negative
        first_len, second_len = len(self.data), len(other.data)
        first_diff, second_diff = second_len - first_len, first_len - second_len
        first_bin, second_bin = f'{"0"*first_diff}{self.data}', f'{"0"*second_diff}{other.data}'
        result_bin = ''
        for index in range(max([first_len, second_len])):
            result_bin += '1' if int(first_bin[index]) and int(second_bin[index]) else '0'
        return BinaryDigit(result_bin, negative_flag)

    def __pos__(self):
        return BinaryDigit.from_decimal(+self.dec)

    def __neg__(self):
        return BinaryDigit.from_decimal(-self.dec)

    @is_binary_digit
    def __eq__(self, other):
        return self.dec == other.dec

    def __hash__(self):
        return hash((self.data, self.dec))

    @staticmethod
    def from_decimal(decimal: int):
        negative = decimal < 0
        binary = bin(decimal if not negative else +decimal)
        string = str(binary)[2 if not negative else 3:]
        return BinaryDigit(string, negative)

    def test_max_length(self):
        if len(self.data) > 48:
            raise Exception('Переполнение максимального размера допустимого числа: 6 байт')
