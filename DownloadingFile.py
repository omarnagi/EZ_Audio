from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QListWidget
from PyQt5.QtCore import pyqtSlot


class DownLoadFile(QMainWindow):

    @pyqtSlot()
    def downloadFile(self):

        # Call the Drive v3 API
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        else:
            QMessageBox.question(self, 'Error', "Connect to google drive first ", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

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