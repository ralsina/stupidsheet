from pprint import pprint
import sys,os,pickle
import parser
from traxcompiler import traverse_tree
from StupidSheet.backend.cellutils import *

def addOp(*args):
        return '+'.join([decompile_token(a) for a in args])
def mulOp(*args):
        return '*'.join([decompile_token(a) for a in args])
def subOp(*args):
        return '-'.join([decompile_token(a) for a in args])
def divOp(*args):
        return '/'.join([decompile_token(a) for a in args])

def groupOp(*args):
        return '(%s)'%decompile_token(args[0])

def funcOp(*args):
        return '%s(%s)'%(args[0].upper(),
                         ','.join([decompile_token(a) for a in args[1]]))

def rangeOp(*args):
        c1=decompile_token(args[0])
        c2=decompile_token(args[1])
        return '%s:%s'%(c1,c2)
def cellOp(*args):
        return ''.join([decompile_token(a) for a in args])
def absOp(*args):
        return '$'+str(args[0])
def relOp(*args):
        return str(args[0])

def stringOp(*args):
    return r'%s'%args[0]


def decompile_token(token):
        if isinstance(token,list):
            return apply(operators[token[0]],token[1:])
        return str(token)

operators={'+':addOp,
           '-':subOp,
           '*':mulOp,
           '/':divOp,
           'group':groupOp,
           'funcall':funcOp,
           'range':rangeOp,
           'cell':cellOp,
           'relcol':relOp,
           'abscol':absOp,
           'relrow':relOp,
           'absrow':absOp, 
           'string':stringOp
           }

def regurgitate(assignment):
        '''Takes a single assignment and returns traxter code'''
        var=assignment[1]
        code=decompile_token(assignment[2])
        return '%s=%s'%(var,code)


def displace_cell(token,dx,dy):
        if type(token)==list and token[0]=='cell':
            if token[1][0]=='relcol':
                x,y=keyCoord(token[1][1]+'1')
                k=coordKey(x+dx,1)
                c,r=splitcell(k)
                token[1][1]=c
            if token[2][0]=='relrow':
                x,y=keyCoord('A'+str(token[2][1]))
                k=coordKey(1,y+dy)
                c,r=splitcell(k)
                token[2][1]=r

# FIXME make it less incredibly awful
def displace_source(source,key_from,key_to):
        x1,y1=keyCoord(key_from)
        x2,y2=keyCoord(key_to)
        dx=x2-x1
        dy=y2-y1

        # Traverse formula applying displace_cell
        tree=parser.parse(source)
        traverse_tree([tree[2]],displace_cell,[dx,dy])
        ax,ay=keyCoord(tree[1])
        tree[1]=coordKey(ax+dx,ay+dy)
        return regurgitate(tree)

if __name__=="__main__":
        from aperiot.parsergen import build_parser
        #t='A1=SUM(A1:A7);A1=SUM(AVG(A1:A7))*2;A1=$A1+A$1+$A$1+A1;'
        #pprint (regurgitate(traxparser.parse(t)))
        t='A1=A9'
        pprint (regurgitate(displace_source(t,'A1','B2')))
