from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Box layout3')

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addStretch()
        vbox.addWidget(btn2)

        btn3 = QPushButton("Button 3", self)
        btn4 = QPushButton("Button 4", self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn3)
        hbox.addStretch()
        hbox.addWidget(btn4)

        vbox.addStretch()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
