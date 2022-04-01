import sys
from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6.QtWidgets import QApplication, QGridLayout, QGroupBox, QPushButton, QRadioButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup1(), 1, 0)
        grid.addWidget(self.createExampleGroup(), 0, 1)
        grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("CSS Inheritance demo")
        self.resize(400, 300)

    def createExampleGroup(self):
        groupBox = QGroupBox("Best Food")

        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def createExampleGroup1(self):
        groupBox = QGroupBox("Best Food1")

        radio1 = QRadioButton("&Radio pizza")
        radio2 = QRadioButton("R&adio taco")
        radio3 = QRadioButton("Ra&dio burrito")

        radio1.setChecked(True)

        btnRand = QPushButton("&Random button")

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(btnRand)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet("QGroupBox { color: red; } ")

    #app.setStyleSheet("QGroupBox, QGroupBox * { color: red; }")

    #QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_UseStyleSheetPropagationInWidgetStyles, True)
    #app.setStyleSheet("QGroupBox { color: red; } ")
    
    clock = Window()
    clock.show()
    sys.exit(app.exec())
