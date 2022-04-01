#here we import necessary things we need
import sys
from PyQt6 import QtWidgets, QtGui, QtCore, Qt


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.imagePath = "240px-Smiley.svg.png"

        self.initGUI()

        self.window.setWindowTitle("Before applying CSS")
        
        self.window.setGeometry(500, 100, 300,600)
        self.window.show()
        sys.exit(self.app.exec())

    def initGUI(self):

        #create a label
        self.image = QtGui.QImage(self.imagePath)
        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(50,20, 200,200)

        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        #create a pseudo field
        self.pseudo = QtWidgets.QTextEdit(self.window)
        self.pseudo.setGeometry(25,270,250,40)
        self.pseudo.setText("Pseudo")


        #create an email field
        self.email = QtWidgets.QTextEdit(self.window)
        self.email.setGeometry(25, 330,250,40)
        self.email.setText("Email")

        #create a password field
        self.password = QtWidgets.QTextEdit(self.window)
        self.password.setGeometry(25,390,250,40)
        self.password.setText("Password")

        #create a comfirm password field
        self.confirmPassword = QtWidgets.QTextEdit(self.window)
        self.confirmPassword.setGeometry(25,450,250,40)
        self.confirmPassword.setText("Confirm Password")

        #creata the create account button
        self.createBtn = QtWidgets.QPushButton(self.window)
        self.createBtn.setText("Create an Account")
        self.createBtn.setGeometry(25, 510, 250, 40)


#let's instantiate an object to the class MainWindow
main = MainWindow()
