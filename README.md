# WalS

### Abstract:
* For all you aspiring coding cooks out there, this is the programming language for you! Our code defines tokens for various cooking-related actions and then processes that input text to parse and evaluate expressions. 

### Token Definitions:
* ID: matches any sequence of letters or underscores starting with a letter or underscore.
* NUMBER matches with any number
* STRING: matches with any string definition
* ARRAY: matches with any array declaration 
* ADD: replacement for the addition operator "+"
* SLICE: replacement for the subtraction operator "-"
* MIX: replacement for the multiplication operator "mix"
* FOLD: replacement for the division operator "fold"
* PREHEAT: replacement for left parenthesis "preheat"
* OVEN: replacement for right parenthesis "oven"
* BAKE: replacement for statement "PRINT"
* EQ: matches with "==" 
* NEQ: matches with "!=" 
* LT: matches with "<" 
* LTE: matches with "<=" 
* GT: matches with ">" 
* GTE: matches with ">=" 
* AND: matches with "&&" 
* OR: matches with "||"  
* NOT: matches with "!"
* IF: matches with "if"
* ELSE: matches with "else"
* THEN: matches with "then"
* WHILE: matches with "while"
* FOR: matches with "for"
* DO: matches with "do"
* TO: matches with "to"
* INCREMENT: matches with "++" 
* DECREMENT: matches with "--"
* ASSIGN: matches with "ASSIGN"
* BOOLEAN: matches with "true|false" 

### Parser Definition Example:
* yacc.py uses a tuple ‘p’ containing the components of the matches rule:
* P[0] is reserved for the left side (expression), P[1] and onwards represents the right side (BOOLEAN)
  
**Grammar Rule for Booleans**
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
**3. Increment and Decrement**
```
Wals > x = 10
10
Wals > x++
11
Wals > x--
10
```
**4. Variable Handling**
```
Wals > x = 5
5
Wals > y = 10
10
Wals > z = x add y
15
Wals > bake preheat z oven
// print(z)
15
```
**5. Boolean and Logic**
```
Wals > a = 5
5
Wals > b = 10
10
Wals > bake preheat a == b oven
// print (a == b)
False

Wals > bake preheat a != b oven
// print(a != b)
True
Wals > bake preheat preheat a < b oven && preheat b==10 oven oven
//  print((a < b) && (b==10))
True
Wals > bake preheat preheat a > b oven || preheat b == 10 oven oven 
// print((a > b) || (b == 10))
True
```
**6. Strings and Comments**
```
Wals > bake preheat "Hello World" oven # This part is recognized as a comment!
// print("Hello World") # This part is recognized as a comment!
Hello World
```
**7. Arrays**
```
Wals > arr = [1,2,3]
[1, 2, 3]
```

