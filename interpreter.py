"""
Класс интерпретатора - обходим узлы
"""

from const import PLUS, MINUS, MUL, DIV
from abract_syntax_tree import BinOp, UnaryOp, Num


class NodeVisitor(object):
    def __init__(self):
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

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_NoOp(self, node):
        pass

    def visit_Assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val:
            return val
        raise NameError(repr(var_name))

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
