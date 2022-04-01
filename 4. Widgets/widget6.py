from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import pyqtSlot, QStringListModel
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('Slot machine sim')
        
        myList = []
        myList.extend(range(0,10))
        myList = [str(i) for i in myList]

        stringModel = QStringListModel(self)
        stringModel.setStringList(myList)

        self.comboBox1 = QComboBox(self)
##        self.comboBox1.addItem("0")
##        self.comboBox1.addItem("1")
##        self.comboBox1.addItem("2")
##        self.comboBox1.addItem("3")
##        self.comboBox1.addItem("4")
##        self.comboBox1.addItem("5")
##        self.comboBox1.addItem("6")
##        self.comboBox1.addItem("7")
##        self.comboBox1.addItem("8")
##        self.comboBox1.addItem("9")
        self.comboBox1.setModel(stringModel)

        self.comboBox2 = QComboBox(self)
        self.comboBox3 = QComboBox(self)

        self.comboBox2.setModel(stringModel)
        self.comboBox3.setModel(stringModel)

        self.comboBox1.move(50, 50)
        self.comboBox2.move(100, 50)
        self.comboBox3.move(150, 50)

        self.movie = QMovie("tenor.gif")

        self.label1 = QLabel(self)
        self.label1.move(50, 100)
        self.label1.setGeometry(50, 100, 400, 500)
        self.label1.setMovie(self.movie)

        self.comboBox1.activated[int].connect(self.onActivated)
        self.comboBox2.activated[int].connect(self.onActivated)
        self.comboBox3.activated[int].connect(self.onActivated)

        self.resize(500, 650)
        self.show()

    @pyqtSlot(int)
    def onActivated(self, text):
        if(self.comboBox1.currentText() == '7' and self.comboBox2.currentText() == '7'\
           and self.comboBox3.currentText() == '7'):
            self.movie.start()
            #self.comboBox1.setEnabled(False)
            print("Lotto!!!")

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
