"""
Реализация AST
"""

from token_class import Token


class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
