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
        
        

    def on_tab_change(self, idx):
        print "TAB"
        self.stack.setCurrentIndex(idx)
     
    
        
            
        
           
    
    def loadExcel(self, file_path): 
        
        fi = QtCore.QFileInfo(file_path)
        print file_path, fi , fi.exists()
        if not fi.exists():
            ## TODO - raise warning
            return
        wb = xlrd.open_workbook(file_path)
        
        for ws in wb.sheets():
            print "Sheet", ws.name
            
            sheet = self.addSheet(ws.name)
            
            sheet.setRowCount(ws.nrows)
            sheet.setColumnCount(ws.ncols)
            
            for row in range(ws.nrows):
                for col in range(ws.ncols):
                    print row, col, ws.cell(row, col).value
                    sheet.setCellText(row, col, "%s" % ws.cell(row, col).value )
                
    def addSheet(self, title):
        
        # add the tab
        self.tabBar.addTab(title)
        
        ## create and add new sheet
        workSheet = WorkSheetWidget.WorkSheetWidget()
        self.stack.addWidget( workSheet )
        
        return workSheet
   
                
                   
        
        
    
