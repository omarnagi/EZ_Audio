
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys

import time
import datetime


class List(QMainWindow):

    @pyqtSlot()
    def __init__(self):
        super().__init__()
        self.title = 'Sort the library'
        self.left = 1000
        self.top = 1000
        self.width = 1000
        self.height = 5000
        self.initUI()

    @pyqtSlot()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setStyleSheet("""QMainWindow{ background: red; }""")


        # # Create textbox
        # self.textbox = QLineEdit(self)
        # self.textbox.move(20, 20)
        # self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Ascending', self)
        self.button.move(0, 0)

        # Create a button in the window
        self.button2 = QPushButton('Descending' , self)
        self.button2.move(100, 0)

        self.listwidget = QListWidget(self)
        self.listwidget.move(0, 30)
        self.listwidget.resize(200, 500)
        # self.setStyleSheet("""QListWidget{ background: red; }""")
        self.listwidget.addItem("Yousif");
        self.listwidget.addItem("Jake");
        self.listwidget.addItem("Mohamed");
        self.listwidget.addItem("Abdulla");
        self.listwidget.addItem("Omar");

        self.button.clicked.connect(self.sortAscending)
        self.button2.clicked.connect(self.sortDescending)





        # date

        self.button3 = QPushButton('Ascending', self)
        self.button3.move(300, 0)

        # Create a button in the window
        self.button4 = QPushButton('Descending', self)
        self.button4.move(400, 0)

        self.listwidget2 = QListWidget(self)
        self.listwidget2.move(300, 30)
        self.listwidget2.resize(200, 500)
        # self.setStyleSheet("""QListWidget{ background: red; }""")
        self.listwidget2.addItem("01/02/2019");
        self.listwidget2.addItem("04/30/2012");
        self.listwidget2.addItem("03/15/2015");
        self.listwidget2.addItem("10/19/2005");
        self.listwidget2.addItem("09/34/2009");
        self.button3.clicked.connect(self.sortDatAscending)
        self.button4.clicked.connect(self.sortDateDescending)

        # by chanle
        # Create a button in the window
        self.button5 = QPushButton('Ascending', self)
        self.button5.move(600, 0)

        # Create a button in the window
        self.button6 = QPushButton('Descending' , self)
        self.button6.move(700, 0)

        self.listwidget3 = QListWidget(self)
        self.listwidget3.move(600, 30)
        self.listwidget3.resize(200, 500)
        # self.setStyleSheet("""QListWidget{ background: red; }""")
        self.listwidget3.addItem("Ladysif1");
        self.listwidget3.addItem("Politeness");
        self.listwidget3.addItem("Chorus");
        self.listwidget3.addItem("Blarney");
        self.listwidget3.addItem("Fogcreep");

        self.button5.clicked.connect(self.sortChannelAscending)
        self.button6.clicked.connect(self.sortChanelDescending)


    @pyqtSlot()
    def sortAscending(self):
        self.listwidget.sortItems()
        self.show()
    @pyqtSlot()
    def sortDescending(self):
        self.listwidget.sortItems(QtCore.Qt.DescendingOrder)
        self.show()
    @pyqtSlot()
    def sortDatAscending(self):
        self.listwidget2.sortItems()
        self.show()
    @pyqtSlot()
    def sortDateDescending(self):
        self.listwidget2.sortItems(QtCore.Qt.DescendingOrder)
        self.show()

    @pyqtSlot()
    def sortChannelAscending(self):
        self.listwidget3.sortItems()
        self.show()

    @pyqtSlot()
    def sortChanelDescending(self):
        self.listwidget3.sortItems(QtCore.Qt.DescendingOrder)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = List()
    ex.show()
    sys.exit(app.exec_())


