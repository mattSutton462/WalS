import json
import ply.lex as lex
import ply.yacc as yacc

# Token declaration
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN',
    'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE', # Comparison operators
    'AND', 'OR', 'NOT',                    # Logical operators
    'IF', 'ELSE', 'WHILE', 'FOR',          # Control flow keywords
    'INCREMENT', 'DECREMENT',              # Increment and decrement operators
    'PRINT',                               # Print keyword
    'ASSIGN',                              # Assignment operator
]

# Dictionary to store variables
variables = {}

# Global variable to store the AST
parsed_ast = {}

# Token regular expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_ASSIGN = r'='
t_PRINT = r'print' 

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignored characters
t_ignore = ' \t'

# Comment definition
def t_COMMENT(t):
    r'\#.*'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),  # Unary minus operator
    ('right', 'POWER'),
    ('nonassoc', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE'),  # Comparison operators
    ('left', 'AND'),  # Logical AND
    ('left', 'OR'),   # Logical OR
    ('right', 'NOT'),  # Logical NOT
)

def p_statement_empty(p):
    'statement : '
    pass

# Grammar rules
def p_statement_expr(p):
    '''statement : expression
                 | PRINT LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {"PRINT": p[3]}

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    p[0] = {p[2]: [p[1], p[3]]}

def p_expression_unary_minus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = {"UMINUS": p[2]}

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_assignment(p):
    'expression : ID ASSIGN expression'
    p[0] = {"ASSIGN": [p[1], p[3]]}

def p_expression_increment_decrement(p):
    '''expression : ID INCREMENT
                  | ID DECREMENT'''
    p[0] = {p[2]: p[1]}

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Shell text and user input
print("Start Cooking (type 'exit' to quit): ")
while True:
    text = input("Wals > ")
    if text.lower() == 'exit':
        break

    # Tokenize input
    lexer.input(text)

    # Parse input
    parsed_ast = parser.parse(text)
    
    # Serialize AST to JSON
    serialized_ast = json.dumps(parsed_ast)
    print("Serialized AST:", serialized_ast)