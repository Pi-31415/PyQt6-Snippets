from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Absolute positioning')

        self.setWindowIcon(QIcon('240px-Smiley.svg.png'))

        label1 = QLabel(parent=self)
        label1.setText('Don\'t')
        label1.move(80, 50)

        label2 = QLabel(self)
        label2.setText('use')
        label2.move(90, 80)

        label3 = QLabel('this positioning technique in real life!',self)
        label3.move(100, 110)

        self.resize(350, 254)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
