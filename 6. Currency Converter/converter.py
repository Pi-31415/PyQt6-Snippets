from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.usdLabel.clear)
        self.pushButton.clicked.connect(self.audLabel.clear)
        self.pushButton.clicked.connect(self.xauLabel.clear)
        self.pushButton.clicked.connect(self.btcLabel.clear)
        
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
