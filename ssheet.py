#!/usr/bin/env python

import sys
from qt import *

import ssheet.window

def main(args):
        app=QApplication(args)

        win=ssheet.window.Window()
        app.setMainWidget(win)
        win.show()
        app.connect(app, SIGNAL("lastWindowClosed()")
                                                        , app
                                                        , SLOT("quit()")
                                                        )
        app.exec_loop()

if __name__=="__main__":
        main(sys.argv)
