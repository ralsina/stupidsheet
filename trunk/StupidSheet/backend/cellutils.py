from pprint import pprint

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
    sc,sr=keyCoord(start)
    ec,er=keyCoord(end)

    res=[]
    for col in xrange(sc,ec+1):
        for row in xrange(sr,er+1):
                res.append(['cell', coordKey(col,row)])

    return res

def parse_cellref(cellref):
    '''Takes a half-cooked cellref from the parser and makes it nice'''
    expanded=[]
    for label in cellref[1:]:
        if isKey(label):
            c,r=splitcell(label)
            expanded+=[c,r]
        else:
            expanded.append(label)

    processed=['cell']
    is_abs=False
    for label in expanded:
        if label=='ABS':
            is_abs=True
            continue
        if is_abs:
            if type(label)==str:
                processed.append(['abscol',label])
            else:
                processed.append(['absrow',label])
        else:
            if type(label)==str:
                processed.append(['relcol',label])
            else:
                processed.append(['relrow',label])
        is_abs=False

    return processed


