from PyQt6.QtWidgets import QApplication, QWidget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple example 1')
        self.resize(230, 254)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
