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


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value


class StatementList(AST):
    def __init__(self):
        self.children = []


class DeclarationList(AST):
    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.type_value = token.value


class Declaration(AST):
    def __init__(self, variable, var_type):
        self.variable = variable
        self.type = var_type


class NoOp(AST):
    """Пустое содержание"""
    def __init__(self):
        pass


class Program(AST):
    def __init__(self, declaration_list, statement_list):
        self.declaration_list = declaration_list
        self.statement_list = statement_list
