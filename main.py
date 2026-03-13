import Data.Scripts.socket_logic as sk
import os
import shutil

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon
from ui_app import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("VeloData")
        self.setWindowIcon(QIcon("Data/Images/icon.png"))

        self.senderSocket = None
        self.recieverPort = None
        self.recieverSocket = None
        self.recieverThread = None

        self.recieving = False
        self.sedning = False

        # Button Events
        self.ui.senderPushButton.clicked.connect(self.senderPushButton_callback)
        self.ui.recieverPushButton.clicked.connect(self.recieverPushButton_callback)
        self.ui.removePushButton.clicked.connect(self.removePushButton_callback)
        self.ui.browsePushButton.clicked.connect(self.browsePushButton_callback)
        self.ui.sendPushButton.clicked.connect(self.sendPushButton_callback)
        self.ui.connectPushButton.clicked.connect(self.connectPushButton_callback)
        self.ui.startPushButton.clicked.connect(self.StartPushButton_callback)

        # Labels
        self.ui.usingIPLabel.setText(f"IP: {sk.getUserIp()}")
        self.ui.dropFileLabel.fileDropped.connect(self.on_dropped_file)

    def senderPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def recieverPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def removePushButton_callback(self):
        comboBox = self.ui.removeComboBox
        plainTextEdit = self.ui.addedFilesPlainTextEdit

        fileName = comboBox.currentText()
        comboBox.removeItem(comboBox.findText(fileName))
        
        plainText = plainTextEdit.toPlainText()
        plainText = plainText.split("\n")
        plainText.remove(fileName)
        plainText = "\n".join(plainText)
        plainTextEdit.setPlainText(plainText)

        os.remove(f"Sending_files/{fileName}")

    def on_dropped_file(self, fileName):
        self.ui.removeComboBox.addItem(fileName)
        self.ui.addedFilesPlainTextEdit.insertPlainText(fileName + "\n")

    def browsePushButton_callback(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Select File")
        if filePath:
            fileName = os.path.basename(filePath)
            shutil.copy(filePath, f"Sending_files/{fileName}")

            self.ui.removeComboBox.addItem(fileName)
            self.ui.addedFilesPlainTextEdit.insertPlainText(fileName + "\n")

    def connectPushButton_callback(self):
        self.ui.connectionStatusContainer.setStyleSheet("QWidget {\nbackground-color: orange;\nborder-radius: 7px\n}")

        self.senderSocket = sk.senderConnect(self.ui.destinationLineEdit.text(), self.ui.portLineEdit.text())
        if self.senderSocket:
            self.ui.connectionStatusContainer.setStyleSheet("QWidget {\nbackground-color: rgb(0, 255, 0);\nborder-radius: 7px\n}")
        else:
            self.ui.connectionStatusContainer.setStyleSheet("QWidget {\nbackground-color: rgb(255, 0, 0);\nborder-radius: 7px\n}")

    def sendPushButton_callback(self):
        sk.sendFiles(self.senderSocket, fileSent=self.file_sent)

    def file_sent(self, fileName):
        comboBox = self.ui.removeComboBox
        plainTextEdit = self.ui.addedFilesPlainTextEdit

        comboBox.removeItem(comboBox.findText(fileName))
        
        plainText = plainTextEdit.toPlainText()
        plainText = plainText.split("\n")
        plainText.remove(fileName)
        plainText = "\n".join(plainText)
        plainTextEdit.setPlainText(plainText)

    def StartPushButton_callback(self):
        if self.recieving:
            self.recieverSocket.close()
            self.recieverPort = None
            self.ui.StartStatusContainer.setStyleSheet("QWidget {\nbackground-color: rgb(255, 0, 0);\nborder-radius: 7px\n}")
            self.ui.usingPortLabel.setText(f"Using Port: -")
            self.ui.startPushButton.setText("Start reciever")
            self.recieving = False
            self.recieverThread.quit()
            self.recieverThread = None
            return
        
        self.recieving = True
        self.recieverSocket, self.recieverPort = sk.setUpReciever()

        # Update UI
        self.ui.usingPortLabel.setText(f"Using Port: {str(self.recieverPort)}")
        self.ui.StartStatusContainer.setStyleSheet("QWidget {\nbackground-color: orange;\nborder-radius: 7px\n}")
        self.ui.startPushButton.setText("Stop reciever")

        self.recieverThread = sk.RecieverThread(self.recieverSocket)





if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

    for file in os.listdir("Sending_files/"):
        os.remove(f"Sending_files/{file}")

    if window.senderSocket:
        window.senderSocket.close()

    if window.recieverSocket:
        window.recieverSocket.close()
    if window.recieverThread:
        window.recieverThread.quit()