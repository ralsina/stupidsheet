from Ui_windowbase import Ui_WindowBase
import StupidSheet.backend.engine as engine
from PyQt4 import QtCore, QtGui
import opensave
import os
import pickle
import pprint
import tokenize
import StringIO
from StupidSheet.backend.cellutils import *
import time

class Window(QtGui.QMainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        
        # Set up the UI from designer
        self.ui=Ui_WindowBase()
        self.ui.setupUi(self)
        
        self.ui.grid.setRowCount(10000)
        self.ui.grid.setColumnCount(26*27)
        labels=[]
        for i in range (0,26):
            labels.append(chr(97+i).upper())
        for i in range (0,26):
            for j in range (0,26):
                labels.append((chr(97+i)+chr(97+j)).upper())
        self.ui.grid.setHorizontalHeaderLabels (labels)
        self.sheet=engine.SpreadSheet(self)
        self.editing=None
        self.fname=None

        QtCore.QObject.connect(self.ui.actionEdit_Cell,
                               QtCore.SIGNAL('activated()'),
                               self.editCell)
        QtCore.QObject.connect(self.ui.grid,
                               QtCore.SIGNAL('cellClicked(int,int)'),
                               self.editCell)
        QtCore.QObject.connect(self.ui.cancelFormula,
                               QtCore.SIGNAL('clicked()'),
                               self.cancelFormulaSlot)
        QtCore.QObject.connect(self.ui.saveFormula,
                               QtCore.SIGNAL('clicked()'),
                               self.saveFormulaSlot)
        QtCore.QObject.connect(self.sheet,
                               QtCore.SIGNAL('changed'),
                               self.changeCell)
        QtCore.QObject.connect(self.ui.editCopyAction,
                               QtCore.SIGNAL('activated()'),
                               self.editCopy)
        QtCore.QObject.connect(self.ui.editPasteAction,
                               QtCore.SIGNAL('activated()'),
                               self.editPaste)
        QtCore.QObject.connect(self.ui.editCutAction,
                               QtCore.SIGNAL('activated()'),
                               self.editCut)

        self.ui.grid.setFocus()

    def fileSaveAs(self):
        data=pickle.dumps(self.sheet._cells)
        (status,key,fname)=opensave.saveAsFile(data)
        if status:
            self.fname=fname
        return status
        
    def fileSave(self):
        data=pickle.dumps(self.sheet._cells)
        if not self.fname:
            return  self.fileSaveAs()
        return opensave.saveFile(self.fname,data)
            
    def fileOpen(self):
        (data,fname,key)=opensave.openFile('')
        self.fname=fname
        cells=pickle.loads(data)
        self.sheet=engine.SpreadSheet(self)
        for key in cells:
            self.sheet[key]=cells[key]
            self.changeCell(key,self.sheet[key])
        
    def changeCell(self,key):
        print 'changing: ',key
        (x,y)=keyCoord(key)
        print x,y
        item=self.ui.grid.item(y,x)
        if not item:
            item=QtGui.QTableWidgetItem('####')
            self.ui.grid.setItem(y,x,item)
        item.setText(str(self.sheet[key]))
        
    def editCell(self):
        row,col=self.ui.grid.currentRow(),self.ui.grid.currentColumn()
        h=self.ui.grid.horizontalHeader()
        label=coordKey(col,row)
        self.editing=label
        self.ui.namebox.clear()
        self.ui.namebox.addItem(label)

        try:
            f=self.sheet.getformula(label)
            # Need to decide if it's a formula or just a string            
            # Sure there are corner cases here but since classic
            # spreadsheet formulas don't support strings...
            if not f:
                pass
            # A special case for historical reasons
            elif f[0]=="'":
                pass
            elif f[0]=='"' and f[-1]=='"':
                f="'"+f[1:-1]
            else: #A formula
                f='='+f
        except KeyError:
            f=''
        self.ui.formula.setText(f)
        self.ui.saveFormula.setEnabled(True)
        self.ui.cancelFormula.setEnabled(True)
        self.ui.formula.setFocus()
        
    def saveFormulaSlot(self):
        # Let's do this the braindead way everyone does it:
        formula=str(self.ui.formula.text())
        if formula[0]=='=':
            self.sheet[self.editing]=formula[1:]
        elif formula[0]=="'": #Historical special case
            self.sheet[self.editing]='"%s"'%formula[1:]
        else:
            self.sheet[self.editing]='"%s"'%formula
            
        self.ui.saveFormula.setEnabled(False)
        self.ui.cancelFormula.setEnabled(False)
        self.ui.namebox.clear()
        self.ui.formula.clear()
        self.ui.grid.setFocus()
        self.changeCell(self.editing)

    def cancelFormulaSlot(self):
        print "cancelFormulaSlot"
        
    def fileExit(self):
        self.close()
        self.deleteLater()

    def editCut(self):
        pass
        
    def editCopy(self):
        # Let's do copy of multiple selections (which oocalc doesn't!)
        ranges=set(self.ui.grid.selectedRanges())

        minx=min([ r.leftColumn() for r in ranges ])
        maxx=max([ r.rightColumn() for r in ranges ])
        miny=min([ r.topRow() for r in ranges ])
        maxy=max([ r.bottomRow() for r in ranges ])

        self.clipboard_width=maxx-minx+1
        self.clipboard_height=maxy-miny+1

        self.clipPos=(minx,miny)

        self.clipboard={}

        for r in ranges:
            for x in range(r.leftColumn(),r.rightColumn()+1):
                for y in range(r.topRow(),r.bottomRow()+1):
                    i=self.ui.grid.item(x,y)
                    if i==0:
                        continue
                    key=coordKey(x,y)
                    f=self.sheet.getformula(key)
                    if f:
                        self.clipboard[key]='%s=%s;'%(key,self.sheet.getformula(key))

        print self.clipboard,self.clipboard_width,self.clipboard_height,self.clipPos

    def editPaste(self):
        selRanges=self.ui.grid.selectedRanges()
        # OOcalc doesn't support it. KSpread does, but it does
        # weird things. Let's go safe ;-)
        if len(selRanges)>1:
                QtGui.QMessageBox.information(self,'SSheet','Insert into multiple selection is not possible')
                return

        selw=selRanges[0].columnCount()
        selh=selRanges[0].rowCount()

        print selw,selh ,'||' ,self.clipboard_width ,self.clipboard_height
        # If the selection is not one cell, but is smaller than
        # the clipboard, warn that we will paste outside of the
        # selection
        if (selw <>1 or selh <>1 ) and (selw < self.clipboard_width or selh < self.clipboard_height):
            r=QtGui.QMessageBox.question(self,'SSheet',
                   'The content of the clipboard is bigger than the range selected.<br>Do you want to insert it anyway?',
                   QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            if r==QtGui.QMessageBox.No: return

        # Adjust the selection to match clipboard size
        if selw < self.clipboard_width:
             selRanges[0]=QtGui.QTableWidgetSelectionRange(selRanges[0].topRow(),
                                                           selRanges[0].leftColumn(),
                                                           selRanges[0].bottomRow(),
                                                           selRanges[0].leftColumn()+self.clipboard_width-1
                                                           )
        if selh < self.clipboard_height:
             selRanges[0]=QtGui.QTableWidgetSelectionRange(selRanges[0].topRow(),
                                                           selRanges[0].leftColumn(),
                                                           selRanges[0].topRow()+self.clipboard_height-1,
                                                           selRanges[0].rightColumn())
        self.ui.grid.setRangeSelected(selRanges[0],True)



        print "paste start:",time.time()
        # We traverse the target selection
        for x in range(selRanges[0].leftColumn(),selRanges[0].rightColumn()+1):
            for y in range(selRanges[0].topRow(),selRanges[0].bottomRow()+1):
                targetKey=coordKey(x,y)

                # How many cells to the right and down of the origin of the
                # source cells is the cell we should copy

                dx1=(x-selRanges[0].leftColumn())%self.clipboard_width
                dy1=(y-selRanges[0].topRow())%self.clipboard_height

                # How many cells to the right and down should the formula
                # of that cell be displaced

                dx2=x-self.clipPos[0]-dx1
                dy2=y-self.clipPos[1]-dy1

                # Key of the source cell to be copied
                sourceKey=coordKey(self.clipPos[0]+dx1,
                                   self.clipPos[1]+dy1)

                print targetKey,sourceKey,dx1,dy1,dx2,dy2
                if sourceKey in self.clipboard:
                        self.sheet[targetKey]=self.sheet.displaceFormula(self.clipboard[sourceKey],sourceKey,targetKey)
                        self.changeCell(targetKey)


        # Find the matching origin cell considering tiling

        # And paste

        print "paste end:",time.time()

                
    
