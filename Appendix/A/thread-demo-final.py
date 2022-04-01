import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QRadioButton, QProgressBar
from PyQt6 import QtCore
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Threads demo final')
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
        self.stopProgress = False
        self.progressValue = self.progressBar.value()
        self.progressbar_counter(self.progressValue)

    def reset_progressbar(self):
        self.progressValue = 0
        self.progressBar.reset()
        self.stopProgress = True
        self.stop_progressbar()

    def stop_progressbar(self):
        self.stopProgress = True
        try:
            self.runThread.stop()
        except:
            pass

    def progressbar_counter(self, start_value=0):
        self.runThread = RunThread(parent=None, counter_start=start_value)
        self.runThread.start()
        self.runThread.counter_value.connect(self.set_progressbar)

    def set_progressbar(self, counter):
        if not self.stopProgress:
            self.progressBar.setValue(counter)

class RunThread(QtCore.QThread):

    counter_value = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, counter_start = 0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.isRunning = True

    def run(self):
        while (self.counter < 100) and (self.isRunning == True):
            sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)

    def stop(self):
        self.isRunning = False
        print("Stopping Thread")
        self.terminate()

if __name__ == '__main__':

     qApp = QApplication(sys.argv)
     form = MainWindow()
     sys.exit(qApp.exec())