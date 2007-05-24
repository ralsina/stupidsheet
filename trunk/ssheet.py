#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui

from ssheet.window import Window

def main(args):
    app=QtGui.QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
        main(sys.argv)
