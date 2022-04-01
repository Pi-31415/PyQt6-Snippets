from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QSpinBox, QLineEdit
from PyQt6.QtCore import pyqtSlot
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('Signals example')        
       
        nameLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QSpinBox()

        formLayout = QFormLayout()
        formLayout.addRow("Name:", nameLineEdit)
        formLayout.addRow("Email:", emailLineEdit)
        formLayout.addRow("Age:", ageSpinBox)

        ageSpinBox.valueChanged[int].connect(self.headsUp)
        
        self.setLayout(formLayout) 
        
        self.show()

    @pyqtSlot(int)
    def headsUp(self, arg1):
        print("New value is", arg1)

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
