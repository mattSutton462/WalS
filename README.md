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
* ID: matches any sequence of letters or underscores starting with a letter or underscore.

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
Wals > z = x + y
15
Wals > print(z)
15
```
**5. Boolean and Logic**
```
Wals > a = 5
5
Wals > b = 10
10
Wals > print preheat a == b oven
// print (a == b)
False

Wals > print preheat a != b oven
// print(a != b)
True
Wals > print preheat preheat a < b oven && preheat b==10 oven oven
//  print((a < b) && (b==10))
True
Wals > print preheat preheat a > b oven || preheat b == 10 oven oven 
// print((a > b) || (b == 10))
True
```
**6. Strings and Comments**
```
Wals > print preheat "Hello World" oven # This part is recognized as a comment!
// print("Hello World") # This part is recognized as a comment!
Hello World
```
**7. Arrays**
```
Wals > arr = [1,2,3]
[1, 2, 3]
```

