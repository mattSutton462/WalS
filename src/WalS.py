import re

# Define tokens
tokens = [
    ('INGREDIENT', r'\b(?:flour|sugar|butter|milk|eggs|salt|pepper|oil)\b'),
    ('ACTION', r'\b(?:mix|bake|boil|fry|saute|chop|slice)\b'),
    ('UTENSIL', r'\b(?:bowl|pan|pot|spoon|knife|whisk|oven)\b'),
    ('NUMBER', r'\d+'),
    ('UNIT', r'\b(?:cup|teaspoon|tablespoon)\b'),
    ('NEWLINE', r'\n'),
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
                if token != 'WHITESPACE' and token != 'NEWLINE':
                    tokens.append((token, value))
                text = text[match.end():]
                break
        if not match:
            raise ValueError('Illegal character: %s' % text)
    return tokens

# Test the lexer
text = """
1 cup flour
2 eggs
Mix ingredients
Preheat oven to 350°F
"""
tokens = lexer(text)
for token in tokens:
    print(token)
