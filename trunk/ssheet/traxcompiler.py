from pprint import pprint
from aperiot.parsergen import build_parser
import aperiot
from cellutils import *
import sys

dependencies=set()
currentKey=None

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
        return '%s(%s)'%(args[0],
                         ','.join([compile_token(a) for a in args[1]]))

def rangeOp(*args):
        c1=compile_token(args[0])
        c2=compile_token(args[1])
        return ','.join([compile_token(a) for a in cellrange(c1,c2)])
def cellOp(*args):
        return ''.join([compile_token(a) for a in args])
def elemOp(*args):
        return str(args[0])


operators={'+':addOp,
           '-':subOp,
           '*':mulOp,
           '/':divOp,
           'group':groupOp,
           'funcall':funcOp,
           'range':rangeOp,
           'cell':cellOp,
           'relcol':elemOp,
           'abscol':elemOp,
           'relrow':elemOp,
           'absrow':elemOp
           }

def compile_token(token):
        if isinstance (token,aperiot.lexer.Identifier):
                v=token.symbolic_name.lower()
                dependencies.add(v)
                return v
        if isinstance(token,list):
            return apply(operators[token[0]],token[1:])
        return str(token)

def compile_assignment(tokens):
        global currentKey
        currentKey=tokens[0].symbolic_name
        compiled=compile_token(tokens[1])
        return currentKey,compiled

def traxcompile(source):
    global dependencies
    compiled={}
    traxparser = build_parser('traxter')
    assign_list=traxparser.parse(source)
    for assignment in assign_list:
            pprint(assignment)
            dependencies=set()
            var,c=compile_assignment(assignment)
            compiled[var]=[c,dependencies]
    return compiled

def traverse_tree(tokens,func,extra_args):
        '''applies func to all tokens in a tree'''
        for token in tokens:
                apply(func,[token]+list(extra_args))
                if type(token)==list:
                        traverse_tree(token,func,extra_args)


if __name__=="__main__":

        t='A1=SUM(A1:A7);'
        pprint (traxcompile(t))
        print
        print
        t='A1=SUM(AVG(A1:A7))*2;'
        pprint (traxcompile(t))
        print
        print
        t='A1=$A1+A$1+$A$1+A1;'
        pprint (traxcompile(t))



