# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web_dialog.ui'
#
# Created: Tue Nov  4 02:55:22 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WebDialog(object):
    def setupUi(self, WebDialog):
        WebDialog.setObjectName("WebDialog")
        WebDialog.resize(640, 480)
        self.gridLayout = QtGui.QGridLayout(WebDialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(WebDialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.webView = QtWebKit.QWebView(self.groupBox)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(WebDialog)
        QtCore.QMetaObject.connectSlotsByName(WebDialog)

    def retranslateUi(self, WebDialog):
        WebDialog.setWindowTitle(QtGui.QApplication.translate("WebDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
