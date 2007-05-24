import math
import sys
from traxcompiler import compile

from PyQt4 import QtGui, QtCore

class SpreadSheet(QtCore.QObject):
    def __init__(self,parent):
        QtCore.QObject.__init__(self,parent)
    _cells = {}
    _deps = {}
    tools = {}  
    def __setitem__(self, key, formula):
        key=key.lower()
        c=compile('%s=%s;'%(key,formula))
        self._cells[key] = c[key][0]
        print c
        self.emit(QtCore.SIGNAL('changed'),(key))
    def getformula(self, key):
        key=key.lower()
        return self._cells[key][1]
    def __getitem__(self, key ):
        print self._cells[key]
        return eval(self._cells[key], self.tools, self)

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
