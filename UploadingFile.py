from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtCore import pyqtSlot


class UploadingFile(QMainWindow):

    @pyqtSlot()
    def uploadFile(self):

        # Setup the Drive v3 API
        SCOPES = 'https://www.googleapis.com/auth/drive.file'
        store = file.Storage('token.pickle')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        drive_service = build('drive', 'v3', http=creds.authorize(Http()))

        file_metadata = {
            'name': 'photo.jpg',
            'mimeType': '*/*'
        }

        media = MediaFileUpload('photo.jpg',
                                mimetype='*/*',
                                resumable=True)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print('File ID: ' + file.get('id'))