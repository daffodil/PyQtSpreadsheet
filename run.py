#!/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui

from pyqtspreadsheet import MainWindow


if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    
    app.setOrganizationName( "PyQtSpreadsheet" )
    app.setOrganizationDomain( "https://github.com/daffodil/pyqt-spreadsheet" )
    app.setApplicationName( "PyQtSpreadsheet" )
    app.setApplicationVersion( "0.1" )
    
    window = MainWindow.MainWindow()
    window.show()
    
    sys.exit(app.exec_())
