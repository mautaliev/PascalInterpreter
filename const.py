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
    'BEGIN'.lower(): Token('BEGIN', 'BEGIN'),
    'END'.lower(): Token('END', 'END'),
    'PROGRAM'.lower(): Token('PROGRAM', 'PROGRAM'),
    'VAR'.lower(): Token('VAR', 'VAR'),
    'DIV'.lower(): Token('DIV', 'DIV'),
    'INTEGER'.lower(): Token('INTEGER_TYPE', 'INTEGER'),
    'CHAR'.lower(): Token('CHAR_TYPE', 'CHAR'),
    'BOOLEAN'.lower(): Token('BOOLEAN_TYPE', 'BOOLEAN'),
    'WRITELN'.lower(): Token('WRITELN', 'WRITELN'),
    'CASE'.lower(): Token('CASE', 'CASE'),
    'OF'.lower(): Token('OF', 'OF'),
    'OR'.lower(): Token('OR', 'OR'),
    'AND'.lower(): Token('AND', 'AND'),
    'SHL'.lower(): Token('SHL', 'SHL'),
    'SHR'.lower(): Token('SHR', 'SHR')
}

# цифры
POSSIBLE_DIGITS = ('0', '1')

# запросы
SEARCH_HISTORY = """
    SELECT
        "requestcode"
    FROM
        "history"
    ORDER BY "requestid" DESC
    LIMIT 10
"""
INSERT_HISTORY_OBJECT = """
    INSERT INTO history(requestcode) VALUES ('{}'::text)
"""
