"""
Класс интерпретатора - обходим узлы
"""

from const import PLUS, MINUS, MUL, DIV
from abract_syntax_tree import BinOp, UnaryOp, Num, Program, DeclarationList, StatementList, Declaration, Type


class NodeVisitor(object):
    def __init__(self):
        self.DECLARE_SCOPE = {}
        self.GLOBAL_SCOPE = {}

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Не существует реализации метода visit_{type(node).__name__}')


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        super().__init__()
        self.parser = parser

    def visit_BinOp(self, node: BinOp):
        mapping = {
            PLUS: lambda x, y: x+y,
            MINUS: lambda x, y: x-y,
            MUL: lambda x, y: x*y,
            DIV: lambda x, y: int(x/y)
        }
        return mapping.get(node.op.type)(self.visit(node.left), self.visit(node.right))

    def visit_UnaryOp(self, node: UnaryOp):
        mapping = {
            PLUS: lambda x: +x,
            MINUS: lambda x: -x
        }
        return mapping.get(node.op.type)(self.visit(node.expr))

    def visit_Num(self, node: Num):
        return node.value

    def visit_StatementList(self, node: StatementList):
        for child in node.children:
            self.visit(child)

    def visit_NoOp(self, node):
        pass

    def visit_Assign(self, node):
        var_name = node.left.value
        var_value = self.visit(node.right)
        var_type = self.DECLARE_SCOPE.get(var_name)
        if not var_type:
            raise Exception(f'Попытка присвоить значения необъявленной переменной {var_name}')
        if not isinstance(var_value, var_type):
            raise Exception(f'Несоответствие типа: переменная {var_name} имеет тип {var_type}, '
                            f'пытались присвоить {type(var_value)}')
        self.GLOBAL_SCOPE[var_name] = var_value

    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val:
            return val
        raise NameError(repr(var_name))

    def visit_Program(self, node: Program):
        self.visit(node.declaration_list)
        self.visit(node.statement_list)

    def visit_DeclarationList(self, node: DeclarationList):
        for item in node.children:
            self.visit(item)

    def visit_Declaration(self, node: Declaration):
        var_name = node.variable.value
        self.DECLARE_SCOPE[var_name] = self.visit(node.type)

    def visit_Type(self, node: Type):
        mapping = {
            'INTEGER': int,
            'CHAR': str,
            'BOOLEAN': bool
        }
        return mapping.get(node.type_value)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
