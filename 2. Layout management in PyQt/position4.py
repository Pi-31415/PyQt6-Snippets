from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grid layout')

        label1 = QLabel(self)
        label1.setPixmap(QPixmap("Smiley_green_alien.svg.png"))
        label2 = QLabel(self)
        label2.setPixmap(QPixmap("Smiley_green_alien_wow.svg.png"))
        label3 = QLabel(self)
        label3.setPixmap(QPixmap("Smiley_green_alien_black_ninja.svg.png"))
        label4 = QLabel(self)
        label4.setPixmap(QPixmap("Smiley_green_alien_big_eyes.svg.png"))

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(label3, 0, 1)
        grid.addWidget(label4, 1, 1)

        self.setLayout(grid)

        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
