from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("Youtube Download")
        main_window.resize(760, 600)
        main_window.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.girdLayout =  QtWidgets.QGridLayout(self.centralwidget)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 90, 23))
        self.label_4.setObjectName("label_4")
        self.txtDir = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDir.setEnabled(False)
        self.txtDir.setGeometry(QtCore.QRect(80, 10, 187, 20))
        self.txtDir.setObjectName("txtDir")
        self.btnFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnFile.setGeometry(QtCore.QRect(280, 10, 61, 23))
        self.btnFile.setObjectName("btnFile")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_3.setObjectName("label_3")
        self.txtUrl = QtWidgets.QTextEdit(self.centralwidget)
        self.txtUrl.setGeometry(QtCore.QRect(80, 40, 261, 71))
        self.txtUrl.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtUrl.setHtml("")
        self.txtUrl.setObjectName("txtUrl")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(10, 120, 331, 23))
        self.btnDownload.setObjectName("btnDownload")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(360, 10, 381, 131))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 19, 361, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Folder"))
        self.btnFile.setText(_translate("MainWindow", "Browser"))
        self.label_3.setText(_translate("MainWindow", "Link youtube"))
        self.txtUrl.setPlaceholderText(_translate("MainWindow", "Link youtube"))
        self.btnDownload.setText(_translate("MainWindow", "Download"))
        self.groupBox.setTitle(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Downloading (20%) Justin Bieber - Love Yourself (Lyrics)"))
        self.label_2.setText(_translate("MainWindow", ""))
