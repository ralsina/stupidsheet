##~ Copyright (c) 2004 Roberto Alsina <ralsina@kde.org>
##~ 
##~ Permission is hereby granted, free of charge, to any person obtaining a 
##~ copy of this software and associated documentation files (the 
##~ "Software"), to deal in the Software without restriction, including 
##~ without limitation the rights to use, copy, modify, merge, publish, 
##~ distribute, sublicense, and/or sell copies of the Software, and to permit
##~ persons to whom the Software is furnished to do so, subject to the 
##~ following conditions:
##~ 
##~ The above copyright notice and this permission notice shall be included
##~ in all copies or substantial portions of the Software.
##~ 
##~ THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
##~ OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
##~ MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
##~ IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
##~ CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
##~ TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
##~ SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""
This module contains functions implementing a generic open/save 
interface for applications. It supports regular, compressed and/or
encrypted files, without having to make your application more complex.

As long as you can pickle your data into a string, this should be easy 
to use and just work.

The compressed files are compressed using python's zlib, the encryption 
is made using python's rotor.

If you don't do autosaves, and you don't mind the user having to type
the password on all save operations, you can happily ignore the "key"
parameters and return values, and everything should work anyway.

The save is atomic: First we save to a temporal file, then rename it 
into the desired name. This is so noone can open the file while it's not
completely saved.

KNOWN ISSUES: 

* It will use lots of memory for a large file, because it keeps it fully
  in memory (won't fix)

* A file encrypted with a null password is not encrypted (won't fix)

* Compressed files are not gunzip/gzip compatible. (may fix)

* No way to choose the filtering in the save dialog (may fix)

* Could be cleaner by removing all dialog code and/or making it optional
  and/or adding more functions for it. (won't fix)

"""

__author__ = 'Roberto Alsina <ralsina@kde.org>'
__license__ = 'MIT/X11'


import qt
import zlib
import traceback
import tempfile
import os
import shutil

def encrypt(data,key=None):
	"""

	Helper function, encrypts data using key, with a 12-wheel rotor.
	
	Returns the encrypted data. If key==None, it's not encrypted
	"""
	if not key: #No key, no encryption
		return data
	import rotor
	rt=rotor.newrotor(key,12)
	return rt.encrypt(data)

def decrypt(data,key=None):	
	"""

	Helper function, decrypts data using key, with a 12-wheel rotor
	
	Returns the decrypted data. Remember that decryption ALWAYS returns
	something. I suggest you use some magic cookie at the beginning
	to see if the data returned makes sense.
	
	If key==None, it's not decrypted
	
	"""
	if not key: #No key, no encryption
		return data
	import rotor
	rt=rotor.newrotor(key,12)
	return rt.decrypt(data)
	
	
def saveFile(fname,data,key=None):
	"""

	data: a string containing the data to ve saved.
	fname: name of the file where you want to save. 
	
	If the name ends in .comp, it will be saved compressed using zlib.
	If the name ends in .rotor, it will be saved encrypted using the key.
	If the name ends in .comp.rotor, it will be compressed, then 
	encrypted.
	
	Using .rotor.comp makes no sense, because encrypted files don't
	compress at all, so it's not supported.
	
	key is a string used for rotor encryption
	If a key is required but not provided, a dialog will popup asking 
	for it.
	
	If there is an error when compressing, or writing, or anything else,
	it will popup a error message.
	
	The return value on success will be True,key with key being the 
	encription key or None.
	
	On error, it will return False,key with key being the encription
	key or None.
	
	"""
	tempfile.tempdir=os.path.dirname(fname)
	tname=tempfile.mktemp()
	if os.access(fname,os.W_OK) or not os.access(fname,os.F_OK):
		extensions=fname.split('.')
		try:	
		
			if len (extensions)>1:
				if extensions[-2]=='comp' or extensions[-1]=='comp': #A compressed file
					data=zlib.compress(data,9)
				if extensions[-1]=='rotor': #A rotor-crypted file

					if not key:
						(key,ok)=qt.QInputDialog.getText("Notty - Password",
									"Please enter the password",
									qt.QLineEdit.Password)
						if ok:
							key=str(key)
					data=encrypt(data,key)
					
			f=open(tname,'wb')
			f.write(data)
			f.flush()
			f.close()
			if os.access(fname,os.F_OK): #File exists	
				shutil.copymode(fname,tname)
			os.rename(tname,fname)
			return (True,key)
		except:
			traceback.print_exc()
			try:
				os.unlink(tname)
			except:
				# There really isn't much we can do :-) 
				pass
	qt.QMessageBox.critical(None,'Error - Notty',
			'Error writing to file "%s"'%fname,'Ok')
	return (False,key)
	
def openFile(fname,key=None):
	"""

	fname: name of the file you want to open. If no name is given,
	the standard file dialog will pop, asking for one.
	
	If the name ends in .comp, it will be uncompressed using zlib.
	If the name ends in .rotor, it will be decrypted using the key.
	If the name ends in .comp.rotor, it will be decrypted, then 
	uncompressed.
	
	Using .rotor.comp makes no sense, because encrypted files don't
	compress at all, so it's not supported.

	key is a string used for rotor encryption
	
	If a key is required but not provided, a dialog will popup asking 
	for it.
	
	Decrypting will **never** fail, so remember that when you process
	the code, maybe all you get is garbage, so implement some error 
	checking ;-)
	
	If there is an error when decompressing, or reading, or anything 
	else, it will popup a error message.
	
	The return value on success will be data,fname,key with key being 
	the encription key or None.
	
	On error, it will return '',key with key being the encription
	key or None.
	
	"""
	if fname=='': #Empty filename, ask for one
		fname=str(qt.QFileDialog.getOpenFileName(os.getcwd()))
		if not fname:
			return None
		else:
			return openFile(fname)

	extensions=fname.split('.')
	
	if os.access(fname,os.F_OK) and os.access(fname,os.R_OK):
		f=open(fname,'rb')
		data=f.read()	
		pos=-1
		if extensions[pos]=='rotor':
			if not key:
				(key,ok)=qt.QInputDialog.getText("Notty - Password",
						"Please enter the password",
						qt.QLineEdit.Password)
				key=str(key)
			if not key or not ok: #No key, no need to decrypt
				pass
			else:
				data=decrypt(data,key)
			pos=-2
		if extensions[pos]=='comp': #Compressed file
			data=zlib.decompress(data)
		return data,fname,key
	elif not (os.access(fname,os.F_OK)): #File doesn't exist
		try:
			f=open(fname,'wb') #But we can create it
			return '',fname,key
		except: #And we can't create it
			pass
		
	qt.QMessageBox.critical(None,'Error - Notty',
			'Error reading file "%s"'%fname,'Ok')
	return False
	
def saveAsFile(data,key=None):
	"""

	data is a string containing the data to be saved.
	key is a string used for rotor encryption
	
	It will popup a file dialog asking for a filename to save, then will
	call saveFile with that filename.

	If a key is required but not provided, a dialog will popup asking 
	for it.
	
	The return value on success will be True,filename,key with key being
	the encription key or None.
	
	On error, it will return False,filename,key with key being the 
	encription key or None.
	
	"""
	fname=str(qt.QFileDialog.getSaveFileName(os.getcwd()))
	if not fname:
		return False,'',None
	else:
		status,key=saveFile(fname,data,key)
		return status,key,fname
