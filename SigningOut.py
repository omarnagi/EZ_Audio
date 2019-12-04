

from __future__ import print_function
import os.path
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class SigningOut(QMainWindow):
    def signOut(self):
        print("out")
        if os.path.exists('token.pickle'):
            buttonReply = QMessageBox.question(self, 'Message', "Do you do u want to sign out ?",
                                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                os.remove("token.pickle")
                QMessageBox.question(self, 'Message', "Now you are signd out", QMessageBox.Ok,
                                QMessageBox.Ok)
            return 1

        else:
            QMessageBox.question(self, 'Message', "you are not connected to any google drive", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return 0
