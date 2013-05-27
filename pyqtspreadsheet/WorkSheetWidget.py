# -*- coding: utf-8 -*-

from PyQt4 import QtGui


class WorkSheetWidget(QtGui.QWidget):
    
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        ## Main layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)
        
        
        ## Table (needs ext)
        self.table = QtGui.QTableWidget(self)
        self.mainLayout.addWidget(self.table)
        
        #self._setup()
        
    def setRowCount(self, rows):
        self.table.setRowCount(rows)
        
    def setColumnCount(self, cols):
        self.table.setColumnCount(cols)
        
        
    def _setup(self):
        a2z = [chr(a) for a in range(ord('A'), ord('Z') + 1)]
        self.table.setColumnCount(len(a2z))
        #for a in range(ord('A'), ord('Z')+1):
        #print a2z
        self.table.setHorizontalHeaderLabels(a2z)
        
        self.table.setRowCount(20)
        
    def setCellText(self, row, col, txt):
        print "setCell", row, col, txt
        item = self.table.item(row, col)
        if item == None:
            item = QtGui.QTableWidgetItem()
            self.table.setItem(row, col, item)
            #print "stop", ss
        print item
        item.setText(txt)
        
        #workSheet.setExcelCell(row, col, sheet.cell(row, col))
        
        
         