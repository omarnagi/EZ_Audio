from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtCore import pyqtSlot

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

class Authorization(QMainWindow):

    @pyqtSlot()
    def authorization(self):

        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        if os.path.exists('token.pickle'):
            self.on_click()
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

    @pyqtSlot()
    def on_click(self):
        QMessageBox.question(self, 'Message', "You are already connected" , QMessageBox.Ok,
                             QMessageBox.Ok)
    @pyqtSlot()
    def AuthMessage(self):
        QMessageBox.question(self, 'Message', "The connection was successfully done" , QMessageBox.Ok,
                             QMessageBox.Ok)
    @pyqtSlot()
    def of_click(self):
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " , QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Authorization()
#     ex.show()
#     sys.exit(app.exec_())