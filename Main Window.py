from PyQt5 import QtCore, QtGui, QtWidgets
from downloadlibrary import Ui_DownloadLibrary
from InitializeWindow import Window
from Sorting_Name_Date_Channel import  List
import conversionEngine

from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QListWidget,QMessageBox
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.defaultError = "Welcome to EZ Audio! Expand your audio library by entering a valid Youtube URL above."
        self.defaultURL = "Enter URL Here..."
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 415)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PrimaryLayout = QtWidgets.QVBoxLayout()
        self.PrimaryLayout.setContentsMargins(10, 10, 10, 90)
        self.PrimaryLayout.setSpacing(30)
        self.PrimaryLayout.setObjectName("PrimaryLayout")
        self.TopLayout = QtWidgets.QHBoxLayout()
        self.TopLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.TopLayout.setContentsMargins(0, -1, 0, 0)
        self.TopLayout.setSpacing(0)
        self.TopLayout.setObjectName("TopLayout")
        self.TitleLayout = QtWidgets.QVBoxLayout()
        self.TitleLayout.setContentsMargins(0, 0, 0, -1)
        self.TitleLayout.setSpacing(0)
        self.TitleLayout.setObjectName("TitleLayout")
        self.EZAudioLogo = QtWidgets.QLabel(self.centralwidget)
        self.EZAudioLogo.setMinimumSize(QtCore.QSize(20, 100))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.EZAudioLogo.setFont(font)
        self.EZAudioLogo.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.EZAudioLogo.setObjectName("EZAudioLogo")
        self.TitleLayout.addWidget(self.EZAudioLogo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TopLayout.addLayout(self.TitleLayout)
        self.QueueLayout = QtWidgets.QVBoxLayout()
        self.QueueLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.QueueLayout.setContentsMargins(0, 0, 0, 0)
        self.QueueLayout.setSpacing(0)
        self.QueueLayout.setObjectName("QueueLayout")
        self.LibraryButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.LibraryButton.setFont(font)
        self.LibraryButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 103, 103);")
        self.LibraryButton.setObjectName("LibraryButton")
        self.QueueLayout.addWidget(self.LibraryButton)
        self.QueueButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.QueueButton.setFont(font)
        self.QueueButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 103, 103);")
        self.QueueButton.setObjectName("QueueButton")
        self.QueueLayout.addWidget(self.QueueButton)
        self.TopLayout.addLayout(self.QueueLayout)
        self.TopLayout.setStretch(0, 1)
        self.PrimaryLayout.addLayout(self.TopLayout)
        self.BottomLayout = QtWidgets.QVBoxLayout()
        self.BottomLayout.setSpacing(30)
        self.BottomLayout.setObjectName("BottomLayout")
        self.ConvertLayout = QtWidgets.QHBoxLayout()
        self.ConvertLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.ConvertLayout.setContentsMargins(-1, -1, 0, 0)
        self.ConvertLayout.setSpacing(5)
        self.ConvertLayout.setObjectName("ConvertLayout")
        self.URLBox = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        self.URLBox.setFont(font)
        self.URLBox.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.URLBox.setObjectName("URLBox")
        self.ConvertLayout.addWidget(self.URLBox)
        self.ConvertButton = QtWidgets.QToolButton(self.centralwidget)
        self.ConvertButton.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setUnderline(False)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(103, 103, 103);")
        self.ConvertButton.setObjectName("ConvertButton")
        self.ConvertLayout.addWidget(self.ConvertButton)
        self.BottomLayout.addLayout(self.ConvertLayout)
        self.ErrorBox = QtWidgets.QLabel(self.centralwidget)
        self.ErrorBox.setMinimumSize(QtCore.QSize(361, 61))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        # self.ErrorBox.setFont(font)
        # self.ErrorBox.setStyleSheet("background-color: rgb(168, 168, 168);")
        # self.ErrorBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.ErrorBox.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.ErrorBox.setLineWidth(0)
        # self.ErrorBox.setMidLineWidth(0)
        # self.ErrorBox.setTextFormat(QtCore.Qt.AutoText)
        # self.ErrorBox.setScaledContents(False)
        # self.ErrorBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        # self.ErrorBox.setWordWrap(True)
        # self.ErrorBox.setObjectName("ErrorBox")
        self.BottomLayout.addWidget(self.ErrorBox)
        self.PrimaryLayout.addLayout(self.BottomLayout)
        self.horizontalLayout_3.addLayout(self.PrimaryLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.convert_Button = QPushButton('convert', MainWindow)
        self.convert_Button.resize(100, 49)
        self.convert_Button.move(2450, 200)
        self.convert_Button.setStyleSheet("background-color: white;")

        self.initUI()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def changeError(self):
        self.inputURL = self.URLBox.text()
        _translate = QtCore.QCoreApplication.translate
        self.ErrorBox.setText(_translate("MainWindow", "Hold on..."))
        conversionEngine.ytdlExec(self.inputURL)
        self.ErrorBox.setText(_translate("MainWindow", "Download done!"))

    def openLibrary(self):
        self.ex = List()
        self.ex.show()

    def openQueue(self): #Cloud Function
        self.cal = Window()
        self.cal.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EZ Audio"))
        self.URLBox.setText(_translate("MainWindow", self.defaultURL))
        self.EZAudioLogo.setText(_translate("MainWindow", "<html><head/><body><p>EZ Audio</p><p><span style=\" font-size:11pt;\">Made by Yousif, Omar, Jack, and Khaled</span></p></body></html>"))
        self.LibraryButton.setText(_translate("MainWindow", "Library"))
        self.QueueButton.setText(_translate("MainWindow", "Cloud"))
        self.ConvertButton.setText(_translate("MainWindow", "AddUrl"))
        # self.ErrorBox.setText(_translate("MainWindow", self.defaultError))
        # self.ConvertButton.clicked.connect(self.changeError)
        self.ConvertButton.clicked.connect(self.addUrl)
        self.URL_List.clicked.connect(self.removeURL)

        self.convert_Button.clicked.connect(self.covertURL)

        self.LibraryButton.clicked.connect(self.openLibrary)
        self.QueueButton.clicked.connect(self.openQueue)

    @pyqtSlot()
    def initUI(self):
        self.textbox = QLineEdit(MainWindow)
        self.textbox.move(1000, 200)
        self.textbox.resize(700, 200)
        self.textbox.setStyleSheet("background-color: red;")
        self.textbox.setText("To delete a URL double click on it")
        #self.textbox.fornt.setPointSize(50)

        self.URL_List = QListWidget(MainWindow)
        self.URL_List.move(1000, 350)
        self.URL_List.resize(700, 1500)
        self.URL_List.setStyleSheet("""QListWidget{ background: white; }""")

    def addUrl(self):
        textboxValue = self.URLBox.text()
        subString = textboxValue[0:23]
        print(subString)

        if subString == "https://www.youtube.com":
            self.URL_List.addItem(textboxValue)
        else:
            # self.message = QMessageBox(MainWindow)
            QMessageBox(MainWindow).question(MainWindow, 'Error', "The Url you entered is not a valid ",
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
            print(subString)


    def removeURL(self):
        index = self.URL_List.row(self.URL_List.currentItem())

        buttonReply = QMessageBox(MainWindow).question(MainWindow, 'Message', "Do you want to delete?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.URL_List.takeItem(index)
        else:
            return

    def covertURL(self):

        index = self.URL_List.item(0)
        if index is None:
            QMessageBox(MainWindow).question(MainWindow, 'Message', "No Url to convert ",
                                             QMessageBox.Ok,
                                             QMessageBox.Ok)
        else:
            while index is not None:
                print(self.URL_List.item(0).text())
                self.inputURL = self.URL_List.item(0).text()
                conversionEngine.ytdlExec(self.inputURL)
                self.URL_List.takeItem(0)
                index = self.URL_List.item(0)
            QMessageBox(MainWindow).question(MainWindow, 'Message', "All url have been converted ",
                                         QMessageBox.Ok,
                                         QMessageBox.Ok)

    # def converting(self):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
