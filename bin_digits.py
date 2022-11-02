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

    def calculate(self):
        self.dec = 0
        reversed_string = self.data[::-1]
        for index in range(len(self.data)):
            self.dec += 2**index*int(reversed_string[index])
        self.dec *= -1 if self.negative else 1

    def __str__(self):
        return f'{"-" if self.negative else ""}{self.data}'

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
        return BinaryDigit.from_decimal(int(self.dec / other.dec))

    @is_binary_digit
    def __lshift__(self, other):
        return BinaryDigit.from_decimal(int(self.dec << other.dec))

    @is_binary_digit
    def __rshift__(self, other):
        return BinaryDigit.from_decimal(int(self.dec >> other.dec))

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
