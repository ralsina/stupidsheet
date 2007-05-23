from pprint import pprint
import aperiot.lexer as lexer


def splitcell(cname):
    # Sure, this only works for well-formed cellnames ;-)
    col=''
    row=''
    for c in cname:
        if c.isalpha():
            col+=c
        else:
            row+=c
    return col,int(row)

def col2num(col):
    ac=0
    a=ord('a')
    col=col.lower()
    i=1
    for c in col:
        v=ord(c)-a+1
        ac+=v*(26**(len(col)-i))
        i+=1
    return ac

def num2col(num):
    res=chr(65+(num-1)%26).lower()
    if num > 26:
        res=chr(64+(num-1)/26).lower()+res
    return res

def cellrange(start,end):
    sc,sr=splitcell(start)
    ec,er=splitcell(end)

    res=[]
    for col in xrange(col2num(sc),col2num(ec)+1):
        for row in xrange(sr,er+1):
                res.append(lexer.Identifier(num2col(col)+str(row)))

    return res
