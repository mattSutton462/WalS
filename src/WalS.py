import ply.lex as lex
import ply.yacc as yacc

# Token Declaration
tokens = [
    'FLOAT', 'INT', 'ADD', 'SUB', 'MUL', 'DIV', 'EXP',  # Arithmetic operators
    'LPAREN', 'RPAREN',                                 # Parentheses
    'ID', 'INCREMENT', 'DECREMENT',                     # Variables, incrementors, decrementors
    'BOOLEAN', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE',   # Booleans and comparison operators
]

# Token regular expressions
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_EXP = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='

# Regular expressions for tokens
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'  # Change type to ID for identifiers
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

# Ignored characters
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('right', 'EXP'),
    ('right', 'UMINUS'),  # Unary minus operator
)

# Grammar rules
def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression EXP expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '**':
        p[0] = p[1] ** p[3]

def p_expression_unary_minus(p):
    'expression : SUB expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : INT
                  | FLOAT'''
    p[0] = p[1]

def p_expression_var(p):
    'expression : ID'
    # You would handle variable lookup and assignment here
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : BOOLEAN'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def evaluate_expression(text):
    result = parser.parse(text)
    return result if result is not None else 0

# Shell text and user input
print("Start Cooking (type 'exit' to quit): ")
while True:
    text = input("WalS > ")
    if text.lower() == 'exit':
        break

    # Tokenize input
    lexer.input(text)
    
    # # Print all tokens
    # for token in lexer:
    #     print(token)

    # Evaluate and print result
    result = evaluate_expression(text)
    print(result)