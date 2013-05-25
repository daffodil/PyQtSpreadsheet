# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import WorkBookWidget

class MainWindow(QtGui.QMainWindow):
    
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        
        self.workBooWidget = WorkBookWidget.WorkBookWidget()
        self.setCentralWidget(self.workBooWidget)
        
        for n in range(1, 4):
            self.workBooWidget.addSheet("Sheet %s" % n)
            