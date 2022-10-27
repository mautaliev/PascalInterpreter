from token_class import Token

# типы токенов
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = '('
RPAREN = ')'
BEGIN = 'BEGIN'
END = 'END'
DOT = 'DOT'
ASSIGN = 'ASSIGN'
SEMI = 'SEMI'
ID = 'ID'

# токен конца входной строки
EOF = 'EOF'

# зарезервированные ключевые слова
RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', 'BEGIN'),
    'END': Token('END', 'END')
}
