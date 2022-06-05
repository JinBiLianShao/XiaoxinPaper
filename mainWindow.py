# author ：Liansixin

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 431)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 60, 321, 291))
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(600, 60, 321, 291))
        self.textEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 190, 101, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(750, 30, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(430, 370, 161, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小鑫降重工具"))
        self.pushButton.setText(_translate("MainWindow", "开始降重"))
        self.label.setText(_translate("MainWindow", "原文"))
        self.label_2.setText(_translate("MainWindow", "结果"))
        self.label_3.setText(_translate("MainWindow", "该工具使用需要联网哦"))
