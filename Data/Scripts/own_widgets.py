from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal
import os
import shutil

class DropFileLabel(QLabel):
    fileDropped = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setText("Drop Files Here")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event): # Does not check for already existing
        for url in event.mimeData().urls():
            filePath = url.toLocalFile()
            fileName = os.path.basename(filePath)

            if fileName not in os.listdir("Sending_files/"):
                shutil.copy(filePath, f"Sending_files/{fileName}")
                self.fileDropped.emit(fileName)