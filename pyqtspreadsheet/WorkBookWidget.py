# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import Qt, SIGNAL

import WorkSheetWidget


class WorkBookWidget(QtGui.QWidget):
    
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        ## Main layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)
        
        ## Stack
        self.stack = QtGui.QStackedWidget()
        self.mainLayout.addWidget(self.stack)
        
        ## TabBar
        self.tabBar = QtGui.QTabBar()
        self.tabBar.setShape(QtGui.QTabBar.RoundedSouth);
        self.mainLayout.addWidget(self.tabBar)
        self.connect(self.tabBar, SIGNAL("currentChanged(int)"), self.on_tab_change)
        
        

    def on_tab_change(self, idx):
        print "TAB"
        self.stack.setCurrentIndex(idx)
     
    def addSheet(self, title, item=None):
        
        # add the tab
        self.tabBar.addTab(title)
        
        ## create and add new sheet
        workSheet = WorkSheetWidget.WorkSheetWidget()
        self.stack.addWidget( workSheet )
           
    
    def loadExcel(self, file_path): 
        
        pass
    
