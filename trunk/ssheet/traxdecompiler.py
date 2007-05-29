from pprint import pprint
import sys
import aperiot

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
        return '%s(%s)'%(args[0],
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

def decompile_token(token):
        if isinstance (token,aperiot.lexer.Identifier):
                v=token.symbolic_name.lower()
                dependencies.add(v)
                return v
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
           'absrow':absOp
           }



def regurgitate_assignment(assignment):
        '''Takes a single assignment and returns traxter code'''
        var=assignment[0]
        code=decompile_token(assignment[1])
        return '%s=%s'%(var.symbolic_name,code)

def regurgitate(assignlist):
        '''Takes an assignlist (the output of the trax parser)
        and produces traxter code.'''
        return ';'.join([regurgitate_assignment(a) for a in assignlist])

if __name__=="__main__":
        from aperiot.parsergen import build_parser
        traxparser = build_parser('traxter')
        t='A1=SUM(A1:A7);A1=SUM(AVG(A1:A7))*2;A1=$A1+A$1+$A$1+A1;'
        pprint (regurgitate(traxparser.parse(t)))
