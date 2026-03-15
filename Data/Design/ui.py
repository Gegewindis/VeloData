# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finished.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from Data.Scripts.own_widgets import DropFileLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 700))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QFrame(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMinimumSize(QSize(1200, 75))
        self.headerContainer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border-bottom: 1px solid rgb(255, 255, 255);\n"
"}")
        self.headerContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.appTitleLable = QLabel(self.headerContainer)
        self.appTitleLable.setObjectName(u"appTitleLable")
        self.appTitleLable.setMinimumSize(QSize(250, 50))
        font = QFont()
        font.setFamilies([u"Sylfaen"])
        font.setPointSize(36)
        font.setItalic(False)
        self.appTitleLable.setFont(font)
        self.appTitleLable.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"}")
        self.appTitleLable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.appTitleLable)

        self.horizontalSpacer = QSpacerItem(755, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.switchContainer = QFrame(self.headerContainer)
        self.switchContainer.setObjectName(u"switchContainer")
        self.switchContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	margin: 5px\n"
"}")
        self.switchContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.switchContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.switchContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recieverPushButton = QPushButton(self.switchContainer)
        self.recieverPushButton.setObjectName(u"recieverPushButton")
        self.recieverPushButton.setMinimumSize(QSize(75, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.recieverPushButton.setFont(font1)
        self.recieverPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.recieverPushButton)

        self.senderPushButton = QPushButton(self.switchContainer)
        self.senderPushButton.setObjectName(u"senderPushButton")
        self.senderPushButton.setMinimumSize(QSize(75, 50))
        self.senderPushButton.setFont(font1)
        self.senderPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.senderPushButton)


        self.horizontalLayout_5.addWidget(self.switchContainer)


        self.verticalLayout.addWidget(self.headerContainer)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.senderPage = QWidget()
        self.senderPage.setObjectName(u"senderPage")
        self.horizontalLayout_11 = QHBoxLayout(self.senderPage)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.menuContainer = QFrame(self.senderPage)
        self.menuContainer.setObjectName(u"menuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuContainer.sizePolicy().hasHeightForWidth())
        self.menuContainer.setSizePolicy(sizePolicy)
        self.menuContainer.setMinimumSize(QSize(250, 0))
        self.menuContainer.setMaximumSize(QSize(350, 16777215))
        self.menuContainer.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: none;\n"
"	margin: 0px;\n"
"}")
        self.menuContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.senderDestinationContainer = QFrame(self.menuContainer)
        self.senderDestinationContainer.setObjectName(u"senderDestinationContainer")
        self.senderDestinationContainer.setMinimumSize(QSize(0, 125))
        self.senderDestinationContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.senderDestinationContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.senderDestinationContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.senderDestinationContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.senderDestinationLabel = QLabel(self.senderDestinationContainer)
        self.senderDestinationLabel.setObjectName(u"senderDestinationLabel")
        font2 = QFont()
        font2.setPointSize(20)
        self.senderDestinationLabel.setFont(font2)
        self.senderDestinationLabel.setLineWidth(1)
        self.senderDestinationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.senderDestinationLabel)

        self.destinationLineEdit = QLineEdit(self.senderDestinationContainer)
        self.destinationLineEdit.setObjectName(u"destinationLineEdit")
        self.destinationLineEdit.setMinimumSize(QSize(190, 50))
        self.destinationLineEdit.setFont(font1)
        self.destinationLineEdit.setStyleSheet(u"QLineEdit {\n"
"	margin-right: 30px;\n"
"	margin-left: 30px;\n"
"}")

        self.verticalLayout_13.addWidget(self.destinationLineEdit)


        self.verticalLayout_12.addWidget(self.senderDestinationContainer)

        self.senderPortContainer = QFrame(self.menuContainer)
        self.senderPortContainer.setObjectName(u"senderPortContainer")
        self.senderPortContainer.setMinimumSize(QSize(0, 125))
        self.senderPortContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.senderPortContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.senderPortContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.senderPortContainer.setLineWidth(1)
        self.verticalLayout_14 = QVBoxLayout(self.senderPortContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.senderPortLabel = QLabel(self.senderPortContainer)
        self.senderPortLabel.setObjectName(u"senderPortLabel")
        self.senderPortLabel.setFont(font2)
        self.senderPortLabel.setLineWidth(1)
        self.senderPortLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.senderPortLabel)

        self.portLineEdit = QLineEdit(self.senderPortContainer)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setMinimumSize(QSize(190, 50))
        self.portLineEdit.setFont(font1)
        self.portLineEdit.setStyleSheet(u"QLineEdit {\n"
"	margin-right: 30px;\n"
"	margin-left: 30px;\n"
"}")
        self.portLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_14.addWidget(self.portLineEdit)


        self.verticalLayout_12.addWidget(self.senderPortContainer)

        self.menuSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.menuSpacer_4)

        self.connectContainer = QFrame(self.menuContainer)
        self.connectContainer.setObjectName(u"connectContainer")
        self.connectContainer.setMinimumSize(QSize(0, 100))
        self.connectContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connectContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.connectContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.connectContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.connectContainer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.connectPushButton = QPushButton(self.connectContainer)
        self.connectPushButton.setObjectName(u"connectPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connectPushButton.sizePolicy().hasHeightForWidth())
        self.connectPushButton.setSizePolicy(sizePolicy1)
        self.connectPushButton.setMinimumSize(QSize(150, 50))
        self.connectPushButton.setMaximumSize(QSize(140, 16777215))
        self.connectPushButton.setFont(font1)
        self.connectPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.connectPushButton)

        self.senderStatusContainer = QFrame(self.connectContainer)
        self.senderStatusContainer.setObjectName(u"senderStatusContainer")
        self.senderStatusContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.senderStatusContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.senderStatusContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.senderStatusContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.connectionStatusContainer = QWidget(self.senderStatusContainer)
        self.connectionStatusContainer.setObjectName(u"connectionStatusContainer")
        self.connectionStatusContainer.setMaximumSize(QSize(15, 15))
        self.connectionStatusContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.connectionStatusContainer.setAutoFillBackground(False)
        self.connectionStatusContainer.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 7px\n"
"}")

        self.horizontalLayout_6.addWidget(self.connectionStatusContainer)


        self.horizontalLayout_10.addWidget(self.senderStatusContainer)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_12.addWidget(self.connectContainer)


        self.horizontalLayout_11.addWidget(self.menuContainer)

        self.senderMainContainer = QFrame(self.senderPage)
        self.senderMainContainer.setObjectName(u"senderMainContainer")
        self.senderMainContainer.setMinimumSize(QSize(950, 625))
        self.senderMainContainer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.senderMainContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.senderMainContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.senderMainContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.errorPlainTextEdit = QPlainTextEdit(self.senderMainContainer)
        self.errorPlainTextEdit.setObjectName(u"errorPlainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.errorPlainTextEdit.sizePolicy().hasHeightForWidth())
        self.errorPlainTextEdit.setSizePolicy(sizePolicy2)
        self.errorPlainTextEdit.setMinimumSize(QSize(0, 100))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setItalic(True)
        self.errorPlainTextEdit.setFont(font3)
        self.errorPlainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	\n"
"	color: rgb(149, 0, 2)\n"
"}")
        self.errorPlainTextEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.errorPlainTextEdit.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.errorPlainTextEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 289, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.lowerMainContainer = QFrame(self.senderMainContainer)
        self.lowerMainContainer.setObjectName(u"lowerMainContainer")
        self.lowerMainContainer.setMinimumSize(QSize(950, 350))
        self.lowerMainContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.lowerMainContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.lowerMainContainer)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.dropFileContainer = QFrame(self.lowerMainContainer)
        self.dropFileContainer.setObjectName(u"dropFileContainer")
        self.dropFileContainer.setMinimumSize(QSize(600, 350))
        self.dropFileContainer.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.dropFileContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropFileContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dropFileContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 0, 30)
        self.dropOptionContainer = QFrame(self.dropFileContainer)
        self.dropOptionContainer.setObjectName(u"dropOptionContainer")
        self.dropOptionContainer.setMinimumSize(QSize(0, 50))
        self.dropOptionContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropOptionContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.dropOptionContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.browsePushButton = QPushButton(self.dropOptionContainer)
        self.browsePushButton.setObjectName(u"browsePushButton")
        self.browsePushButton.setMinimumSize(QSize(0, 45))
        self.browsePushButton.setFont(font1)
        self.browsePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.browsePushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.removePushButton = QPushButton(self.dropOptionContainer)
        self.removePushButton.setObjectName(u"removePushButton")
        self.removePushButton.setMinimumSize(QSize(0, 45))
        self.removePushButton.setFont(font1)
        self.removePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.removePushButton)

        self.removeComboBox = QComboBox(self.dropOptionContainer)
        self.removeComboBox.setObjectName(u"removeComboBox")
        self.removeComboBox.setMinimumSize(QSize(0, 45))
        self.removeComboBox.setMaximumSize(QSize(16777213, 16777215))
        self.removeComboBox.setFont(font1)
        self.removeComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.removeComboBox.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"    background-color: rgb(45, 45, 45);\n"
"}")

        self.horizontalLayout_2.addWidget(self.removeComboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 6)
        self.horizontalLayout_2.setStretch(4, 10)
        self.horizontalLayout_2.setStretch(5, 1)

        self.verticalLayout_3.addWidget(self.dropOptionContainer)

        self.dropFileLabel = DropFileLabel(self.dropFileContainer)
        self.dropFileLabel.setObjectName(u"dropFileLabel")
        font4 = QFont()
        font4.setPointSize(16)
        self.dropFileLabel.setFont(font4)
        self.dropFileLabel.setAutoFillBackground(False)
        self.dropFileLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.dropFileLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.dropFileLabel)

        self.verticalLayout_3.setStretch(1, 4)

        self.horizontalLayout_9.addWidget(self.dropFileContainer)

        self.addedFilesContainer = QFrame(self.lowerMainContainer)
        self.addedFilesContainer.setObjectName(u"addedFilesContainer")
        self.addedFilesContainer.setMinimumSize(QSize(350, 350))
        self.addedFilesContainer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.addedFilesContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.addedFilesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.addedFilesContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 30, 30, 20)
        self.addedFilesPlainTextEdit = QPlainTextEdit(self.addedFilesContainer)
        self.addedFilesPlainTextEdit.setObjectName(u"addedFilesPlainTextEdit")
        self.addedFilesPlainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: 1px solid rgb(45, 45, 45);\n"
"}")
        self.addedFilesPlainTextEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.addedFilesPlainTextEdit)

        self.sendContainer = QFrame(self.addedFilesContainer)
        self.sendContainer.setObjectName(u"sendContainer")
        self.sendContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.sendContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sendContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.sendPushButton = QPushButton(self.sendContainer)
        self.sendPushButton.setObjectName(u"sendPushButton")
        self.sendPushButton.setMinimumSize(QSize(0, 50))
        self.sendPushButton.setFont(font1)
        self.sendPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sendPushButton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.sendPushButton)

        self.percentCompletedLabel = QLabel(self.sendContainer)
        self.percentCompletedLabel.setObjectName(u"percentCompletedLabel")
        self.percentCompletedLabel.setFont(font1)
        self.percentCompletedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.percentCompletedLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 3)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout_4.addWidget(self.sendContainer)


        self.horizontalLayout_9.addWidget(self.addedFilesContainer)

        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_11.addWidget(self.lowerMainContainer)

        self.verticalLayout_11.setStretch(0, 2)
        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 4)

        self.horizontalLayout_11.addWidget(self.senderMainContainer)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 5)
        self.stackedWidget.addWidget(self.senderPage)
        self.recieverPage = QWidget()
        self.recieverPage.setObjectName(u"recieverPage")
        self.horizontalLayout = QHBoxLayout(self.recieverPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.recieverMenuContainer = QFrame(self.recieverPage)
        self.recieverMenuContainer.setObjectName(u"recieverMenuContainer")
        sizePolicy.setHeightForWidth(self.recieverMenuContainer.sizePolicy().hasHeightForWidth())
        self.recieverMenuContainer.setSizePolicy(sizePolicy)
        self.recieverMenuContainer.setMinimumSize(QSize(250, 0))
        self.recieverMenuContainer.setMaximumSize(QSize(350, 16777215))
        self.recieverMenuContainer.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border: none;\n"
"	margin: 0px;\n"
"}")
        self.recieverMenuContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.recieverMenuContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.recieverMenuContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.recieverDestinationContainer = QFrame(self.recieverMenuContainer)
        self.recieverDestinationContainer.setObjectName(u"recieverDestinationContainer")
        self.recieverDestinationContainer.setMinimumSize(QSize(0, 125))
        self.recieverDestinationContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.recieverDestinationContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.recieverDestinationContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.recieverDestinationContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.recieverDestinationLabel = QLabel(self.recieverDestinationContainer)
        self.recieverDestinationLabel.setObjectName(u"recieverDestinationLabel")
        self.recieverDestinationLabel.setFont(font2)
        self.recieverDestinationLabel.setLineWidth(1)
        self.recieverDestinationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.recieverDestinationLabel)

        self.usingIPLabel = QLabel(self.recieverDestinationContainer)
        self.usingIPLabel.setObjectName(u"usingIPLabel")
        self.usingIPLabel.setFont(font4)
        self.usingIPLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 25px;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}")
        self.usingIPLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.usingIPLabel)


        self.verticalLayout_15.addWidget(self.recieverDestinationContainer)

        self.recieverPortContainer = QFrame(self.recieverMenuContainer)
        self.recieverPortContainer.setObjectName(u"recieverPortContainer")
        self.recieverPortContainer.setMinimumSize(QSize(0, 125))
        self.recieverPortContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.recieverPortContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.recieverPortContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.recieverPortContainer.setLineWidth(1)
        self.verticalLayout_17 = QVBoxLayout(self.recieverPortContainer)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.recieverPortLabel = QLabel(self.recieverPortContainer)
        self.recieverPortLabel.setObjectName(u"recieverPortLabel")
        self.recieverPortLabel.setFont(font2)
        self.recieverPortLabel.setLineWidth(1)
        self.recieverPortLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.recieverPortLabel)

        self.usingPortLabel = QLabel(self.recieverPortContainer)
        self.usingPortLabel.setObjectName(u"usingPortLabel")
        self.usingPortLabel.setFont(font4)
        self.usingPortLabel.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border-radius: 25px;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}")
        self.usingPortLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.usingPortLabel)


        self.verticalLayout_15.addWidget(self.recieverPortContainer)

        self.menuSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.menuSpacer_5)

        self.StartContainer = QFrame(self.recieverMenuContainer)
        self.StartContainer.setObjectName(u"StartContainer")
        self.StartContainer.setMinimumSize(QSize(0, 100))
        self.StartContainer.setMaximumSize(QSize(16777215, 16777215))
        self.StartContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.StartContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.StartContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.StartContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.StartContainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.startPushButton = QPushButton(self.StartContainer)
        self.startPushButton.setObjectName(u"startPushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.startPushButton.sizePolicy().hasHeightForWidth())
        self.startPushButton.setSizePolicy(sizePolicy3)
        self.startPushButton.setMinimumSize(QSize(150, 50))
        self.startPushButton.setMaximumSize(QSize(150, 16777215))
        self.startPushButton.setFont(font1)
        self.startPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.startPushButton.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.startPushButton)

        self.recieverStatusContainer = QFrame(self.StartContainer)
        self.recieverStatusContainer.setObjectName(u"recieverStatusContainer")
        self.recieverStatusContainer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.recieverStatusContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.recieverStatusContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.recieverStatusContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 9, 9, 9)
        self.StartStatusContainer = QWidget(self.recieverStatusContainer)
        self.StartStatusContainer.setObjectName(u"StartStatusContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.StartStatusContainer.sizePolicy().hasHeightForWidth())
        self.StartStatusContainer.setSizePolicy(sizePolicy4)
        self.StartStatusContainer.setMaximumSize(QSize(15, 15))
        self.StartStatusContainer.setAutoFillBackground(False)
        self.StartStatusContainer.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 7px\n"
"}")

        self.horizontalLayout_7.addWidget(self.StartStatusContainer)


        self.horizontalLayout_12.addWidget(self.recieverStatusContainer)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_15.addWidget(self.StartContainer)


        self.horizontalLayout.addWidget(self.recieverMenuContainer)

        self.mainDownloadedContainer = QFrame(self.recieverPage)
        self.mainDownloadedContainer.setObjectName(u"mainDownloadedContainer")
        sizePolicy.setHeightForWidth(self.mainDownloadedContainer.sizePolicy().hasHeightForWidth())
        self.mainDownloadedContainer.setSizePolicy(sizePolicy)
        self.mainDownloadedContainer.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}")
        self.mainDownloadedContainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainDownloadedContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainDownloadedContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.downloadedLabel = QLabel(self.mainDownloadedContainer)
        self.downloadedLabel.setObjectName(u"downloadedLabel")
        font5 = QFont()
        font5.setPointSize(24)
        self.downloadedLabel.setFont(font5)
        self.downloadedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.downloadedLabel)


        self.horizontalLayout.addWidget(self.mainDownloadedContainer)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.stackedWidget.addWidget(self.recieverPage)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appTitleLable.setText(QCoreApplication.translate("MainWindow", u"Velodata", None))
        self.recieverPushButton.setText(QCoreApplication.translate("MainWindow", u"Reciever", None))
        self.senderPushButton.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.senderDestinationLabel.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.destinationLineEdit.setText("")
        self.destinationLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"192.168.x.x / domain.com", None))
        self.senderPortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.portLineEdit.setText("")
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recieving port", None))
        self.connectPushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.errorPlainTextEdit.setPlainText("")
        self.browsePushButton.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.removePushButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.dropFileLabel.setText(QCoreApplication.translate("MainWindow", u"Drop Files Here", None))
        self.addedFilesPlainTextEdit.setPlainText("")
        self.sendPushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.percentCompletedLabel.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.recieverDestinationLabel.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.usingIPLabel.setText(QCoreApplication.translate("MainWindow", u"IP: 192.168.x.x", None))
        self.recieverPortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.usingPortLabel.setText(QCoreApplication.translate("MainWindow", u"Using Port: -", None))
        self.startPushButton.setText(QCoreApplication.translate("MainWindow", u"Start reciever", None))
        self.downloadedLabel.setText(QCoreApplication.translate("MainWindow", u"KB Recieved: 0", None))
    # retranslateUi

