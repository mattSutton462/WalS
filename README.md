# WalS

### Abstract:
* For all you aspiring coding cooks out there, this is the programming language for you! Our code defines tokens for various cooking-related actions and then processes that input text to parse and evaluate expressions. 

### Token Definitions:
* FLOAT: matches any floating-point number.
* INT: matches any sequence of digits.
* ADD: matches with the addition operator "+".
* SLICE: matches with the subtraction operator "-".
* MIX: matches with the multiplication operator "*".
* FOLD: matches with the division operator "/".
* PREHEAT: matches with left parenthesis "(".
* OVEN: matches with the right parenthesis ")".
* BAKE: matches with the newline character "\n".
* WHISK: declares a variable
* ID: matches any sequence of letters or underscores starting with a letter or underscore.
* WHITESPACE: matches with any whitespace.
* UNKNOWN: matches with any input that is not tokenized.

### Parser Definition Example:
* yacc.py uses a tuple ‘p’ containing the components of the matches rule:
* P[0] is reserved for the left side (expression), P[1] and onwards represents the right side (BOOLEAN)
** Grammar Rule for Booleans**
```
def p_expression_boolean(p):
    'expression : BOOLEAN'
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False
```

### Code Examples:
**1. Addition and Subtraction**
```
Wals > 3 add 5 slice 2
Wals > 6.0
// 3 + 5 - 2 = 6
```
**2. Multiplication and Division**
```
Wals > 10 mix 2 fold 5
Wals > 4.0
// 10 * 2 / 5 = 4
```
**3. Handling Decimal Numbers (Float)**
```
Wals > 2.5 mix 3.5 slice 3.25
Wals > 5.5
// 2.5 * 3.5 - 3.25 = 5.5
```
