# WalS

## Set of tokens using regular expression:
* IDENTIFIER: matches any sequence of letters, digits, or underscores starting with a letter or underscore.
* INTEGER_LITERAL: matches any sequence of digits.
* FLOAT_LITERAL: matches any floating-point number.
* STRING_LITERAL: matches any sequence of characters enclosed in double-quotes.
* OPERATOR_PLUS / OPERATOR_MINUS: match the plus and minus operators, respectively.

## How Ply works with our programming language (WalS): 
- Ply generates a lexical analyzer based on the token definitions and regular expressions provided. The generated lexer can then be used to tokenize input text, producing a stream of tokens that can be processed further by a parser or other components of a compiler or interpreter.
