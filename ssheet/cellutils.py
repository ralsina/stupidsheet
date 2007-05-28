from pprint import pprint
import aperiot.lexer as lexer

def isKey(key):
    if (key[0].isalpha() and key[1:].isdigit()) or (key[0:1].isalpha() and key[2:].isdigit()):
        return True
    return False

def coordKey(x,y):
    if x< 26:
        key=chr(97+x)
    else:
        key=chr(97+int(x/26))+chr(97+x%26)
    key=key+str(y+1)
    return key
    
    
def keyCoord(key):      
    if key[1].isalpha():
        x=(ord(key[0])-97)*26+ord(key[1])-97
        y=int(key[2:])-1
    else:
        x=ord(key[0])-97
        y=int(key[1:])-1
    return (x,y)

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

def cellrange(start,end):
    sc,sr=splitcell(start)
    ec,er=splitcell(end)

    res=[]
    for col in xrange(keyCoord(sc),col2num(ec)+1):
        for row in xrange(sr,er+1):
                res.append(lexer.Identifier(coordKey(col)+str(row)))

    return res
