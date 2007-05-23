from qt import QObject,PYSIGNAL
import math
import compiler
import sys


import cells

class Cell(cells.Model):
    formula=cells.makecell(value='')
    @cells.fun2cell()
    def value(self,prev):
        print ">>eval %s %s<<"%(self.key,self.formula),
        rv=eval(self.formula, self.ss.tools, self.ss)
        self.ss.emit(PYSIGNAL("cellChanged"),(self.key,rv))
        return rv
    def __init__(self, ss, key, *args, **kwargs):
        self.ss=ss
        self.key=key
        cells.Model.__init__(self, *args, **kwargs)


class SpreadSheet(QObject):
    tools = {}
    ss={}
    def __init__(self,parent):
        global obj
        QObject.__init__(self,parent)
        for name in dir(math):
            if name[0]<>"_":
                self.tools[name]=eval('math.'+name)

    def __getitem__(self,key):
        if not self.ss.has_key(key):
            return 0
        return self.ss[key].value

    def __setitem__(self,key,v):
        if not self.ss.has_key(key):
            c=Cell(self,key)
            c.formula=v
            self.ss[key]=c
        else:
            self.ss[key].formula=v

    def getformula(self, key):
        if key in self.ss:
            return self.ss[key].formula
        else:
            return ''

    __repr__=ss.__repr__


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

try:
	import psyco
	psyco.bind(SpreadSheet.__getitem__)
except:
	pass

		
if __name__ == "__main__":	
	ss = SpreadSheet(None)
	ss['a1'] = '5'
	ss['a2'] = 'a1*2'
	ss['a3'] = 'a2*2'
	print  ss['a3']
	ss['a1'] = '7'
	print  ss['a3']
