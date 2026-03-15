import Data.Scripts.socket_logic as sk
import os
import shutil

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIcon
from Data.Design.ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("VeloData")
        self.setWindowIcon(QIcon("Data/Images/icon.png"))

        # Reciever
        self.recieverSocket = None
        self.recieverThread = None

        # Sender
        self.senderSocket = None
        self.senderThread = None

        # Other attributes
        self.downloaded = 0

        # Button Events
        self.ui.senderPushButton.clicked.connect(self.senderPushButton_callback)
        self.ui.recieverPushButton.clicked.connect(self.recieverPushButton_callback)
        self.ui.removePushButton.clicked.connect(self.removePushButton_callback)
        self.ui.browsePushButton.clicked.connect(self.browsePushButton_callback)
        self.ui.sendPushButton.clicked.connect(self.sendPushButton_callback)
        self.ui.connectPushButton.clicked.connect(self.connectPushButton_callback)
        self.ui.startPushButton.clicked.connect(self.startPushButton_callback)

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
        if self.senderSocket:
            # Reset
            self.senderSocket.close()
            self.senderSocket = None

            # UI reset
            self.set_sender_status("red")
            self.ui.connectPushButton.setText("Connect")
            self.ui.recieverPushButton.setEnabled(True)
            return
        
        # Disables swtiching page
        self.ui.recieverPushButton.setEnabled(False)

        # Error check
        if (hostname := self.ui.destinationLineEdit.text()) == "":
            self.ui.senderInfoPlainTextEdit.setPlainText("Please fill out the 'destination' field!")
            self.ui.recieverPushButton.setEnabled(True)
            return
        if (port := self.ui.portLineEdit.text()) == "":
            self.ui.senderInfoPlainTextEdit.setPlainText("Please fill out the 'port' field!")
            self.ui.recieverPushButton.setEnabled(True)
            return
        
        # Tries connecting
        self.set_sender_status("orange")
        self.senderSocket = sk.senderConnect(hostname, int(port))

        if self.senderSocket:
            # UI changes
            self.ui.senderInfoPlainTextEdit.setPlainText("")
            self.ui.connectPushButton.setText("Disconnect")
            self.set_sender_status("green")

        else:
            #UI changes
            self.ui.senderInfoPlainTextEdit.setPlainText("Connection failed, make sure to have the right IP address and port that the reciever uses.\n\nKeep in mind the the current version can only handle datatransfers on the same local network!")
            self.set_sender_status("red")

            # Emable page switch in case of fail
            self.ui.recieverDestinationContainer.setEnabled(True)

    def sendPushButton_callback(self):
        if not self.senderSocket:
            return
        self.ui.sendPushButton.setEnabled(False)
        self.senderThread = sk.SenderThread(self.senderSocket)
        self.senderThread.removeFile.connect(self.remove_file)
        self.senderThread.sentProgress.connect(self.set_sent_progress)
        self.senderThread.sentStatus.connect(self.set_sender_status)
        self.senderThread.finished.connect(lambda: self.ui.sendPushButton.setEnabled(True))
        self.senderThread.start()

    def startPushButton_callback(self):
        if self.recieverSocket:
            self.recieverThread.stop()
            self.recieverThread.wait()
            self.recieverThread = None

            self.recieverSocket.close()
            self.recieverSocket = None

            self.set_reciever_status("red")
            self.ui.usingPortLabel.setText(f"Using Port: -")
            self.ui.startPushButton.setText("Start reciever")

            self.ui.senderPushButton.setEnabled(True)
            return
        
        # Disable page switching
        self.ui.senderPushButton.setEnabled(False)

        # Setup
        self.recieverSocket, recieverPort = sk.setUpReciever()

        # Update UI
        self.ui.usingPortLabel.setText(f"Using Port: {str(recieverPort)}")
        self.set_reciever_status("orange")
        self.ui.startPushButton.setText("Stop reciever")

        # Reciever thread
        self.recieverThread = sk.RecieverThread(self.recieverSocket)
        self.recieverThread.statusFunc.connect(self.set_reciever_status)
        self.recieverThread.downloadFunc.connect(self.set_downloaded)
        self.recieverThread.start()

    # UI update methods
    def set_reciever_status(self, color: str) -> None:
        self.ui.StartStatusContainer.setStyleSheet("QWidget {\nbackground-color: " + color + ";\nborder-radius: 7px\n}")

    def set_sender_status(self, color: str) -> None:
        self.ui.connectionStatusContainer.setStyleSheet("QWidget {\nbackground-color:" + color + ";\nborder-radius: 7px\n}")
    
    def set_sent_progress(self, progress: str) -> None:
        self.ui.percentCompletedLabel.setText(progress)

    def set_downloaded(self, amount: int):
        self.downloaded += amount

        if self.downloaded < 1000:
            self.ui.downloadedLabel.setText(f"KB Recieved: {self.downloaded}")
        elif self.downloaded < 1000000:
            self.ui.downloadedLabel.setText(f"MB Recieved: {int(self.downloaded/1000)}")
        else:
            self.ui.downloadedLabel.setText(f"GB Recieved: {int(self.downloaded/1000000)}")

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
            window.recieverThread.stop()
            window.recieverThread.wait()

        if window.senderThread:
            window.senderThread.wait()

        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()