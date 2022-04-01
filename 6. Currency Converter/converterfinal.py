from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
import requests

CURRENCYLAYER_API_KEY = "put your API key here"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.talkToService)
        self.pushButton.clicked.connect(self.talkToService)
        self.pushButton.clicked.connect(self.talkToService)
        self.pushButton.clicked.connect(self.talkToService)
        
        self.show()

    def talkToService(self):
        try:            
            r = requests.get('http://apilayer.net/api/live?access_key='+CURRENCYLAYER_API_KEY+
                     '&currencies=USD,AUD,CAD,XAU,BTC&format=1')
            response = r.json()

            self.usdLabel.setText(str(response['quotes']['USDUSD']))
            self.audLabel.setText(str(response['quotes']['USDAUD']))
            self.xauLabel.setText(str(response['quotes']['USDXAU']))
            self.btcLabel.setText(str(response['quotes']['USDBTC']))
        except:
            QtWidgets.QMessageBox.critical(self, "Exception",
                                    "Something went wrong!")            
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
