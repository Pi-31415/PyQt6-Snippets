from PyQt6.QtCore import QCoreApplication, QObject, QUrl
from PyQt6.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
import sys

class MainWindow(QObject):
    def __init__(self):
        super().__init__()

        target = "https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html"
        request = QNetworkRequest(QUrl(target))

        self.networkAccessManager = QNetworkAccessManager()
        self.networkAccessManager.finished.connect(self.onFinished)
        self.networkAccessManager.get(request)

    def onFinished(self, response): #response is an object of type QNetworkReply
        error = response.error()

        if (str(error) == "NetworkError.NoError"):
            result = response.readAll() # you can print this if you like
            print("Response content type is: "+response.header(QNetworkRequest.KnownHeaders.ContentTypeHeader))
            print("Server header is: "+response.header(QNetworkRequest.KnownHeaders.ServerHeader))
            print("Server response time is: "+response.header(QNetworkRequest.KnownHeaders.LastModifiedHeader).toString())            
        else:
            print("There was an error. "+response.errorString())

        self.windUp(response)        

    def windUp(self, replyObject): #replyObject is an object of type QNetworkReply
        ##print("Network request completed!")
        replyObject.deleteLater()
        QCoreApplication.quit()       


if __name__ == '__main__':

    qApp = QCoreApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
