from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QListWidget,QMessageBox
from PyQt5.QtCore import pyqtSlot
from GoogleAuthorization import Authorization
from SigningOut import  SigningOut
from DownloadingFile import DownLoadFile
from UploadingFile import UploadingFile


# from AddingURL import AddingURL

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

class Window(QMainWindow):

    @pyqtSlot()
    def __init__(self):
        super().__init__()
        self.title = 'Google Drive Connection'
        self.left = 0
        self.top = 0
        self.width = 10000
        self.height = 20000
        self.initUI()

    @pyqtSlot()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: gray;")

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        self.textbox.setStyleSheet("background-color: white;")

        # Create a button in the window
        self.add_URL_button = QPushButton('Add URL', self)
        self.add_URL_button.move(20, 80)
        self.add_URL_button.resize(289, 49)
        self.add_URL_button.setStyleSheet("background-color: white;")

        # self.textboxValue1 = "ssss"
        # self.adding = AddingURL()
        # self.adding.addUrl(self.textboxValue1, self.URL_List)
        #self.add_URL_button.clicked.connect(self.adding.addUrl("ddj"))

        self.add_URL_button.clicked.connect(self.addUrl)


        self.URL_List = QListWidget(self)
        self.URL_List.move(0, 200)
        self.URL_List.resize(700, 1000)
        self.URL_List.setStyleSheet("""QListWidget{ background: white; }""")
        # self.URL_List.



        # goolle coneect
        self.Connect_button = QPushButton('Connect To Google Drive', self)
        self.Connect_button.resize(289, 49)
        self.Connect_button.move(1000, 50)
        self.Connect_button.setStyleSheet("background-color: white;")

        self.auth = Authorization()
        self.Connect_button.clicked.connect(self.auth.authorization)


        self.Download_button = QPushButton('Download', self)
        self.Download_button.resize(289, 49)
        self.Download_button.move(1500, 50)
        self.Download_button.setStyleSheet("background-color: white;")

        self.download = DownLoadFile()
        self.Download_button.clicked.connect(self.download.downloadFile)

        self.Upload_button = QPushButton('Upload', self)
        self.Upload_button.resize(289, 49)
        self.Upload_button.move(2000, 50)
        self.Upload_button.setStyleSheet("background-color: white;")


        self.upload = UploadingFile()
        self.Upload_button.clicked.connect(self.upload.uploadFile)

        self.Sign_Out_button = QPushButton('Sign out', self)
        self.Sign_Out_button.resize(289, 49)
        self.Sign_Out_button.move(500, 50)
        self.Sign_Out_button.setStyleSheet("background-color: white;")

        self.out = SigningOut()
        self.Sign_Out_button.clicked.connect(self.out.signOut)

        self.URL_List.clicked.connect(self.removeURL)

    def addUrl(self):
        textboxValue = self.textbox.text()
        subString = textboxValue[0:23]
        print(subString)

        if subString == "https://www.youtube.com":
            self.URL_List.addItem(textboxValue)
        else:
            QMessageBox.question(self, 'Error', "The Url you entered is not a valid ", QMessageBox.Ok,
                                 QMessageBox.Ok)


    def removeURL(self):
        index = self.URL_List.row(self.URL_List.currentItem())

        buttonReply = QMessageBox.question(self, 'Message', "Do you want to delete?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.URL_List.takeItem(index)
        else:
            return




