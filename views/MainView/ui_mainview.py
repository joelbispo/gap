# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1318, 839)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: rgb(255, 255, 255);\n"
" }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.swMain = QStackedWidget(self.centralwidget)
        self.swMain.setObjectName(u"swMain")
        self.swMain.setLayoutDirection(Qt.LeftToRight)
        self.swMain.setAutoFillBackground(False)
        self.swMain.setStyleSheet(u"background-color:  rgb(255, 255, 255);")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.frame = QFrame(self.main)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(186, 224, 371, 288))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(371, 288))
        self.frame.setMaximumSize(QSize(371, 288))
        self.frame.setSizeIncrement(QSize(2, 2))
        self.frame.setStyleSheet(u"padding: 3px;\n"
"border-color: rgb(255, 85, 0);\n"
"border-top-color: rgb(255, 0, 0);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.btnResearcher = QPushButton(self.frame)
        self.btnResearcher.setObjectName(u"btnResearcher")
        self.btnResearcher.setMinimumSize(QSize(220, 71))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(20)
        self.btnResearcher.setFont(font)
        self.btnResearcher.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(94, 184, 255);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"gridline-color:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 91, 159);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.btnResearcher, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(740, 224, 371, 288))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(371, 288))
        self.frame_2.setMaximumSize(QSize(800, 600))
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setStyleSheet(u"padding: 3px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.btnParticipant = QPushButton(self.frame_2)
        self.btnParticipant.setObjectName(u"btnParticipant")
        self.btnParticipant.setMinimumSize(QSize(220, 71))
        self.btnParticipant.setFont(font)
        self.btnParticipant.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(94, 184, 255);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"gridline-color:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 91, 159);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.btnParticipant, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout(self.main)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.swMain.addWidget(self.main)
        self.researcher = QWidget()
        self.researcher.setObjectName(u"researcher")
        self.frame_4 = QFrame(self.researcher)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(130, 60, 991, 512))
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(229, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lError = QLabel(self.frame_4)
        self.lError.setObjectName(u"lError")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(12)
        self.lError.setFont(font1)
        self.lError.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.lError)

        self.leEmail = QLineEdit(self.frame_4)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setMinimumSize(QSize(491, 81))
        self.leEmail.setMaximumSize(QSize(491, 81))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(16)
        self.leEmail.setFont(font2)
        self.leEmail.setStyleSheet(u"background-color: rgb(245, 245, 246);\n"
"border: None;\n"
"border-bottom: 1px solid blue;\n"
"color: rgb(116, 116, 116);")
        self.leEmail.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.leEmail)

        self.lePassword = QLineEdit(self.frame_4)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMinimumSize(QSize(491, 81))
        self.lePassword.setMaximumSize(QSize(491, 16777215))
        self.lePassword.setFont(font2)
        self.lePassword.setStyleSheet(u"background-color: rgb(245, 245, 246);\n"
"border: None;\n"
"border-bottom: 1px solid blue;\n"
"color: rgb(116, 116, 116);")
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.lePassword.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lePassword)

        self.btnLogin = QPushButton(self.frame_4)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(491, 71))
        self.btnLogin.setMaximumSize(QSize(491, 71))
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(94, 184, 255);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"gridline-color:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 91, 159);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout.addWidget(self.btnLogin)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnForgetPassword = QPushButton(self.frame_4)
        self.btnForgetPassword.setObjectName(u"btnForgetPassword")
        self.btnForgetPassword.setMinimumSize(QSize(0, 0))
        self.btnForgetPassword.setMaximumSize(QSize(201, 51))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnForgetPassword.setFont(font3)
        self.btnForgetPassword.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border: none;\n"
"color:  rgb(2, 136, 209);\n"
"gridline-color:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:transparent;\n"
"border-bottom: 1px solid blue;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btnForgetPassword)

        self.btnRegister = QPushButton(self.frame_4)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setMinimumSize(QSize(201, 51))
        self.btnRegister.setMaximumSize(QSize(201, 51))
        self.btnRegister.setFont(font3)
        self.btnRegister.setStyleSheet(u"QPushButton {\n"
"background-color:transparent;\n"
"border: none;\n"
"color:  rgb(2, 136, 209);\n"
"gridline-color:transparent;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:transparent;\n"
"border-bottom: 1px solid blue;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.btnRegister)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_9.addLayout(self.verticalLayout_2, 2, 1, 2, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(971, 80))
        self.frame_5.setMaximumSize(QSize(971, 80))
        self.frame_5.setStyleSheet(u"background-color: rgb(94, 146, 243);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 20, 481, 41))
        font4 = QFont()
        font4.setFamily(u"Roboto Black")
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.frame_5, 0, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(229, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.gridLayout_10 = QGridLayout(self.researcher)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.swMain.addWidget(self.researcher)

        self.gridLayout_3.addWidget(self.swMain, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy2)
        self.topFrame.setStyleSheet(u"background-color: rgb(2, 136, 209);")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.topFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(768, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.topFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(70, 35))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Black")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.frame_3.setFont(font5)
        self.frame_3.setLayoutDirection(Qt.RightToLeft)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lUser = QLabel(self.frame_3)
        self.lUser.setObjectName(u"lUser")
        font6 = QFont()
        font6.setFamily(u"Roboto")
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.lUser.setFont(font6)
        self.lUser.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.lUser, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.topFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.swMain.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.btnResearcher.setText(QCoreApplication.translate("MainWindow", u"Estou Pesquisando", None))
        self.btnParticipant.setText(QCoreApplication.translate("MainWindow", u"Sou Participante", None))
        self.lError.setText("")
        self.leEmail.setText(QCoreApplication.translate("MainWindow", u"joelbisponeto@gmail.com", None))
        self.leEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.lePassword.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.lePassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.btnForgetPassword.setText(QCoreApplication.translate("MainWindow", u"Esqueci minha senha", None))
        self.btnRegister.setText(QCoreApplication.translate("MainWindow", u"Quero me cadastrar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u00c1rea de Pesquisa", None))
        self.lUser.setText("")
    # retranslateUi

