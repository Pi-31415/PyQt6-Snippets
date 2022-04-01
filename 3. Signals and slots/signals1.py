from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QDial
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.setWindowTitle('Signals example1')        
       
        lcd = QLCDNumber(self)        
        dial = QDial(self)
        dial.setMinimum(50)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)

        self.setLayout(vbox)
        dial.valueChanged.connect(lcd.display)
        
        self.resize(300, 254)
        self.show()

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
