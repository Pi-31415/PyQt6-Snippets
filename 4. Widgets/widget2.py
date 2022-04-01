from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget, QCheckBox
from PyQt6.QtCore import pyqtSlot, QDate
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('QCheckBox example')        

        vbox = QVBoxLayout(self)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.headsUp)

        checkbox = QCheckBox('Disable Grid?', self)
        #checkbox.stateChanged.connect(self.toggleCalendarGrid)
        checkbox.stateChanged.connect(self.headsUp)
        
        self.resultLabel = QLabel(self.calendar.selectedDate().toString(),self)

        vbox.addWidget(checkbox)
        vbox.addWidget(self.calendar)
        vbox.addWidget(self.resultLabel)

        self.resize(300, 300)
        self.show()

    @pyqtSlot(QDate)
    def headsUp(self, arg1):                
        self.resultLabel.setText(arg1.toString())

    @pyqtSlot()
    def headsUp(self):
        if not (self.calendar.isGridVisible()):
            self.calendar.setGridVisible(True)
        else:
            self.calendar.setGridVisible(False)

##    def toggleCalendarGrid(self):
##        if not (self.calendar.isGridVisible()):
##            self.calendar.setGridVisible(True)
##        else:
##            self.calendar.setGridVisible(False)

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
