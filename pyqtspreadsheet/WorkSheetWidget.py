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
        
        self._setup()
        
    def _setup(self):
        a2z = [chr(a) for a in range(ord('A'), ord('Z') + 1)]
        self.table.setColumnCount(len(a2z))
        #for a in range(ord('A'), ord('Z')+1):
        #print a2z
        self.table.setHorizontalHeaderLabels(a2z)
        
        self.table.setRowCount(20)
        
        