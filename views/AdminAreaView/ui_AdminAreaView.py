# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminAreaView.ui'
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


class Ui_AdminAreaView(object):
    def setupUi(self, AdminAreaView):
        if not AdminAreaView.objectName():
            AdminAreaView.setObjectName(u"AdminAreaView")
        AdminAreaView.resize(1298, 726)
        AdminAreaView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_4 = QGridLayout(AdminAreaView)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_5 = QFrame(AdminAreaView)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(100, 50))
        self.frame_5.setMaximumSize(QSize(12121212, 1212121))
        self.frame_5.setStyleSheet(u"background-color: rgb(94, 146, 243);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(AdminAreaView)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnNewExpriment = QPushButton(self.frame)
        self.btnNewExpriment.setObjectName(u"btnNewExpriment")
        self.btnNewExpriment.setMinimumSize(QSize(191, 41))
        self.btnNewExpriment.setMaximumSize(QSize(191, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(12)
        self.btnNewExpriment.setFont(font1)
        self.btnNewExpriment.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btnNewExpriment)

        self.horizontalSpacer_3 = QSpacerItem(968, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(518, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.btnNewExpriment_2 = QPushButton(self.frame)
        self.btnNewExpriment_2.setObjectName(u"btnNewExpriment_2")
        self.btnNewExpriment_2.setMinimumSize(QSize(191, 41))
        self.btnNewExpriment_2.setMaximumSize(QSize(191, 41))
        self.btnNewExpriment_2.setFont(font1)
        self.btnNewExpriment_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.btnNewExpriment_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.tbExperiment = QTableWidget(self.frame)
        if (self.tbExperiment.columnCount() < 2):
            self.tbExperiment.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbExperiment.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbExperiment.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbExperiment.setObjectName(u"tbExperiment")

        self.gridLayout_2.addWidget(self.tbExperiment, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.retranslateUi(AdminAreaView)

        QMetaObject.connectSlotsByName(AdminAreaView)
    # setupUi

    def retranslateUi(self, AdminAreaView):
        AdminAreaView.setWindowTitle(QCoreApplication.translate("AdminAreaView", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("AdminAreaView", u"Pesquisas", None))
        self.btnNewExpriment.setText(QCoreApplication.translate("AdminAreaView", u"Criar novo experimento", None))
        self.btnNewExpriment_2.setText(QCoreApplication.translate("AdminAreaView", u"Iniciar uma nova sess\u00e3o", None))
        ___qtablewidgetitem = self.tbExperiment.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminAreaView", u"Name", None));
        ___qtablewidgetitem1 = self.tbExperiment.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminAreaView", u"Numbers", None));
    # retranslateUi

