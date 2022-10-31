"""
Класс парсера
"""

from lexer import Lexer
from const import INT, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, DOT, BEGIN, END, SEMI, ID, ASSIGN, EOF, VAR,\
    COLON, INTEGER, CHAR, BOOLEAN, WRITELN, CASE, OF
from abract_syntax_tree import BinOp, UnaryOp, Num, StatementList, DeclarationList, Var, NoOp, Assign, Program, Type,\
    Declaration, WriteLn, Case, ChoiceList, Choice


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
        elif token.type == INT:
            self.eat(INT)
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
        """
        program : VAR declaration_list BEGIN statement_list END.
        :return:
        """
        self.eat(VAR)
        var_node = self.declaration_list()
        self.eat(BEGIN)
        statement_list_node = self.statement_list()
        self.eat(END)
        self.eat(DOT)
        return Program(var_node, statement_list_node)

    def declaration_list(self):
        """
        declaration_list : declaration | declaration_list; declaration
        :return:
        """
        node = self.declaration()
        result = [node]
        while self.current_token.type == SEMI:
            self.eat(SEMI)
            result.append(self.declaration())

        if self.current_token.type == ID:
            self.error()

        root = DeclarationList()
        for item in result:
            root.children.append(item)
        return root

    def declaration(self):
        """
        declaration : variable : type
        :return:
        """
        left = self.variable()
        self.eat(COLON)
        right = self.type()
        return Declaration(left, right)

    def statement_list(self):
        """
        statement_list : statement | statement_list; statement;
        :return:
        """
        node = self.statement()
        result = [node]
        while self.current_token.type == SEMI:
            self.eat(SEMI)
            result.append(self.statement())

        if self.current_token.type == ID:
            self.error()

        root = StatementList()
        for item in result:
            root.children.append(item)

        return root

    def statement(self):
        if self.current_token.type == ID:
            node = self.assignment_statement()
        elif self.current_token.type == WRITELN:
            node = self.writeln()
        elif self.current_token.type in (CASE,):
            node = self.management_statement()
        else:
            node = self.empty()
        return node

    def assignment_statement(self):
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def writeln(self):
        self.eat(WRITELN)
        self.eat(LPAREN)
        node = self.variable()
        self.eat(RPAREN)
        return WriteLn(node)

    def management_statement(self):
        """
        management_statement : case
        :return:
        """
        # используем маппинг, т.к. в теории правило управляющей конструкции
        # может быть расширено: добавлены for, if и т.д...
        mapping = {CASE: self.case}
        return mapping.get(self.current_token.type)()

    def case(self):
        """
        case : CASE variable OF choice_list END
        :return:
        """
        self.eat(CASE)
        case_variable = self.variable()
        self.eat(OF)
        choose_list = self.choice_list()
        self.eat(END)
        return Case(case_variable, choose_list)

    def choice_list(self):
        """
        choice_list : choice | choice_list; choice
        :return:
        """
        node = self.choice()
        result = [node]
        while self.current_token.type == SEMI:
            self.eat(SEMI)
            result.append(self.choice())

        if self.current_token.type == ID:
            self.error()

        root = ChoiceList()
        for item in result:
            root.children.append(item)
        return root

    def choice(self):
        """
        choice : <factor>: <assignment_statement>
        :return:
        """
        factor = self.factor()
        self.eat(COLON)
        assignment = self.assignment_statement()
        return Choice(factor, assignment)

    def variable(self):
        node = Var(self.current_token)
        self.eat(ID)
        return node

    def type(self):
        token = self.current_token
        if token.type not in (INTEGER, CHAR, BOOLEAN):
            self.error()
        self.eat(token.type)
        return Type(token)

    def empty(self):
        return NoOp()

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error()
        return node
