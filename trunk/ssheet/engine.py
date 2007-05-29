import math
import sys
from traxcompiler import traxcompile
from PyQt4 import QtGui, QtCore
from graph_lib import *
import ssheet.functions as functions

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
        c=traxcompile('%s=%s;'%(key,formula))
        self._cells[key] = [c[key][0],False,compile(c[key][0],"Formula for %s"%key,'eval')]

        # Dependency graph
        if not self.graph.has_node(key):
            self.graph.add_node(key)
        for edge in self.graph.in_arcs(key):
            self.graph.delete_edge(edge)
        for cell in c[key][1]:
            if not self.graph.has_node(cell):
                self.graph.add_node(cell)
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
        if not self._cells.has_key(key):
            return 0
        if self._cells[key][1]:
            return "ERROR: cyclic dependency"
        else:
            print 'evaluating [%s]: '%key,type(self._cells[key][0]),self._cells[key][0]
            print self._cells[key][0], self
            r=eval(self._cells[key][0], self.tools, self)
            print r
            return r


        
if __name__ == "__main__":  
    ss = SpreadSheet(None)
    ss['a1'] = '5'
    ss['a2'] = 'a1*2'
    ss['a3'] = 'a2*2'
    print  ss['a3']
    ss['a1'] = '7'
    print  ss['a3']
