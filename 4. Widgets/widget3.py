from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QSlider
from PyQt6.QtCore import Qt, pyqtSlot
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.setWindowTitle('Radio tuner')        
       
        self.lcd = QLCDNumber(self)        
        slider = QSlider(self)
        slider.setOrientation(Qt.Orientations.Horizontal)
        self.lcd.setProperty("value", 87.5)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged[int].connect(self.headsUp)
        
        self.resize(300, 254)
        self.show()

    @pyqtSlot(int)
    def headsUp(self, arg1):
        display = str(87.5 + (0.205*arg1))
        self.lcd.setProperty("value", display)

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
