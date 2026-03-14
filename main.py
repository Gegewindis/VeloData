import Data.Scripts.socket_logic as sk
import os
import shutil

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from Data.Design.ui_app import Ui_MainWindow

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
        self.senderThread = None

        self.recieving = False
        self.sending = False

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

    # Callback methods
    def senderPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def recieverPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def removePushButton_callback(self):
        fileName = self.ui.removeComboBox.currentText()
        self.remove_file(fileName)
        
    def browsePushButton_callback(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Select File")
        if filePath:
            fileName = os.path.basename(filePath)
            shutil.copy(filePath, f"Sending_files/{fileName}")

            self.ui.removeComboBox.addItem(fileName)
            self.ui.addedFilesPlainTextEdit.insertPlainText(fileName + "\n")

    def connectPushButton_callback(self):
        if self.sending:
            self.senderSocket.close()
            self.senderSocket = None
            self.sender_set_status("red")
            self.sending = False
            return

        self.sender_set_status("orange")
        self.senderSocket = sk.senderConnect(self.ui.destinationLineEdit.text(), int(self.ui.portLineEdit.text()))
        if self.senderSocket:
            self.sender_set_status("green")
            self.ui.connectPushButton.setText("Disconnect")
            self.sending = True
        else:
            self.sender_set_status("red")

    def sendPushButton_callback(self):
        self.senderThread = sk.SenderThread(self.senderSocket)
        self.senderThread.removeFile.connect(self.remove_file)
        self.senderThread.sentProgress.connect(self.sent_set_progress)
        self.senderThread.sentStatus.connect(self.sender_set_status)
        self.senderThread.start()

    def StartPushButton_callback(self):
        if self.recieving:
            self.recieverSocket.close()
            self.recieverSocket = None
            self.recieverPort = None
            self.reciever_set_status("red")
            self.ui.usingPortLabel.setText(f"Using Port: -")
            self.ui.startPushButton.setText("Start reciever")
            self.recieving = False
            self.recieverThread.quit()
            self.recieverThread = None
            return
        
        # Setup
        self.recieving = True
        self.recieverSocket, self.recieverPort = sk.setUpReciever()

        # Update UI
        self.ui.usingPortLabel.setText(f"Using Port: {str(self.recieverPort)}")
        self.reciever_set_status("orange")
        self.ui.startPushButton.setText("Stop reciever")

        # Reciever thread
        self.recieverThread = sk.RecieverThread(self.recieverSocket)
        self.recieverThread.statusFunc.connect(self.reciever_set_status)
        self.recieverThread.start()

    # Other methods
    def remove_file(self, fileName: str) -> None:
        # Removes it from the folder
        os.remove(f"Sending_files/{fileName}")

        # Removes the selected comboBox alternative
        self.ui.removeComboBox.removeItem(self.ui.removeComboBox.findText(fileName))

        # Removes the file from the plainTextEdit
        plainText = self.ui.addedFilesPlainTextEdit.toPlainText()
        plainText = plainText.split("\n")
        plainText.remove(fileName)
        plainText = "\n".join(plainText)
        self.ui.addedFilesPlainTextEdit.setPlainText(plainText)

    def reciever_set_status(self, color: str) -> None:
        self.ui.StartStatusContainer.setStyleSheet("QWidget {\nbackground-color: " + color + ";\nborder-radius: 7px\n}")
    
    def sent_set_progress(self, num: int) -> None:
        self.ui.percentCompletedLabel.setText(f"{num}%")

    def sender_set_status(self, color: str) -> None:
        self.ui.connectionStatusContainer.setStyleSheet("QWidget {\nbackground-color:" + color + ";\nborder-radius: 7px\n}")

    def on_dropped_file(self, fileName: str) -> None:
        self.ui.removeComboBox.addItem(fileName)
        self.ui.addedFilesPlainTextEdit.insertPlainText(fileName + "\n")

    # Cleanup method
    def closeEvent(self, event):
        for fileName in os.listdir("Sending_files/"):
            if fileName != ".gitkeep":
                os.remove(f"Sending_files/{fileName}")

        if window.senderSocket:
            window.senderSocket.close()

        if window.recieverSocket:
            window.recieverSocket.close()

        if window.recieverThread:
            window.recieverThread.quit()
            window.recieverThread.wait()

        if window.senderThread:
            window.senderThread.quit()
            window.senderThread.wait()


        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()