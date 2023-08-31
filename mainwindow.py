# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(494, 447)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(98, 160, 234);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 60, 281, 321))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 309, 352))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 20)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../Downloads/200.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.txtEmail = QLineEdit(self.verticalLayoutWidget_2)
        self.txtEmail.setObjectName(u"txtEmail")

        self.horizontalLayout_3.addWidget(self.txtEmail)

        self.horizontalLayout_3.setStretch(0, 50)
        self.horizontalLayout_3.setStretch(1, 50)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.txtPassword = QLineEdit(self.verticalLayoutWidget_2)
        self.txtPassword.setObjectName(u"txtPassword")

        self.horizontalLayout.addWidget(self.txtPassword)

        self.horizontalLayout.setStretch(0, 50)
        self.horizontalLayout.setStretch(1, 50)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_7.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.commandLinkButton = QCommandLinkButton(self.verticalLayoutWidget_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.horizontalLayout_7.addWidget(self.commandLinkButton)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.btnLogin = QPushButton(self.verticalLayoutWidget_2)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.btnLogin)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Remember Me", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

