from pprint import pprint
from aperiot.parsergen import load_parser
import aperiot
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
        return '%s(%s)'%(args[0],
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
           'string':stringOp
           }


def traverse_tree(tokens,func,extra_args):
        '''applies func to all tokens in a tree'''
        for token in tokens:
                apply(func,[token]+list(extra_args))
                if type(token)==list:
                        traverse_tree(token,func,extra_args)

class Compiler:
        def __init__(self):
                self.dependencies=set()

                # Basically, I am remplementing aperiot's load_parser
                # because it's broken when your project is in
                # more than one folder

                root,ext=os.path.splitext('StupidSheet.compiler.traxter.traxter')
                package_name = root + '_cfg'
                temp_table = {}
                exec "import " + package_name in temp_table
                package_path = eval(package_name, temp_table).__path__[0]
                filename = os.path.join(package_path, 'traxter.pkl')
                file_handler = file(filename, 'r')
                self.parser = pickle.load(file_handler)
                file_handler.close()

        def compile(self,source):
            compiled={}
            assign_list=self.parser.parse(source)
            for assignment in assign_list:
                    pprint(assignment)
                    self.dependencies=set()
                    var,c=self.compile_assignment(assignment)
                    compiled[var]=[c,self.dependencies]
            return compiled

        def compile_token(self,token):
                if isinstance (token,aperiot.lexer.Identifier):
                    self.dependencies.add(token.symbolic_name.lower())
                    return token.symbolic_name.lower()
                if isinstance(token,list):
                    return apply(operators[token[0]],[self]+token[1:])
                return str(token)

        def compile_assignment(self,tokens):
                currentKey=tokens[0].symbolic_name
                compiled=self.compile_token(tokens[1])
                return currentKey,compiled

if __name__=="__main__":
        c=Compiler()
        t='A1=SUM(A1:A7, C3:C9);'
        pprint (c.compile(t))
        print
        print
        t='A1=SUM(A1:A7);'
        pprint (c.compile(t))
        print
        print
        t='A1=SUM(AVG(A1:A7))*2;'
        pprint (c.compile(t))
        print
        print
        t='A1=$A1+A$1+$A$1+A1;'
        pprint (c.compile(t))
        print
        print
        t='A1="Hello world!";'
        pprint (c.compile(t))
