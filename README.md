# WalS

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
* ID: matches any sequence of letters or underscores starting with a letter or underscore.
* WHITESPACE: matches with any whitespace.
* UNKNOWN: matches with any input that is not tokenized.

### Code Examples:
**1. Addition and Subtraction**
```
3 add 3 slice 2
12.0
```
**2. Multiplication and Division**
```
10 mix 2 fold 5
4.0
```
**3. Handling Decimal Numbers (Float)**
```
2.5 mix 3.5 slice 3 
5.75
```
