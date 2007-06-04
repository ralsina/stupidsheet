import ply.lex as lex
from pprint import pprint

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'EQUAL',
   'COMMA',
   'RANGE',
   'ID', 
   'CELL',
   'SEMICOLON'
)

def t_RANGE(t):
    r'\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}:\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}'
    t.type='RANGE'
    return t
    
def t_CELL(t):
    r'\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}'
    t.type='CELL'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_EQUAL  = r'\='
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r'\,'
t_SEMICOLON   = r'\;'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    try:
         t.value = int(t.value)    
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno,t.value)
         t.value = 0
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
#lex.lex(debug=1)
lex.lex()

# Yacc example

import ply.yacc as yacc

def p_assignment(p):
    'assignment : CELL EQUAL expression'
    p[0] = [ '=',p[1],p[3]]

def p_funcall(p):
    'funcall : ID LPAREN arglist RPAREN'
    p[0] = [ 'funcall',p[1],p[3]]

def p_arglist(p):
    'arglist : arglist COMMA arglist'
    p[0] = p[1]+p[3]

def p_arglist_expression(p):
    'arglist : expression'
    p[0] = [p[1]]

def p_arglist_range(p):
    'arglist : RANGE'
    c1, c2=p[1].split(':')    
    p[0] = [['range', ['cell', c1], ['cell', c2]]]

def p_arglist_bool(p):
    'arglist : bool'
    p[0] = [p[1]]

def p_bool_equal(p):
    'bool : expression EQUAL expression'
    p[0] = ['==',p[1],p[3]]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = [ '+' , p[1],p[3]]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ['-', p[1] , p[3]]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ['*', p[1] , p[3]]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] =[ '/ ', p[1] , p[3]]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_funcall(p):
    'factor : funcall'
    p[0] = p[1]

def p_factor_cell(p):
    'factor : CELL'
    p[0] = ['cell', p[1]]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"
    print p

# Build the parser
yacc.yacc()

# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")

def parse(s):
    print 'Parsing: ', s
    return yacc.parse(s)
    
if __name__=="__main__":
        t='A1=SUM(A1:A7, C3:C9)'
        pprint (parse(t))
        print
        print
        t='A1=SUM(A1:A7)'
        pprint (parse(t))
        print
        print
        t='A1=SUM(AVG(A1:A7))*2'
        pprint (parse(t))
        print
        print
        t='A1=IF(A2=A1, 1, 0)'
        pprint (parse(t))
        print
        print
#        while 1:
#            lex.runmain()
