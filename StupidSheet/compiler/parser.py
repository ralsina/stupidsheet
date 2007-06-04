import ply.lex as lex
import ply.yacc as yacc
from pprint import pprint
import re


#########################
#
# LEX
#
#########################

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
   'STRING', 
   'SEMICOLON',
   'LT',
   'GT'
)

def t_RANGE(t):
    r'\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}:\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}'
    t.type='RANGE'
    return t

def t_CELL(t):
    r'\${0,1}[a-zA-Z]{1,2}\${0,1}[0-9]{1,5}'
    t.type='CELL'
    return t

def parse_cell(c):
    r=re.compile(r'(\${0,1}[a-zA-Z]{1,2})(\${0,1}[0-9]{1,5})')
    _, col, row, _=r.split(c)
    if col[0]=='$':
        col=['abscol', col[1:]]
    else:
        col=['relcol', col]
    if row[0]=='$':
        row=['absrow', row[1:]]
    else:
        row=['relrow', row]
    return ['cell', col, row]
    
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_EQUAL   = r'\='
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r'\,'
t_SEMICOLON   = r'\;'
t_STRING  = r'\"[^"]*\"'
t_LT      = r'\<'
t_GT      = r'\>'

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

#########################
#
# YACC
#
#########################


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
    p[0] = ['range', parse_cell(c1),parse_cell(c2)]

def p_arglist_bool(p):
    'arglist : bool'
    p[0] = [p[1]]

def p_bool_equal(p):
    'bool : expression EQUAL expression'
    p[0] = ['bool','==',p[1],p[3]]
def p_bool_lt(p):
    'bool : expression LT expression'
    p[0] = ['bool','<',p[1],p[3]]
def p_bool_gt(p):
    'bool : expression GT expression'
    p[0] = ['bool','>',p[1],p[3]]
def p_bool_le(p):
    'bool : expression LT EQUAL expression'
    p[0] = ['bool','<=',p[1],p[3]]
def p_bool_ge(p):
    'bool : expression GT EQUAL expression'
    p[0] = ['bool','>=',p[1],p[3]]
def p_bool_ne(p):
    'bool : expression LT GT expression'
    p[0] = ['bool','<>',p[1],p[3]]

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

def p_factor_str(p):
    'factor : STRING'
    p[0] = ['string', p[1]]

def p_factor_funcall(p):
    'factor : funcall'
    p[0] = p[1]

    

def p_factor_cell(p):
    'factor : CELL'
    p[0] = parse_cell(p[1])

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
