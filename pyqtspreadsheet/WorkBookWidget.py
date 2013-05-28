# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui 
from PyQt4.QtCore import Qt, SIGNAL

import xlrd

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
        
        
    def initDefaults(self):
        """This loads the default bog standard sheets, ie Sheet1 - 3"""
        for i in range(1, 4):
            sheet = self.addSheet("Sheet %s" % i)
            sheet.initDefaults()
            

    def on_tab_change(self, idx):
        print "TAB"
        self.stack.setCurrentIndex(idx)
     
    
        
            
        
    def clear(self):
		while self.tabBar.count() > 0:
			self.tabBar.removeTab(0)
			self.stack.removeWidget(self.stack.widget(0))
			
    
    def loadExcelFile(self, file_path): 
        
        self.setUpdatesEnabled(False)
        self.clear()
        
        
        fi = QtCore.QFileInfo(file_path)
        print file_path, fi , fi.exists()
        if not fi.exists():
            ## TODO - raise warning
            self.setUpdatesEnabled(True)
            return
        
        ## Open excel workbook
        wb = xlrd.open_workbook(file_path)
        
        ## add the sheets
        for ws in wb.sheets():
            
            sheet = self.addSheet(ws.name)
            
            sheet.setRowCount(ws.nrows)
            sheet.setColumnCount(ws.ncols)
            
            for row in range(ws.nrows):
                for col in range(ws.ncols):
            	    ## TODO colors etc
                    sheet.setCellText(row, col, "%s" % ws.cell(row, col).value )
                    
        self.setUpdatesEnabled(True)
        
                
    def addSheet(self, title):
        
        ## add the tab
        self.tabBar.addTab(title)
        
        ## create and add new widgets to stack
        workSheet = WorkSheetWidget.WorkSheetWidget()
        self.stack.addWidget( workSheet )
        
        return workSheet
   
                
                   
        
        
    
