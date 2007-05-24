
from aperiot.lexer import *

imports = []

useindents = False
usenewlines = False

# Terminal symbols

plus      = Operator('+', 'plus')
times     = Operator('*', 'times')
minus     = Operator('-', 'minus')
div       = Operator('/', 'div')
equal     = Operator('=', 'equal')
colon     = Operator(':', 'colon')
comma     = Operator(',', 'comma')
semicolon = Operator(';', 'semicolon')
absolute  = Operator('$', 'absolute')
lpar = Bracket('(', 'lpar')
rpar = Bracket(')', 'rpar')
label = Identifier
number = NumberLiteral


# Non-terminal symbols

TERM       = 'TERM'
ASSIGNMENT = 'ASSIGNMENT'
ARG        = 'ARG'
LIST       = 'LIST'
CELLREF    = 'CELLREF'
FUNCALL    = 'FUNCALL'
RANGE      = 'RANGE'
EXPR       = 'EXPR'
ARGLIST    = 'ARGLIST'
FACTOR     = 'FACTOR'


# Start symbol

start = 'LIST'

# Rules

rules = \
    {
        TERM: 
            [
                ([FACTOR], '$1'), 
                ([FACTOR, times, TERM], '(\'*\',$1,$3)'), 
                ([FACTOR, div, TERM], '(\'/\',$1,$3)'), 
            ],
        ASSIGNMENT: 
            [
                ([label, equal, EXPR], '($1,$3)'), 
            ],
        ARG: 
            [
                ([RANGE], '$1'), 
                ([EXPR], '$1'), 
                ([CELLREF], '$1'), 
            ],
        LIST: 
            [
                ([ASSIGNMENT], '[$1]'), 
                ([ASSIGNMENT, semicolon, LIST], '[$1]+$3'), 
                ([ASSIGNMENT, semicolon], '[$1]'), 
            ],
        CELLREF: 
            [
                ([absolute, label], '(\'cellref\',\'ABS\',$2.symbolic_name)'), 
                ([label, absolute, number], '(\'cellref\',$1.symbolic_name,\'ABS\',str(int($3)))'), 
                ([label], '(\'cellref\',$1.symbolic_name)'), 
                ([absolute, label, absolute, number], '(\'cellref\',\'ABS\',$2.symbolic_name,\'ABS\',str(int($4)))'), 
            ],
        FUNCALL: 
            [
                ([label, lpar, ARGLIST, rpar], '(\'funcall\',$1,$3)'), 
            ],
        RANGE: 
            [
                ([CELLREF, colon, CELLREF], '(\'range\',$1,$3)'), 
            ],
        EXPR: 
            [
                ([TERM], '$1'), 
                ([TERM, plus, EXPR], '(\'+\',$1,$3)'), 
                ([TERM, minus, EXPR], '(\'-\',$1,$3)'), 
            ],
        ARGLIST: 
            [
                ([ARG, comma, ARGLIST], '[$1]+$3'), 
                ([ARG], '[$1]'), 
            ],
        FACTOR: 
            [
                ([number], '$1.val()'), 
                ([CELLREF], '$1'), 
                ([lpar, EXPR, rpar], '(\'group\',$2)'), 
                ([FUNCALL], '$1'), 
                ([minus, FACTOR], '-$2'), 
            ],
    }

