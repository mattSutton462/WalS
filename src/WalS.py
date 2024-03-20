import re

# Token Declaration
tokens = [
('FLOAT', r'\d+\.\d+'),                     # Floating Point Numbers
('INT', r'\d+'),                            # Integer Numbers
('ADD', r'add|Add|ADD'),                    # Addition
('SLICE', r'slice|Slice|SLICE'),            # Subtraction
('MIX', r'mix|Mix|MIX'),                    # Multiplication
('FOLD', r'fold|Fold|FOLD'),                # Division
('PREHEAT', r'preheat|Preheat|PREHEAT'),    # Left Paren
('OVEN', r'oven|Oven|OVEN'),                # Right Paren
('BAKE', r'bake|Bake|BAKE'),                # Newline
('WHISK', r'whisk|Whisk|WHISK'),            # Declare a value
('ID', r'[a-zA-Z_]\w*'),                    # String
('WHITESPACE', r'\s+'),                     # Whitespace
('UNKNOWN', r'.'),                          # NOT LISTED
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
                if token != 'WHITESPACE' and token != 'UNKNOWN':
                    tokens.append((token, value))
                text = text[match.end():]
                break
        if not match:
            raise ValueError('Illegal character: %s' % text)
    return tokens

def evaluate_expression(tokens):
    # Initialize variables to store the result and the current operation
    result = None
    current_op = None
    
    for token_type, token_value in tokens:
        if token_type in ['INT', 'FLOAT']:
            num = float(token_value)
            if result is None:
                result = num
            elif current_op.upper() == 'MIX':
                result *= num
            elif current_op.upper() == 'FOLD':
                result /= num
            elif current_op.upper() == 'ADD':
                result += num
            elif current_op.upper() == 'SLICE':
                result -= num
        elif token_type == 'BAKE':
            print("\n")
        elif token_type in ['ADD', 'SLICE', 'MIX', 'FOLD']:
            current_op = token_value
    
    return result if result is not None else 0

# Shell text and user input
text = print("Start Cooking (type 'exit' to quit): ")
while True:
    text = input("WalS > ")
    if text.lower() == 'exit':
        break 

    tokens = lexer(text)
    result = evaluate_expression(tokens)
    if result == 0:
        print("", end='')
    else:
        print(result)

    # Displays Tokens
    # 2 mix 2.5 slice 3
    for token in tokens:
        print(token)
