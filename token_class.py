"""
Класс токена
Токен = тип + значение
"""


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """
        Строковое представление сущности класса
        :return: строка типа Token({type}, {value})
        """
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        """
        Формальное строковое представление
        :return:
        """
        return self.__str__()
