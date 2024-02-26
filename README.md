# WalS

## Token Definitions:
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

## WalS Lexical Analyser: 
- We decided to use a manually implemented lexical analyzer (lexer) for our programming language, where the lexer function takes a string of input text and breaks it down into tokens based on predefined patterns. Our lexer follows a manual approach to tokenization, where we explicitly define the token types and their corresponding patterns. This approach gives us complete control over the tokenization process and allows for ease of customization. Each token consists of a token type (INT, FLOAT, ADD, etc.) and its corresponding value in the input text. 
