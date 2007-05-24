import math
import compiler
import sys

from PyQt4 import QtGui, QtCore

class SpreadSheet(QtCore.QObject):
    def __init__(self,parent):
        QtCore.QObject.__init__(self,parent)
    _cells = {}
    tools = {}  
    def __setitem__(self, key, formula):
        self._cells[key] = formula
        self.emit(QtCore.SIGNAL('changed'),(key))
        print key
    def getformula(self, key):
        return self._cells[key]
    def __getitem__(self, key ):
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
