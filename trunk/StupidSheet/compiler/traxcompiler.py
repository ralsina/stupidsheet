from pprint import pprint
import parser
from StupidSheet.backend.cellutils import *
import pickle
import sys,os

def addOp(self,*args):
        return '+'.join([self.compile_token(a) for a in args])
def mulOp(self,*args):
        return '*'.join([self.compile_token(a) for a in args])
def subOp(self,*args):
        return '-'.join([self.compile_token(a) for a in args])
def divOp(self,*args):
        return '/'.join([self.compile_token(a) for a in args])
def groupOp(self,*args):
        return '(%s)'%self.compile_token(args[0])
def funcOp(self,*args):
        return '%s(%s)'%(args[0].upper(),
                         ','.join([self.compile_token(a) for a in args[1]]))

def rangeOp(self,*args):
        c1=self.compile_token(args[0])
        c2=self.compile_token(args[1])
        return ','.join([self.compile_token(a) for a in cellrange(c1,c2)])
def cellOp(self,*args):
        name=''.join([self.compile_token(a) for a in args]).lower()
        self.dependencies.add(name)
        return name
def elemOp(self,*args):
        return str(args[0])

def stringOp(self, *args):
    return r'"""%s"""'%args[0].string

def eqOp(self, *args):
    return '%s==%s'%(self.compile_token(args[0]),self.compile_token(args[1])) 

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
           'absrow':elemOp, 
           'string':stringOp, 
           '==':eqOp
           }


def traverse_tree(tokens,func,extra_args):
        '''applies func to all tokens in a tree'''
        print 'traverse: ', tokens
        for token in tokens:
                apply(func,[token]+list(extra_args))
                if type(token)==list:
                        traverse_tree(token,func,extra_args)

class Compiler:
        def compile(self,source):
            print 'Compiling: ', source
            pprint(source)
            self.dependencies=set()
            parsed=parser.parse(source)
            print 'Parsed: '
            pprint(parsed)

            currentKey=parsed[1]
            compiled=self.compile_token(parsed[2])

            print 'Compiled: ', currentKey, compiled, self.dependencies
            return currentKey, compiled, self.dependencies

        def compile_token(self,token):
                if isinstance(token,list):
                    print 'Compiling token: ', token
                    return apply(operators[token[0]],[self]+token[1:])
                print 'Passing token: ', token
                return str(token)

        
if __name__=="__main__":
        c=Compiler()
        t='A1=SUM(A1:A7, C3:C9)'
        pprint (c.compile(t))
        print
        print
        t='A1=SUM(A1:A7)'
        pprint (c.compile(t))
        print
        print
        t='A1=SUM(AVG(A1:A7))*2'
        pprint (c.compile(t))
        print
        print
#        t='A1="Hello world!"'
#        pprint (c.compile(t))
        print
        print
        t='A1=$A1+A$1+$A$1+A1'
        pprint (c.compile(t))
        print
        print
        t='A1=IF(A2=A1, 1, 0)'
        pprint (c.compile(t))
