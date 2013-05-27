# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import WorkBookWidget

class MainWindow(QtGui.QMainWindow):
    
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        
        self.workBookWidget = WorkBookWidget.WorkBookWidget()
        self.setCentralWidget(self.workBookWidget)
        
        
        self.workBookWidget.loadExcel("/home/pyxl/pyqt-spreadsheet/examples/example-1.xls")
        
        
    def loadDefaults(self):
        for n in range(1, 4):
            self.workBooWidget.addSheet("Sheet %s" % n)
            