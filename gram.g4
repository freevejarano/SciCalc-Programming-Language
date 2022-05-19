grammar gram;

prog:   stat+ ;

stat:   adv NEWLINE                                 
    |   ID "=" arg NEWLINE
    |   em NEWLINE
    ;

adv:    arg
    |   IF "(" argv "):" stat ELSE ":" stat         # If
    |   FOR ID "in" ID ":" adv                      # For
    |   WHILE "(" argv "):" adv                     # While
    |   DEF ID "( ID* ):" adv                       # Def
    ;

argv:   arg "==" arg
    |   arg ">" arg
    |   arg "<" arg
    |   arg "!=" arg
    |   arg "<=" arg
    |   arg ">=" arg
    |   ID
    ;

arg:    "(" arg ")"
    |   conc
    |   opr
    |   em
    |   '[' em+ ']'
    ;

conc:   opr MUL opr                                 # Mul
    |   opr DIV opr                                 # Div
    |   opr ADD opr                                 # Add
    |   opr SUB opr                                 # Sub
    ;

opr:  'mod(' arg ')'                                # Mod
    |  'sqrt(' arg ',' arg ')'                      # Sqrt
    |  'pow(' arg ',' arg ')'                       # Pow
    |  'sin(' arg ')'                               # Sin
    |  'cos(' arg ')'                               # Cos
    |  'tan(' arg ')'                               # Tan
    |  'arcsin(' arg ')'                            # Arcsin
    |  'arccos(' arg ')'                            # Arccos
    |  'arctan(' arg ')'                            # Arctan
    |  'log(' arg ',' arg ')'                       # Log
    |  'factorial(' arg ')'                         # Factorial
    |  'euler(' arg ')'                             # Euler
    |  'rad(' arg ')'                               # Rad
    |  'deg(' arg ')'                               # Deg
    |   em
    ; 

em: PI                                              # Pi
    |   ID
    |   INT
    |   BOOL
    ;   

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
PI :   'PI' ;
FOR : 'for' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
DEF : 'def' ;
BOOL : 'True' | 'False' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
NEWLINE :'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
