from PyQt5 import QtWidgets

from mydesign import Ui_MainWindow  # importing our generated file
import youtube_dl
from logDownload import MyLogger
import sys
import os
from var_dump import var_dump
from PyQt5.QtCore import (QFile, QPoint, QRect, QSize, QStandardPaths,
                                            Qt, QProcess, QSettings)
from PyQt5.QtWidgets import (QMessageBox)
class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.btnDownload.clicked.connect(self.btnClicked)
        self.ui.btnFile.clicked.connect(self.browseSlot)

    def my_hook(self, d):
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Done downloading {}".format(file_tuple[1]))

        if d['status'] == 'downloading':
            percent = round (d['downloaded_bytes']/d['total_bytes'] * 100)
            self.ui.progressBar.setValue(percent) #update progress bar
            print(percent, d['filename'], d['_percent_str'], d['_eta_str'])
    def browseSlot(self):
        QFileDialog = QtWidgets.QFileDialog
        directory = QFileDialog.getExistingDirectory(self, "Select Folder",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        if directory:
            self.ui.txtDir.setText(directory)

    def msgbox(self, message):
        QMessageBox.warning(self, "Message", message)
    def btnClicked(self):
        ui = self.ui
        url = ui.txtUrl.toPlainText()
        directory = ui.txtDir.text()
        if url.strip() == "" :
            self.msgbox("URL can not bank!")
            return
        if directory.strip() == "":
            self.msgbox("Folder can not bank!")
            return

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': directory + '/%(title)s.%(ext)s', # add destination save folder
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            self.video_dict = ydl.extract_info(url, download=False)
            var_dump(self.video_dict)

app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
