# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class WorkBookWidget(QtGui.QWidget):
    
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        ## Main layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        ## TabBar
        self.tabBar = QtGui.QTabBar()
        self.mainLayout.addWidget(self.tabBar)
        
        ## Stack
        self.stack = QtGui.QStackedLayout()
        self.mainLayout.addLayout(self.stack)
        
     
    def addSheet(self, title, item=None):
        
        # add the tab
        self.tabBar.addTab(title)
        
        ## create and add new sheet
        workSheet = WorkSheetWidget()
        self.stack.addWidget( workSheet )
           
    
    def loadExcel(self, file_path): 
        
        pass