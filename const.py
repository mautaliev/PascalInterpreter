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
    'WRITELN': Token('WRITELN', 'WRITELN')
}
