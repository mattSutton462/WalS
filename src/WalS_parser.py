from ply import yacc
from WalS_lexer import tokens

# Parser rules
def p_expression(p):
    '''
    expression : INT
               | FLOAT
               | expression ADD expression
               | expression SLICE expression
               | expression MIX expression
               | expression FOLD expression
               | PREHEAT expression OVEN
               | expression BAKE
               | WHISK ID BAKE
    '''
    if len(p) == 2:  # Single value
        p[0] = p[1]
    elif p[1] == 'preheat':
        p[0] = p[2]  # Ignore PREHEAT and OVEN tokens
    elif p[1] == 'whisk':
        p[0] = (p[1], p[2])  # Store whisked ingredient
    elif p[2] == 'bake':
        p[0] = ('bake', p[1])  # Bake action with ingredient
    else:
        if p[2] == 'add':
            p[0] = p[1] + p[3]
        elif p[2] == 'slice':
            p[0] = p[1] - p[3]
        elif p[2] == 'mix':
            p[0] = p[1] * p[3]
        elif p[2] == 'fold':
            p[0] = p[1] / p[3]


def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

