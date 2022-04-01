from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple example 2')

        self.setWindowIcon(QIcon('240px-Smiley.svg.png'))

        btnClick = QPushButton(parent=self)
        #btnClick = QPushButton(self)
        #btnClick = QPushButton()
        btnClick.setText('Quit')
        btnClick.move(110, 50)
        btnClick.clicked.connect(QApplication.instance().quit)

        self.resize(300, 254)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
