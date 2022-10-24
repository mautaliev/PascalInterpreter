"""
Класс интерпретатора - обходим узлы
"""

from const import PLUS, MINUS, MUL, DIV
from abract_syntax_tree import BinOp, Num


class NodeVisitor(object):
    def __init__(self):
        pass

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

    def visit_Num(self, node: Num):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
