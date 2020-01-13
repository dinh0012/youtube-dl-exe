# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoDownload.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoDownload(object):
    def setupUi(self, infoDownload):
        infoDownload.setObjectName("infoDownload")
        infoDownload.resize(400, 300)
        self.label = QImage(infoDownload)
        self.label.setGeometry(QtCore.QRect(130, 70, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(infoDownload)
        QtCore.QMetaObject.connectSlotsByName(infoDownload)

    def retranslateUi(self, infoDownload):
        _translate = QtCore.QCoreApplication.translate
        infoDownload.setWindowTitle(_translate("infoDownload", "Form"))
        self.label.setText(_translate("infoDownload", "TextLabel"))
from qimage import QImage
