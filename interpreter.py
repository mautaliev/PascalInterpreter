"""
Класс интерпретатора - обходим узлы
"""

import re

from lexer import Lexer
from parser import Parser
from const import PLUS, MINUS, MUL, DIV, OR, AND, SHR, SHL
from abract_syntax_tree import BinOp, UnaryOp, Num, Program, DeclarationList, StatementList, Declaration, Type, \
    WriteLn, Choice, ChoiceList, Case, TextConstant
from bin_digits import BinaryDigit


class NodeVisitor(object):
    def __init__(self):
        self.declare_scope = {}
        self.global_scope = {}
        self.print_str = ''

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
            DIV: lambda x, y: x/y,
            OR: lambda x, y: x.binary_or(y),
            AND: lambda x, y: x.binary_and(y),
            SHL: lambda x, y: x << y,
            SHR: lambda x, y: x >> y
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
        var_type = self.declare_scope.get(var_name)
        if not var_type:
            raise Exception(f'Попытка присвоить значения необъявленной переменной {var_name}')
        if not isinstance(var_value, var_type):
            raise Exception(f'Несоответствие типа: переменная {var_name} имеет тип {var_type}, '
                            f'пытались присвоить {type(var_value)}')
        self.global_scope[var_name] = var_value

    def visit_Var(self, node):
        var_name = node.value
        val = self.global_scope.get(var_name)
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
        self.declare_scope[var_name] = self.visit(node.type)

    def visit_Type(self, node: Type):
        mapping = {
            'INTEGER': BinaryDigit,
            'CHAR': str,
            'BOOLEAN': bool
        }
        return mapping.get(node.type_value)

    def visit_WriteLn(self, node: WriteLn):
        var_value = self.visit(node.variable)
        self.print_str = f'{self.print_str}{var_value}\n'

    def visit_Case(self, node: Case):
        variable = self.visit(node.variable)
        mapping = self.visit(node.choose_list)
        return self.visit(mapping.get(variable))

    def visit_ChoiceList(self, node: ChoiceList):
        case_dict = {}
        for item in node.children:
            case_dict.update(self.visit(item))
        return case_dict

    def visit_Choice(self, node: Choice):
        return {self.visit(node.factor): node.assignment}

    def visit_TextConstant(self, node: TextConstant):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

    def get_optimized_code(self) -> str:
        if not self.declare_scope:
            raise Exception('Не найдено объявление ни одной переменной')
        input_text = self.parser.lexer.text
        constant_assignments = self.find_constant_assignment_statements(input_text)
        for assignment in constant_assignments:
            if assignment[1].strip():
                input_text = input_text.replace(assignment[1].strip(),
                                                str(self.calc_optimized_value(assignment[1].strip())),
                                                1)
        return input_text

    @staticmethod
    def calc_optimized_value(expression):
        lexer = Lexer(expression)
        parser = Parser(lexer)
        calculator = Calculator(parser)
        value = calculator.calculate()
        return value

    @staticmethod
    def find_constant_assignment_statements(text: str):
        return re.findall(r'([a-z ]+):=([ 01+/*-]+)', text)


class Calculator(Interpreter):
    def __init__(self, parser):
        super().__init__(parser)

    def calculate(self):
        tree = self.parser.calculate()
        return self.visit(tree)
