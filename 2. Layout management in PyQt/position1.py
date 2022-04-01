from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Box layout1')

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addStretch()
        vbox.addWidget(btn2)
        self.setLayout(vbox)

        self.resize(300, 254)
        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
