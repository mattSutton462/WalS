import re

# Token Definition
tokens = [
    # Personalized Cooking Tokens
    # ('QTY', r'\d+'),
    # ('ID', r'[a-zA-Z_]\w*'),
    # ('ADD', r'\+'),
    # ('SLICE', r'-'),
    # ('MIX', r'\*'),
    # ('FOLD', r'/'),
    # ('PREHEAT', r'\('),
    # ('OVEN', r'\)+'),
    # ('BAKE', r'\n'),
    # ('WHITESPACE', r'\s+'),
    # ('UNKNOWN', r'.'),

    # Cooking Term Defined Tokens
    ('QTY', r'\d+'),
    ('+', r'add|Add|ADD'),
    ('-', r'slice|Slice|SLICE'),
    ('*', r'mix|,Mix|MIX'),
    ('/', r'fold|Fold|FOLD'),
    ('(', r'preheat|Preheat|PREHEAT'),
    (')', r'oven|Oven|OVEN'),
    ('\n', r'bake|Bake|BAKE'),
    ('ID', r'[a-zA-Z_]\w*'),
    ('WHITESPACE', r'\s+'),
    ('UNKNOWN', r'.'),
]

# Compile regular expressions for tokens
patterns = [(token, re.compile(pattern)) for token, pattern in tokens]

def lexer(text):
    tokens = []
    while text:
        match = None
        for token, pattern in patterns:
            match = pattern.match(text)
            if match:
                value = match.group(0)
                if token != 'WHITESPACE' and token != 'NEWLINE' and token != 'BAKE':
                    tokens.append((token, value))
                text = text[match.end():]
                break
        if not match:
            raise ValueError('Illegal character: %s' % text)
    return tokens

# Testing the lexer using shell's standard input
if __name__ == "__main__":
    text = input("Enter your cooking instructions:\n")
    tokens = lexer(text)
    for token in tokens:
        print(token)

# Example prompt for Lexer
# 3 mix Preheat 5 slice 3 Oven BAKE
# 3*(5-3) 

