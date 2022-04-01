from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QSpinBox, QLineEdit
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Form layout')

        nameLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QSpinBox()
        
        passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        formLayout = QFormLayout()
        formLayout.addRow("Name:", nameLineEdit)
        formLayout.addRow("Password:", passwordLineEdit)
        formLayout.addRow("Email:", emailLineEdit)
        formLayout.addRow("Age:", ageSpinBox)

        self.setLayout(formLayout)
        self.resize(350, 120)

        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
