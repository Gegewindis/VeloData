import Data.Scripts.socket_logic as sk

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from ui_app import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("VeloData")
        self.setWindowIcon(QIcon("Data/Images/icon.png"))

        # Button Events
        self.ui.senderPushButton.clicked.connect(self.senderPushButton_callback)
        self.ui.recieverPushButton.clicked.connect(self.recieverPushButton_callback)

        # Labels
        self.ui.usingIPLabel.setText(sk.getUserIp())

    def senderPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def recieverPushButton_callback(self):
        self.ui.stackedWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()