import math
import sys
from StupidSheet.compiler.traxcompiler import Compiler
from StupidSheet.compiler.traxdecompiler import displace_source
from PyQt4 import QtGui, QtCore
from graph_lib import *
import StupidSheet.backend.functions as functions
from StupidSheet.backend.cellutils import *

class SpreadSheet(QtCore.QObject):
    _cells = {}
    tools = {}
    graph=Graph()
    compiler=Compiler()

    def __init__(self,parent):
        QtCore.QObject.__init__(self,parent)
        for name in dir(functions):
                self.tools[name]=eval('functions.'+name)
                

    def __setitem__(self, key, formula):
        key=key.lower()
        key, code, deps =self.compiler.compile('%s=%s'%(key,formula))
        print key, code, deps
        self._cells[key] = [code,
                            False,
                            compile(code,"Formula for %s"%key,'eval'),
                            formula]
        # Dependency graph
        if not self.graph.has_node(key):
            self.graph.add_node(key)
        for edge in self.graph.in_arcs(key):
            self.graph.delete_edge(edge)
        print 'deps: ',deps
        for cell in deps:
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
        if key in self._cells:
                return self._cells[key][-1]
        else:
                return ''

    def __getitem__(self, key ):
        if not self._cells.has_key(key) and isKey(key):
            print 'unknown cell: ', key
            return 0
        if self._cells[key][1]:
            return "ERROR: cyclic dependency"
        else:
            print 'evaluating [%s]: '%key,type(self._cells[key][0]),self._cells[key][0]
            print self._cells[key][0]
            r=eval(self._cells[key][0], self.tools, self)
            print r
            return r

    def displaceFormula(self,formula,keyFrom,keyTo):
        print 'Displacing: ',formula
        displaced=displace_source(formula,keyFrom,keyTo)
        print 'Displaced: ',displaced
        return displaced[displaced.find('=')+1:]

if __name__ == "__main__":  
    ss = SpreadSheet(None)
    ss['a1'] = '5'
    ss['a2'] = 'a1*2'
    ss['a3'] = 'a2*2'
    print  ss['a3']
    ss['a1'] = '7'
    print  ss['a3']
