from ply import lex

# Token Declaration
tokens = [
    'FLOAT', 'INT', 'ADD', 'SLICE', 'MIX', 'FOLD', 'PREHEAT', 'OVEN',
    'BAKE', 'WHISK', 'ID', 'WHITESPACE', 'UNKNOWN'
]

# Regular expression rules for tokens
t_FLOAT = r'\d+\.\d+'
t_INT = r'\d+'
t_ADD = r'add|Add|ADD'
t_SLICE = r'slice|Slice|SLICE'
t_MIX = r'mix|Mix|MIX'
t_FOLD = r'fold|Fold|FOLD'
t_PREHEAT = r'preheat|Preheat|PREHEAT'
t_OVEN = r'oven|Oven|OVEN'
t_BAKE = r'bake|Bake|BAKE'
t_WHISK = r'whisk|Whisk|WHISK'
t_ID = r'[a-zA-Z_]\w*'
t_WHITESPACE = r'\s+'
t_UNKNOWN = r'.'

# Ignored characters (whitespace)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
