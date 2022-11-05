from token_class import Token

# типы токенов
INT = 'INT'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = '('
RPAREN = ')'
BEGIN = 'BEGIN'
END = 'END'
DOT = 'DOT' # .
ASSIGN = 'ASSIGN' # :=
SEMI = 'SEMI' # ;
COLON = 'COLON' # :
ID = 'ID'
VAR = 'VAR'
INTEGER = 'INTEGER_TYPE'
CHAR = 'CHAR_TYPE'
BOOLEAN = 'BOOLEAN_TYPE'
WRITELN = 'WRITELN'
CASE = 'CASE'
OF = 'OF'
TEXT_CONSTANT = 'TEXT_CONSTANT'
OR = 'OR'
AND = 'AND'
SHL = 'SHL'
SHR = 'SHR'

# токен конца входной строки
EOF = 'EOF'

# зарезервированные ключевые слова
RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END'),
    'PROGRAM': Token('PROGRAM', 'PROGRAM'),
    'VAR': Token('VAR', 'VAR'),
    'DIV': Token('DIV', 'DIV'),
    'INTEGER': Token('INTEGER_TYPE', 'INTEGER'),
    'CHAR': Token('CHAR_TYPE', 'CHAR'),
    'BOOLEAN': Token('BOOLEAN_TYPE', 'BOOLEAN'),
    'WRITELN': Token('WRITELN', 'WRITELN'),
    'CASE': Token('CASE', 'CASE'),
    'OF': Token('OF', 'OF'),
    'OR': Token('OR', 'OR'),
    'AND': Token('AND', 'AND'),
    'SHL': Token('SHL', 'SHL'),
    'SHR': Token('SHR', 'SHR')
}

# цифры
POSSIBLE_DIGITS = ('0', '1')
