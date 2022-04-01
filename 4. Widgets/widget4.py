from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
import sys, time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('QProgressBar demo')        
       
        self.timerButton = QPushButton("Start", self)
        self.timerButton.clicked.connect(self.download)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(10, 20, 290, 25)                

        self.timerButton.move(110,150)        
        self.progressBar.move(10,100)

        self.resize(300, 300)
        self.show()

    def download(self):
        self.completed = 0
        self.timerButton.setEnabled(False)

        while self.completed < 15:
            self.completed += 1
            time.sleep(1)
            self.progressBar.setValue(self.completed)
            
        self.timerButton.setEnabled(True)

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
