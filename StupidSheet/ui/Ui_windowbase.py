# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StupidSheet/ui/windowbase.ui'
#
# Created: Tue May 29 16:31:23 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WindowBase(object):
    def setupUi(self, WindowBase):
        WindowBase.setObjectName("WindowBase")
        WindowBase.resize(QtCore.QSize(QtCore.QRect(0,0,600,480).size()).expandedTo(WindowBase.minimumSizeHint()))

        self.widget = QtGui.QWidget(WindowBase)
        self.widget.setObjectName("widget")

        self.vboxlayout = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.namebox = QtGui.QComboBox(self.widget)
        self.namebox.setEditable(True)
        self.namebox.setObjectName("namebox")
        self.hboxlayout.addWidget(self.namebox)

        self.functions = QtGui.QToolButton(self.widget)
        self.functions.setIcon(QtGui.QIcon(":/icons/funct.svg"))
        self.functions.setObjectName("functions")
        self.hboxlayout.addWidget(self.functions)

        self.cancelFormula = QtGui.QToolButton(self.widget)
        self.cancelFormula.setEnabled(False)
        self.cancelFormula.setIcon(QtGui.QIcon(":/icons/editdelete.svg"))
        self.cancelFormula.setObjectName("cancelFormula")
        self.hboxlayout.addWidget(self.cancelFormula)

        self.saveFormula = QtGui.QToolButton(self.widget)
        self.saveFormula.setEnabled(False)
        self.saveFormula.setIcon(QtGui.QIcon(":/icons/endturn.svg"))
        self.saveFormula.setObjectName("saveFormula")
        self.hboxlayout.addWidget(self.saveFormula)

        self.formula = QtGui.QLineEdit(self.widget)
        self.formula.setObjectName("formula")
        self.hboxlayout.addWidget(self.formula)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.tabWidget2 = QtGui.QTabWidget(self.widget)
        self.tabWidget2.setObjectName("tabWidget2")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.grid = QtGui.QTableWidget(self.tab)
        self.grid.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.NoEditTriggers)
        self.grid.setDragDropOverwriteMode(False)
        self.grid.setAlternatingRowColors(True)
        self.grid.setObjectName("grid")
        self.vboxlayout1.addWidget(self.grid)
        self.tabWidget2.addTab(self.tab,"")
        self.vboxlayout.addWidget(self.tabWidget2)
        WindowBase.setCentralWidget(self.widget)

        self.MenuBar = QtGui.QMenuBar(WindowBase)
        self.MenuBar.setGeometry(QtCore.QRect(0,0,600,29))
        self.MenuBar.setObjectName("MenuBar")

        self.fileMenu = QtGui.QMenu(self.MenuBar)
        self.fileMenu.setObjectName("fileMenu")

        self.helpMenu = QtGui.QMenu(self.MenuBar)
        self.helpMenu.setObjectName("helpMenu")

        self.editMenu = QtGui.QMenu(self.MenuBar)
        self.editMenu.setObjectName("editMenu")
        WindowBase.setMenuBar(self.MenuBar)

        self.toolBar = QtGui.QToolBar(WindowBase)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setObjectName("toolBar")
        WindowBase.addToolBar(self.toolBar)

        self.statusBar = QtGui.QStatusBar(WindowBase)
        self.statusBar.setObjectName("statusBar")
        WindowBase.setStatusBar(self.statusBar)

        self.fileNewAction = QtGui.QAction(WindowBase)
        self.fileNewAction.setIcon(QtGui.QIcon(":/icons/filenew.svg"))
        self.fileNewAction.setObjectName("fileNewAction")

        self.fileOpenAction = QtGui.QAction(WindowBase)
        self.fileOpenAction.setIcon(QtGui.QIcon(":/icons/fileopen.svg"))
        self.fileOpenAction.setObjectName("fileOpenAction")

        self.fileSaveAction = QtGui.QAction(WindowBase)
        self.fileSaveAction.setIcon(QtGui.QIcon(":/icons/filesave.svg"))
        self.fileSaveAction.setObjectName("fileSaveAction")

        self.fileSaveAsAction = QtGui.QAction(WindowBase)
        self.fileSaveAsAction.setIcon(QtGui.QIcon(":/icons/filesaveas.svg"))
        self.fileSaveAsAction.setObjectName("fileSaveAsAction")

        self.filePrintAction = QtGui.QAction(WindowBase)
        self.filePrintAction.setIcon(QtGui.QIcon(":/icons/fileprint.svg"))
        self.filePrintAction.setObjectName("filePrintAction")

        self.fileExitAction = QtGui.QAction(WindowBase)
        self.fileExitAction.setIcon(QtGui.QIcon(":/icons/exit.svg"))
        self.fileExitAction.setObjectName("fileExitAction")

        self.editUndoAction = QtGui.QAction(WindowBase)
        self.editUndoAction.setIcon(QtGui.QIcon(":/icons/undo.svg"))
        self.editUndoAction.setObjectName("editUndoAction")

        self.editRedoAction = QtGui.QAction(WindowBase)
        self.editRedoAction.setIcon(QtGui.QIcon(":/icons/redo.svg"))
        self.editRedoAction.setObjectName("editRedoAction")

        self.editCutAction = QtGui.QAction(WindowBase)
        self.editCutAction.setIcon(QtGui.QIcon(":/icons/editcut.svg"))
        self.editCutAction.setObjectName("editCutAction")

        self.editCopyAction = QtGui.QAction(WindowBase)
        self.editCopyAction.setIcon(QtGui.QIcon(":/icons/editcopy.svg"))
        self.editCopyAction.setObjectName("editCopyAction")

        self.editPasteAction = QtGui.QAction(WindowBase)
        self.editPasteAction.setIcon(QtGui.QIcon(":/icons/editpaste.svg"))
        self.editPasteAction.setObjectName("editPasteAction")

        self.editFindAction = QtGui.QAction(WindowBase)
        self.editFindAction.setIcon(QtGui.QIcon(":/icons/find.svg"))
        self.editFindAction.setObjectName("editFindAction")

        self.helpContentsAction = QtGui.QAction(WindowBase)
        self.helpContentsAction.setIcon(QtGui.QIcon(":/icons/help.svg"))
        self.helpContentsAction.setObjectName("helpContentsAction")

        self.helpAboutAction = QtGui.QAction(WindowBase)
        self.helpAboutAction.setObjectName("helpAboutAction")

        self.actionEdit_Cell = QtGui.QAction(WindowBase)
        self.actionEdit_Cell.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionEdit_Cell.setVisible(False)
        self.actionEdit_Cell.setObjectName("actionEdit_Cell")
        self.fileMenu.addAction(self.fileNewAction)
        self.fileMenu.addAction(self.fileOpenAction)
        self.fileMenu.addAction(self.fileSaveAction)
        self.fileMenu.addAction(self.fileSaveAsAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.filePrintAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileExitAction)
        self.helpMenu.addAction(self.helpContentsAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.helpAboutAction)
        self.editMenu.addAction(self.editUndoAction)
        self.editMenu.addAction(self.editRedoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.editCutAction)
        self.editMenu.addAction(self.editCopyAction)
        self.editMenu.addAction(self.editPasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.editFindAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.actionEdit_Cell)
        self.MenuBar.addAction(self.fileMenu.menuAction())
        self.MenuBar.addAction(self.editMenu.menuAction())
        self.MenuBar.addAction(self.helpMenu.menuAction())
        self.toolBar.addAction(self.fileNewAction)
        self.toolBar.addAction(self.fileOpenAction)
        self.toolBar.addAction(self.fileSaveAction)
        self.toolBar.addAction(self.filePrintAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editUndoAction)
        self.toolBar.addAction(self.editRedoAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editCutAction)
        self.toolBar.addAction(self.editCopyAction)
        self.toolBar.addAction(self.editPasteAction)

        self.retranslateUi(WindowBase)
        QtCore.QObject.connect(self.formula,QtCore.SIGNAL("returnPressed()"),self.saveFormula.animateClick)
        QtCore.QMetaObject.connectSlotsByName(WindowBase)

    def retranslateUi(self, WindowBase):
        WindowBase.setWindowTitle(QtGui.QApplication.translate("WindowBase", "Form1", None, QtGui.QApplication.UnicodeUTF8))
        self.functions.setText(QtGui.QApplication.translate("WindowBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.grid.setRowCount(20)
        self.grid.setColumnCount(20)
        self.grid.clear()
        self.grid.setColumnCount(20)
        self.grid.setRowCount(20)
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab), QtGui.QApplication.translate("WindowBase", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.fileMenu.setTitle(QtGui.QApplication.translate("WindowBase", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.helpMenu.setTitle(QtGui.QApplication.translate("WindowBase", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.editMenu.setTitle(QtGui.QApplication.translate("WindowBase", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNewAction.setText(QtGui.QApplication.translate("WindowBase", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNewAction.setIconText(QtGui.QApplication.translate("WindowBase", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNewAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.fileOpenAction.setText(QtGui.QApplication.translate("WindowBase", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.fileOpenAction.setIconText(QtGui.QApplication.translate("WindowBase", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.fileOpenAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAction.setText(QtGui.QApplication.translate("WindowBase", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAction.setIconText(QtGui.QApplication.translate("WindowBase", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAsAction.setText(QtGui.QApplication.translate("WindowBase", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSaveAsAction.setIconText(QtGui.QApplication.translate("WindowBase", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.filePrintAction.setText(QtGui.QApplication.translate("WindowBase", "&Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.filePrintAction.setIconText(QtGui.QApplication.translate("WindowBase", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.filePrintAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setText(QtGui.QApplication.translate("WindowBase", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.fileExitAction.setIconText(QtGui.QApplication.translate("WindowBase", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.editUndoAction.setText(QtGui.QApplication.translate("WindowBase", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.editUndoAction.setIconText(QtGui.QApplication.translate("WindowBase", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.editUndoAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.editRedoAction.setText(QtGui.QApplication.translate("WindowBase", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.editRedoAction.setIconText(QtGui.QApplication.translate("WindowBase", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.editRedoAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.editCutAction.setText(QtGui.QApplication.translate("WindowBase", "Cu&t", None, QtGui.QApplication.UnicodeUTF8))
        self.editCutAction.setIconText(QtGui.QApplication.translate("WindowBase", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.editCutAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.editCopyAction.setText(QtGui.QApplication.translate("WindowBase", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.editCopyAction.setIconText(QtGui.QApplication.translate("WindowBase", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.editCopyAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setText(QtGui.QApplication.translate("WindowBase", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setIconText(QtGui.QApplication.translate("WindowBase", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.editPasteAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.editFindAction.setText(QtGui.QApplication.translate("WindowBase", "&Find...", None, QtGui.QApplication.UnicodeUTF8))
        self.editFindAction.setIconText(QtGui.QApplication.translate("WindowBase", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.editFindAction.setShortcut(QtGui.QApplication.translate("WindowBase", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.helpContentsAction.setText(QtGui.QApplication.translate("WindowBase", "&Contents...", None, QtGui.QApplication.UnicodeUTF8))
        self.helpContentsAction.setIconText(QtGui.QApplication.translate("WindowBase", "Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setText(QtGui.QApplication.translate("WindowBase", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.helpAboutAction.setIconText(QtGui.QApplication.translate("WindowBase", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Cell.setText(QtGui.QApplication.translate("WindowBase", "Edit Cell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Cell.setShortcut(QtGui.QApplication.translate("WindowBase", "F2", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
