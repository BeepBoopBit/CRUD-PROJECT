import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from GUI.globalVariable import *

class ModifyTable(QDialog):
    def __init__(self, apiCrud):
        super(ModifyTable, self).__init__()
        UIPATH = os.path.dirname(os.path.realpath(__file__)) + "\\ModifyTable.ui" 
        self.ui = loadUi(UIPATH,self)
        self.MOKbutton.clicked.connect(self.gotoaddCRUD)
        self.MExitbutton.clicked.connect(self.gotocancelCRUD)
        self.API = apiCrud;

    # Load Data

    def loadData(self, tableName):
        pass
    
    # PopUp Message Setup

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    # Functions of the Buttons // Both will Go Back to the Main Crud Window 

    def gotoaddCRUD(self):
        Widget.setCurrentIndex(3)
    
    def gotocancelCRUD(self):
        Widget.setCurrentIndex(3)
