from windowbase import WindowBase
import engine
import qt
import opensave
import os
import pickle
import pprint
import tokenize
import StringIO
from engine import isKey,keyCoord,coordKey
import time

class Window(WindowBase):
	def __init__(self):
		WindowBase.__init__(self)
		self.grid.setNumRows(10000)
		self.grid.setNumCols(26*26)
		h=self.grid.horizontalHeader()
		for i in range (0,26):
			h.setLabel(i,chr(97+i))
		for i in range (0,26):
			for j in range (0,26):
				h.setLabel(26+i*26+j,chr(97+i)+chr(97+j))
		self.sheet=engine.SpreadSheet(self)
		self.editing=None
		
		self.connect(self.sheet,qt.PYSIGNAL("cellChanged"),self.changeCell)
		self.fname=None
		
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
		
	def changeCell(self,key,value):
		print key,value
		(x,y)=keyCoord(key)
		self.grid.setText(y,x,str(value))
		
	def clickedGrid(self,row, col, button, mousePos):
		h=self.grid.horizontalHeader()
		label=str(h.label(col))+str(row+1)
		self.editing=label
		self.cellName.setText(label)
		try:
			f=self.sheet.getformula(label)
		except KeyError:
			f=''
		self.formula.setText(f)
		self.saveFormula.setEnabled(True)
		self.cancelFormula.setEnabled(True)
		self.formula.setFocus()
		
	def saveFormulaSlot(self):
		self.sheet[self.editing]=str(self.formula.text())
		self.saveFormula.setEnabled(False)
		self.cancelFormula.setEnabled(False)
		self.cellName.setText("")
		self.changeCell(self.editing,self.sheet[self.editing])
		self.sheet.reCalculate(self.editing)

		
	def fileExit(self):
		self.close()
		self.deleteLater()
		
	def editCopy(self):
		sel=self.grid.selection(0)
		self.clipboard=[]
		for col in range(sel.leftCol(),sel.rightCol()+1):
			r=[]
			for row in range(sel.topRow(),sel.bottomRow()+1):
				key=coordKey(col,row)
##				print "key=",key
				r.append(self.sheet.getformula(key))
			self.clipboard.append(r)
##		pprint.pprint(self.clipboard)
		self.clipPos=(sel.leftCol(),sel.topRow())
		
	def editPaste(self):
		print "paste start:",time.time()
		sel=self.grid.selection(0)
		#Height and width of clipboard
		w=len(self.clipboard)
		h=len(self.clipboard[0])
##		print "h,w=",h,w

		#Offsets of cell displacement
		dx=sel.leftCol()-self.clipPos[0]
		dy=sel.topRow()-self.clipPos[1]
		
		#If selection is smaller than clipboard, just paste it *starting* at selection
		if h > (sel.bottomRow()-sel.topRow()+1) or w > (sel.rightCol()-sel.leftCol()+1):
##			print "non-tiling paste"
			for x in range (0,w):
				for y in range (0,h):
					key=coordKey(sel.leftCol()+x,sel.topRow()+y)
					#Displace the formula for the cell as much as needed
##					print "x,y=",x,y
					form=self.displaceFormula(self.clipboard[x][y],dx,dy)
					self.sheet[key]=form
					self.changeCell(key,self.sheet[key])
		else: #Selection is larger than clipboard		
			#Implement tiling paste, which seems to be the usual way.
			for y in range(sel.topRow(),sel.bottomRow()+1):
				for x in range(sel.leftCol(),sel.rightCol()+1):
					key=coordKey(x,y)
					mx=(x-sel.leftCol())%w
					my=(y-sel.topRow())%h
					mdx=(x-mx)-self.clipPos[0]
					mdy=(y-my)-self.clipPos[1]
					form=self.displaceFormula(self.clipboard[mx][my],mdx,mdy)
					self.sheet[key]=form
					self.changeCell(key,self.sheet[key])
		print "paste end:",time.time()
		print "deps after paste"
		print self.sheet._deps
		#Recalculate all the pasted area
		for y in range(sel.topRow(),sel.bottomRow()+1):
			for x in range(sel.leftCol(),sel.rightCol()+1):
				self.sheet.reCalculate(coordKey(x,y))
	
	def	displaceFormula(self,formula,_dx,_dy):
		global toks,dx,dy,program
		toks=[]
		dx=_dx
		dy=_dy
		program=[]
		lastrow, lastcol = 1, 0
		lastline = ''
		
		f=StringIO.StringIO(formula)
		tokenize.tokenize(f.readline,tokeneater)
##		print toks
##		pprint.pprint(toks)
		for token in toks:
			apply(rebuild,token)
##		print "program: ",program
		if program[0]=='':
			program=program[1:]
		return ''.join(program)

		
#Shamelessly stolen from Ka-Ping Yee's regurgitate
def rebuild(type, token, (startrow, startcol), (endrow, endcol), line):
	global lastrow, lastcol, lastline, program

	# Deal with the bits between tokens.
	if lastrow == startrow == endrow:            # ordinary token
		program.append(line[lastcol:startcol])
	elif lastrow != startrow:                    # backslash continuation
		program.append(lastline[lastcol:] + line[:startcol])
	elif startrow != endrow:                     # multi-line string
		program.append(lastline[lastcol:startcol])

	# Append the token itself.
	program.append(token)

	# Save some information for the next time around.
	if token and token[-1] == '\n':
		lastrow, lastcol = endrow+1, 0           # start on next line
	else:
		lastrow, lastcol = endrow, endcol        # remember last position

	lastline = line                              # remember last line



def tokeneater(type,key,start,end,line):
	global toks,dx,dy
##	print "tokeneater:",tokenize.tok_name[type],key
	if tokenize.tok_name[type]=='NAME':
		if isKey(key):
			(x,y)=keyCoord(key)
			x=x+dx
			y=y+dy
##			print "displacing %s to %s"%(key,coordKey(x,y))
			key=coordKey(x,y)
	toks.append((type,key,start,end,line))
					

#####################################################################
#Psyco cheating
#####################################################################
try:
	import psyco
	psyco.bind(tokeneater)
	psyco.bind(rebuild)
	psyco.bind(Window.displaceFormula)
except:
	pass

	
	
######################################################################
#Don't look below... global variables Yeech!
######################################################################



toks=[]
dx=0
dy=0
program = []
lastrow, lastcol = 1, 0
lastline = ''
