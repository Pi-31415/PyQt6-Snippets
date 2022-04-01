from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLineEdit, QFormLayout
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.setWindowTitle('Signals example2')               
        
        self.nameLineEdit = QLineEdit()
        self.submitButton = QPushButton("&Submit")

        formLayout = QFormLayout()
        formLayout.addRow("Name:", self.nameLineEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(formLayout)
        vbox.addWidget(self.submitButton)        

        self.submitButton.clicked.connect(self.submitContact)

        self.setLayout(vbox)
        self.show()
        
    def submitContact(self):
        name = self.nameLineEdit.text()

        if name == "":
            QMessageBox.critical(self, "Empty Field",
                                    "Please enter a name and address.")
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
