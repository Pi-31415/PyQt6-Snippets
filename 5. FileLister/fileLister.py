from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
import os

from mainwindow import Ui_MainWindow

class ExampleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in the file automatically generated, mainwindow.py
                            # It sets up layout and widgets defined there
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.show()

    def browse_folder(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        directory = QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    form = ExampleApp()
    sys.exit(qApp.exec())
