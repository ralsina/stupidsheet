import math
import sys
from traxcompiler import compile
from PyQt4 import QtGui, QtCore
from graph_lib import *

import functions

class SpreadSheet(QtCore.QObject):
    _cells = {}
    tools = {}
    graph=Graph()

    def __init__(self,parent):
        QtCore.QObject.__init__(self,parent)
        for name in dir(functions):
                self.tools[name]=eval('functions.'+name)
                

    def __setitem__(self, key, formula):
        key=key.lower()
        c=compile('%s=%s;'%(key,formula))
        self._cells[key] = [c[key][0],False]

        # Dependency graph
        if not self.graph.has_node(key):
                self.graph.add_node(key)
        for edge in self.graph.in_arcs(key):
                self.graph.delete_edge(edge)
        for cell in c[key][1]:
                self.graph.add_edge(cell,key)
        try:
                print 'GRAPH(TOPO): ',self.graph.topological_sort()
                self._cells[key][1]=False
                print 'GRAPH(BFS) : ',self.graph.bfs(key)
                for cell in self.graph.bfs(key)[1:]:
                        self.emit(QtCore.SIGNAL('changed'),(cell))
        except Graph_topological_error:
                # We made the graph cyclic
                # So, mark this cell as evil
                self._cells[key][1]=True
                # And remove all incoming edges to go back to
                # status quo
                for edge in self.graph.in_arcs(key):
                        self.graph.delete_edge(edge)

    def getformula(self, key):
        key=key.lower()
        return self._cells[key][0]
    def __getitem__(self, key ):
        print self._cells[key]
        if self._cells[key][1]:
                return "ERROR: cyclic dependency"
        else:
                print 'evaluating [%s]: '%key,type(self._cells[key][0]),self._cells[key][0]
                return eval(str(self._cells[key][0]), self.tools, self)

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
