from ply import lex

# Define tokens
tokens = (
    'IDENTIFIER',
    'INTEGER_LITERAL',
    'FLOAT_LITERAL',
    'STRING_LITERAL',
    'OPERATOR_PLUS',
    'OPERATOR_MINUS'
)

# Define regular expressions for tokens
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEGER_LITERAL = r'[0-9]+'
t_FLOAT_LITERAL = r'[0-9]+\.[0-9]+'
t_STRING_LITERAL = r'"[^"]*"'
t_OPERATOR_PLUS = r'\+'
t_OPERATOR_MINUS = r'-'

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
lexer.input('x = 42 + 3.14')
for token in lexer:
    print(token)