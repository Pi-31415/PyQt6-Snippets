from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt6.QtCore import pyqtSlot
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('QLineEdit widget')        
       
        basicLineEdit = QLineEdit(self)
        self.resultLabel = QLabel(self)

        basicLineEdit.move(10,100)
        #self.resultLabel.setMaximumWidth(100)
        self.resultLabel.move(10,150)

        basicLineEdit.textChanged[str].connect(self.headsUp)        

        self.resize(300, 300)
        self.show()

    @pyqtSlot(str)
    def headsUp(self, arg1):        
        self.resultLabel.setText(arg1)
        self.resultLabel.adjustSize()        

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
