import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QRadioButton, QProgressBar
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Threads demo')
        self.resize(534, 354)

        self.centralwidget = QWidget(self)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(10, 20, 511, 311)

        self.tab = QWidget(self)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget(self)

        self.startButton = QRadioButton(self.tab_2)
        self.startButton.setGeometry(20, 20, 82, 17)

        self.stopButton = QRadioButton(self.tab_2)
        self.stopButton.setGeometry(20, 40, 82, 17)

        self.resetButton = QRadioButton(self.tab_2)
        self.resetButton.setGeometry(20, 60, 82, 17)

        self.progressBar = QProgressBar(self.tab_2)
        self.progressBar.setGeometry(40, 150, 391, 23)
        self.progressBar.setProperty("value", 0)

        self.tabWidget.addTab(self.tab_2, "")

        self.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Tab 1")
        self.startButton.setText("Start")
        self.stopButton.setText("Stop")
        self.resetButton.setText("Reset")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Tab 2")

        self.startButton.clicked.connect(self.start_progressbar)
        self.stopButton.clicked.connect(self.stop_progressbar)
        self.resetButton.clicked.connect(self.reset_progressbar)

        self.progressValue = 0
        self.stopProgress = False

        self.show()

    def start_progressbar(self):
        self.progressValue = self.progressBar.value()

        while (self.progressValue <= 101) and not (self.stopProgress):
            self.progressBar.setValue(self.progressValue)
            #self.progressValue += 0.00001
            self.progressValue += 1
            sleep(0.1)
            #QApplication.processEvents()

    def reset_progressbar(self):
        self.progressValue = 0
        self.progressBar.reset()
        self.stopProgress = False

    def stop_progressbar(self):
        self.stopProgress = True
        

if __name__ == '__main__':

     qApp = QApplication(sys.argv)
     form = MainWindow()
     sys.exit(qApp.exec())
