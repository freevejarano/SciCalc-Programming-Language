grammar gram;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   expr '%' expr               # Mod
    |   'sqrt(' expr ',' expr ')'   # Sqrt
    |   expr '**' expr              # Pow
    |   'sin(' expr ')'             # Sin
    |   'cos(' expr ')'             # Cos
    |   'tan(' expr ')'             # Tan
    |   'arcsin(' expr ')'          # Arcsin
    |   'arccos(' expr ')'          # Arccos
    |   'arctan(' expr ')'          # Arctan
    |   'log(' expr ',' expr ')'    # Log
    |   'factorial(' expr ')'       # Factorial
    |   'euler(' expr ')'           # Euler
    |   'rad(' expr ')'             # Rad
    |   'deg(' expr ')'             # Deg
    |   'pi'                        # Pi
    |   NUM                         # num
    |   ID                          # id
    |   '[' arreglo+ ']'            # array
    |   '(' expr ')'                # parens
    ;

arreglo: NUM+ ','*
    ;

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
NUM :   [0-9]+'.'?[0-9]* ;         // match integers
NEWLINE:    '\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace