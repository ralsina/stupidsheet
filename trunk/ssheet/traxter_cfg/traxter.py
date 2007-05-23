
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
lpar = Bracket('(', 'lpar')
rpar = Bracket(')', 'rpar')
label = Identifier
number = NumberLiteral


# Non-terminal symbols

TERM       = 'TERM'
ASSIGNMENT = 'ASSIGNMENT'
ARG        = 'ARG'
LIST       = 'LIST'
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
                ([label], '$1'), 
            ],
        LIST: 
            [
                ([ASSIGNMENT], '[$1]'), 
                ([ASSIGNMENT, semicolon, LIST], '[$1]+$3'), 
                ([ASSIGNMENT, semicolon], '[$1]'), 
            ],
        FUNCALL: 
            [
                ([label, lpar, ARGLIST, rpar], '(\'funcall\',$1,$3)'), 
            ],
        RANGE: 
            [
                ([label, colon, label], '(\'range\',$1,$3)'), 
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
                ([lpar, EXPR, rpar], '(\'group\',$2)'), 
                ([FUNCALL], '$1'), 
                ([label], '$1'), 
                ([minus, FACTOR], '-$2'), 
            ],
    }

