


# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from httplib2 import Http
# from apiclient.http import MediaFileUpload,MediaIoBaseDownload
#
# from oauth2client import file, client, tools

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtCore import pyqtSlot



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']



class Features(QMainWindow):

    @pyqtSlot()
    def __init__(self):
        super().__init__()
        self.title = 'Google Drive Connection'
        self.left = 1000
        self.top = 1000
        self.width = 1000
        self.height = 5000
        self.initUI()

    @pyqtSlot()
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet("""QMainWindow{ background: yellow; }""")

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Add URL', self)
        self.button.move(20, 80)

        self.listwidget = QListWidget(self)
        self.listwidget.move(200, 200)
        self.listwidget.resize(1000, 1000)
        self.setStyleSheet("""QListWidget{ background: green; }""")
        # self.listwidget.Add

        #goolle coneect

        self.btn = QPushButton('Connect To Google Drive', self)
        self.btn.resize(289,49)
        self.btn.move(1000, 50)



        self.button3 = QPushButton('Download', self)
        self.button3.resize(289,49)
        self.button3.move(1500, 50)

        self.button4 = QPushButton('Upload', self)
        self.button4.resize(289,49)
        self.button4.move(90, 200)

        self.button5 = QPushButton('Sign out', self)
        self.button5.resize(289, 49)
        self.button5.move(500, 50)


        # connect button to function on_click
        self.button.clicked.connect(self.addUrl)
        self.listwidget.clicked.connect(self.removeURL)
        self.btn.clicked.connect(self.auth)

        self.button3.clicked.connect(self.downloadFile)
        #self.button4.clicked.connect(self.uploadFile)
        self.button5.clicked.connect(self.signOut)
        return 1



    def addUrl(self):
        textboxValue = self
        subString = textboxValue[0:23]
        print(subString)

        if subString == 'https://www.youtube.com':
            #self.listwidget.addItem(textboxValue)
            return 1
        else:
            QMessageBox.question(self, 'Error', "The Url you entered is not a valid ", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return 0

    def removeURL(self):
        #index = self.listwidget.row(self.listwidget.currentItem())
        #self.listwidget.takeItem(index)
        index = self

        if index > 0:
         return 1
        else:
            return 0


    @pyqtSlot()
    def downloadFile(self):

        # Call the Drive v3 API
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
                return 1
        else:
            QMessageBox.question(self, 'Error', "Connect to google drive first ", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return 0

        service = build('drive', 'v3', credentials=creds)
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

    # @pyqtSlot()
    # def uploadFile(self):
    #
    #     # Setup the Drive v3 API
    #     SCOPES = 'https://www.googleapis.com/auth/drive.file'
    #     store = file.Storage('token.pickle')
    #     creds = store.get()
    #     if not creds or creds.invalid:
    #         flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    #         creds = tools.run_flow(flow, store)
    #     drive_service = build('drive', 'v3', http=creds.authorize(Http()))
    #
    #     file_metadata = {
    #         'name': 'photo.jpg',
    #         'mimeType': '*/*'
    #     }
    #
    #     media = MediaFileUpload('photo.jpg',
    #                             mimetype='*/*',
    #                             resumable=True)
    #     file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    #
    #     print('File ID: ' + file.get('id'))


        # print("itsworokg")
        #
        # creds = None
        # if os.path.exists('token.pickle'):
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        #         print("itsworokg")
        # else:
        #     QMessageBox.question(self, 'Error', "Connect to google drive first ", QMessageBox.Ok,
        #                          QMessageBox.Ok)
        #     return
        #
        # service = build('drive', 'v3', http = creds.authorize(Http()))
        #
        # #service = build('drive', 'v3', credentials=creds)
        #
        # file_metadata = {'name': 'photo.jpg'}
        # media = MediaFileUpload('photo.jpg',
        #                         mimetype='image/jpeg')
        # file = service.files().create(body=file_metadata,
        #                                     media_body=media).execute()
        # print( 'File ID: %s' % file.get('id'))



    def signOut(self):
        # if os.path.exists('token.pickle'):
        #     # self.buttonReply = QMessageBox.question(self, 'Message', "Do you do u want to sign out ?",
        #     #                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #     replay = 0
        #     if self.buttonReply == QMessageBox.Yes:
        #         os.remove("token.pickle")
        #         QMessageBox.question(self, 'Message', "Now you are signd out", QMessageBox.Ok,
        #                              QMessageBox.Ok)
        #
        # else:
        #     QMessageBox.question(self, 'Message', "you are not connected to any google drive", QMessageBox.Ok,
        #                          QMessageBox.Ok)
        #     m = 1
        replay = self
        if replay == "yes":
            return 1
        else:
            return 0


    @pyqtSlot()
    def auth(self):

        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        if os.path.exists('token.pickle'):
            #self.on_click()
            return 1
        else:
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('drive', 'v3', credentials=creds)
            self.AuthMessage()
            return 0



    @pyqtSlot()
    def on_click(self):
        QMessageBox.question(self, 'Message', "You are already connected" , QMessageBox.Ok,
                             QMessageBox.Ok)

    # @pyqtSlot()
    def AuthMessage(self):
        # QMessageBox.question(self, 'Message', "The connection was successfully done" , QMessageBox.Ok,
        #                      QMessageBox.Ok)
        mess = self
        if mess == "show":
            return 1
        else:
            return 0
    @pyqtSlot()
    def of_click(self):
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " , QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Features()
    ex.show()
    sys.exit(app.exec_())

