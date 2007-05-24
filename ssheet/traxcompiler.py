from pprint import pprint
from aperiot.parsergen import build_parser
import aperiot
import cellutils
import sys

dependencies=set()

def addOp(*args):
        return '+'.join([compile_token(a) for a in args])
def mulOp(*args):
        return '*'.join([compile_token(a) for a in args])
def subOp(*args):
        return '-'.join([compile_token(a) for a in args])
def divOp(*args):
        return '/'.join([compile_token(a) for a in args])

def groupOp(*args):
        return '(%s)'%compile_token(args[0])

def funcOp(*args):
        return '%s(%s)'%(args[0].symbolic_name,
                         ','.join([compile_token(a) for a in args[1]]))

def rangeOp(*args):
        c1=compile_token(args[0])
        c2=compile_token(args[1])
        return ','.join([compile_token(a) for a in cellutils.cellrange(c1,c2)])
def cellOp(*args):
        #FIXME this is simplistic for testing
        return compile_token(aperiot.lexer.Identifier(''.join(args).replace('ABS','')))

operators={'+':addOp,
           '-':subOp,
           '*':mulOp,
           '/':divOp,
           'group':groupOp,
           'funcall':funcOp,
           'range':rangeOp,
           'cellref':cellOp
           }


def compile_token(token):
        if isinstance (token,aperiot.lexer.Identifier):
                v=token.symbolic_name.lower()
                dependencies.add(v)
                return v
        if isinstance(token,list) or isinstance(token,tuple):
            return apply(operators[token[0]],token[1:])
        return str(token)

def compile_assignment(tokens):
        target=tokens[0].symbolic_name
        compiled=compile_token(tokens[1])
        return target,compiled


def compile(source):
    global dependencies
    compiled={}
    myparser = build_parser('traxter')
    assign_list=myparser.parse(source)
    for assignment in assign_list:
            dependencies=set()
            var,c=compile_assignment(assignment)
            compiled[var]=[c,dependencies]
            
    
    return compiled

if __name__=="__main__":

        t='A1=$A$1'
        pprint (compile(t))
        print
        print
        t='A1=SUM(A1:A7)*2;A3=2+2;'
        pprint (compile(t))


