"""
Класс парсера
"""

from lexer import Lexer
from const import INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, DOT, BEGIN, END, SEMI, ID, ASSIGN, EOF
from abract_syntax_tree import BinOp, UnaryOp, Num, Compound, Var, NoOp, Assign


class Parser(object):
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        """Вызвать исключение"""
        raise Exception('Неверный синтаксис')

    def eat(self, token_type):
        """
        Проверяем, подходит ли текущий токен под тот, который мы ожидаем
        :param token_type:
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """Нетерминальное слово factor"""
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        else:
            node = self.variable()
            return node

    def term(self):
        """Нетерминальное слово term"""
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        """Нетерминальное слово expr"""
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def program(self):
        """program : compound_statement DOT"""
        node = self.compound_statement()
        self.eat(DOT)
        return node

    def compound_statement(self):
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        root = Compound()
        for node in nodes:
            root.children.append(node)

        return root

    def statement_list(self):
        node = self.statement()
        results = [node]
        while self.current_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())

        if self.current_token.type == ID:
            self.error()

        return results

    def statement(self):
        if self.current_token.type == BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == ID:
            node = self.assigment_statement()
        else:
            node = self.empty()
        return node

    def assigment_statement(self):
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def variable(self):
        node = Var(self.current_token)
        self.eat(ID)
        return node

    def empty(self):
        return NoOp()

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error()
        return node
