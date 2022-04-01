from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Box layout2')

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addStretch()
        hbox.addWidget(btn2)
        self.setLayout(hbox)

        self.resize(300, 254)
        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
