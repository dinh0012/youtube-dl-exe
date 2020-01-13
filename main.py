from PyQt5 import QtWidgets

from mydesign import Ui_MainWindow  # importing our generated file
import youtube_dl
from logDownload import MyLogger
import sys
import os
from var_dump import var_dump
import re
from PyQt5.QtWidgets import (QMessageBox)
from threads.Download import Download


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.btnDownload.clicked.connect(self.btnClicked)
        self.ui.txtDir.setText('/home/dinhnv/Desktop/test')
        self.ui.txtUrl.setText('https://www.youtube.com/watch?v=VD3swXisXSM&list=PLKU4arUIngTxmHYvkKUA3HylwU8oiSC5y')
        self.ui.btnFile.clicked.connect(self.browseSlot)
        self.ui.tableWidget.setColumnWidth(0, 199)

        self.rowItems = []
        self.url_list = []
        self.complete_url_list = {}
        self.convert_list = []
        self.thread_pool = {}
        self.rowcount = 0

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
        if url.strip() == "":
            self.msgbox("URL can not bank!")
            return
        if directory.strip() == "":
            self.msgbox("Folder can not bank!")
            return

        can_download, rowcount = self.can_download(url)
        if can_download:
            self.download_url(url, rowcount)
        else:
            self.msgbox("This url is already being downloaded")
            if len(self.url_list) is not 0:
                if len(self.url_list) < 2:
                    self.ui.statusbar.showMessage('Downloading {0} file'.format(len(self.url_list)))
                else:
                    self.ui.statusbar.showMessage('Downloading {0} files'.format(len(self.url_list)))
            else:
                self.ui.statusbar.showMessage("done")

    def get_format(self):
        format = self.ui.formatVideo.currentText()
        checkboxes_checked = self.get_checkbox_checked()
        if len(checkboxes_checked) == 0:
            return []
        postprocessors_checkboxes = []
        postprocessors = self.postprocessors()
        for checkbox in checkboxes_checked:
            key = checkbox.text().lower()
            if key in postprocessors:
                postprocessors_checkboxes.append(postprocessors[key])
        return postprocessors_checkboxes

    def postprocessors(self):
        return {
            "mp3": {
                'format': "bestaudio",
                "postprocessors": {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            },
            "mp4": {
                'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/",
            },

            "flv": {
                'format': "bestvideo[ext=flv]+bestaudio[ext=m4a]/",
            },

            "3gp": {
                'format': "bestvideo[ext=3gp]+bestaudio[ext=m4a]/",
            },
        }

    def download_url(self, url, row=None):
        if row >= 0:
            row = row
        elif row is None:
            row = self.rowcount

        directory = str(self.ui.txtDir.text())
        postprocessors = self.get_format()
        if len(postprocessors) == 0:
            self.msgbox("Please select format to convert!")
            return
        options = {
            'url': url,
            'directory': directory,
            'rowcount': row,
            'proxy': '',
            'postprocessors': postprocessors,
            'parent': self,
        }

        self.thread_pool = Download(options)
        self.thread_pool.status_bar_signal.connect(self.ui.statusbar.showMessage)
        self.thread_pool.remove_url_signal.connect(self.remove_url)
        self.thread_pool.add_update_list_signal.connect(self.add_to_table)
        self.thread_pool.remove_row_signal.connect(self.decrease_rowcount)
        self.thread_pool.start()

    def can_download(self, url):
        if url not in self.url_list:
            for row, _url in self.complete_url_list.items():
                if url == _url:
                    return True, row
            return True, self.rowcount
        else:
            return False, self.rowcount

    def remove_url(self, url):
        try:
            self.url_list.remove(url)
        except:
            print(url)
            print(self.url_list)
            return

    def add_to_table(self, values):
        ui = self.ui
        rowItems = self.rowItems
        filename = values['filename']
        tableWidget = ui.tableWidget
        rowCount = tableWidget.rowCount()

        tableWidget.setRowCount(rowCount)
        col = 0
        if filename not in rowItems:
            rowItems.append(filename)

        new_row_count = len(rowItems)

        if rowCount != new_row_count:
            tableWidget.insertRow(tableWidget.rowCount())
        new_row = new_row_count - 1;
        for value in values:
            if value == 'row':
                continue
            tableWidget.setItem(new_row, col, QtWidgets.QTableWidgetItem(values[value]))
            tableWidget.item(new_row, col).setToolTip(values[value])
            col += 1

    def decrease_rowcount(self):
        self.rowcount -= 1


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
