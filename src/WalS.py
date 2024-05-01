import ply.lex as lex
import ply.yacc as yacc

# Token declaration
tokens = [
    'ID', 'NUMBER', 'BOOLEAN', 'STRING', 'ARRAY',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN',
    'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE', # Comparison operators
    'AND', 'OR', 'NOT',                    # Logical operators
    'IF', 'THEN', 'ELSE', 'WHILE', 'FOR',  # Control flow keywords
    'INCREMENT', 'DECREMENT',              # Increment and decrement operators
    'PRINT',                               # Print keyword
    'ASSIGN',                              # Assignment operator
    'DO', 'TO'                             # Other for loop keywords        
]

# Dictionary to store variables
variables = {}

# Token regular expressions
t_PLUS = r'add'
t_MINUS = r'slice'
t_TIMES = r'mix'
t_DIVIDE = r'fold'
t_POWER = r'\*\*'
t_LPAREN = r'preheat'
t_RPAREN = r'oven'
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
t_THEN = r'then'
t_WHILE = r'while'
t_FOR = r'for'
t_DO = r'do'
t_TO = r'to'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_ASSIGN = r'='
t_PRINT = r'print' 
t_BOOLEAN = r'true|false'

# String literal definition
def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Array literal definition
def t_ARRAY(t):
    r'\[(?:\s*([a-zA-Z_][a-zA-Z_0-9]*|\d+)\s*(?:,\s*([a-zA-Z_][a-zA-Z_0-9]*|\d+)\s*)*)?\]'
    # Matches comma-separated list of IDs or numbers within square brackets
    t.value = [eval(x) if x.isdigit() else x for x in t.value[1:-1].split(',')]  # Convert numbers to integers
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'print':                          # Recognize print as PRINT token type
        t.type = 'PRINT'
    elif t.value == 'true' or t.value == 'false':   # Recognize true|false as BOOLEAN token type
        t.type = 'BOOLEAN'
    elif t.value == 'add':
        t.type = 'PLUS'
    elif t.value == 'slice':
        t.type = 'MINUS'
    elif t.value == 'mix':
        t.type = 'TIMES'
    elif t.value == 'fold':
        t.type = 'DIVIDE'
    elif t.value == 'preheat':
        t.type = "LPAREN"
    elif t.value == 'oven':
        t.type = "RPAREN"
    elif t.value == 'if':
        t.type = "IF"
    elif t.value == 'then':
        t.type = "THEN"
    elif t.value == 'else':
        t.type = "ELSE"
    elif t.value == 'while':
        t.type = "WHILE"
    elif t.value == 'for':
        t.type = "FOR"
    elif t.value == 'to':
        t.type = "TO"
    elif t.value == 'do':
        t.type = "DO"
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
    ('nonassoc', 'IF', 'ELSE'),  # Handle the dangling-else problem
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE'),  # Comparison operators should not chain
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),  # Unary minus operator
    ('right', 'POWER'),   # Right associative for exponentiation
    ('right', 'NOT')      # Logical NOT
)



def p_statement_empty(p):
    'statement : '
    pass

# Grammar rules
def p_statement_expr(p):
    '''statement : expression
                 | PRINT LPAREN expression RPAREN'''
    if len(p) == 2:  # If there's only one expression
        print(p[1])
    else:            # If there's a print statement with an expression
        print(p[3])

def p_statement_if(p):
    'statement : IF expression THEN statement opt_else'
    if p[2]:
        parser.parse(p[4])
    elif len(p) > 5 and p[5] is not None:
        parser.parse(p[5])


def p_opt_else(p):
    '''opt_else : ELSE statement
                | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None


def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression AND expression
                  | expression OR expression
                  | NUMBER
                  | ID
                  | ID INCREMENT
                  | ID DECREMENT'''
    if len(p) == 4:  # If there's a binary operation
        if p[2] == 'add':
            p[0] = p[1] + p[3]
        elif p[2] == 'slice':
            p[0] = p[1] - p[3]
        elif p[2] == 'mix':
            p[0] = p[1] * p[3]
        elif p[2] == 'fold':
            p[0] = p[1] / p[3]
        elif p[2] == 'power':
            p[0] = p[1] ** p[3]
        elif p[2] == '&&':
            p[0] = p[1] and p[3]
        elif p[2] == '||':
            p[0] = p[1] or p[3]
    if len(p) == 2:  # If it's a single expression (NUMBER or ID)
        if isinstance(p[1], int):  # If it's a number
            p[0] = p[1]
        elif p[1] in variables:  # If it's an ID (variable)
            p[0] = variables[p[1]]
    elif len(p) == 3:  # If it's an increment or decrement operation
        if p[2] == '++':
            if p[1] in variables:
                variables[p[1]] += 1
                p[0] = variables[p[1]]
            else:
                print(f"Variable '{p[1]}' not found!")
        elif p[2] == '--':
            if p[1] in variables:
                variables[p[1]] -= 1
                p[0] = variables[p[1]]
            else:
                print(f"Variable '{p[1]}' not found!")

def p_expression_relational(p):
    '''expression : expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LTE expression
                  | expression GT expression
                  | expression GTE expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]


def p_expression_unary_minus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_array(p):
    'expression : ARRAY'
    p[0] = p[1]

def p_expression_boolean(p):
    'expression : BOOLEAN'
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = not p[2]

def p_expression_assignment(p):
    'expression : ID ASSIGN expression'
    variables[p[1]] = p[3]  # Assign value to variable
    p[0] = p[3]             # Return the assigned value

def p_statement_while(p):
    'statement : WHILE expression DO statement'
    while p[2]:  # Evaluate the loop condition
        parser.parse(p[4])  # Parse and execute the loop body
        if not eval(p[2], {}, variables):  # Re-evaluate the condition with current variable states
            break

def p_statement_for(p):
    'statement : FOR ID ASSIGN expression TO expression DO statement'
    # Extract loop parameters
    var_name = p[2]
    start_value = p[4]
    end_value = p[6] + 1  # Assuming inclusive range, hence end_value + 1 for Python range handling
    # Execute the loop
    for variables[var_name] in range(start_value, end_value):
        # Evaluate the loop condition
        if variables[var_name] >= end_value:
            break
        p[8]  # Execute the loop body
        parser.parse(p[8])  # This is to re-parse the statement body for every iteration


# Error Handler for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
# parser = yacc.yacc()

parser = yacc.yacc(write_tables=False)

# Shell text and user input
print("Start Cooking (type 'exit' to quit): ")
while True:
    text = input("Wals > ")
    if text.lower() == 'exit':
        break

    # Tokenize input
    lexer.input(text)

    # # Print all tokens
    for token in lexer:
        print(token)

    # Evaluate and print result
    parser.parse(text)