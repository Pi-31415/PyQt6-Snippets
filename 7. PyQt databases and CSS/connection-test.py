from PyQt6.QtWidgets import QMessageBox, QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def createConnection():
    filename = os.path.join(os.path.dirname(__file__), "pyqt101.db")
    
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(filename)
    
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\n",
                QMessageBox.Cancel)
        return False

    query = QSqlQuery()    

    result = query.exec("SELECT Name FROM `authors`")    

    while query.next():
        print(query.value(0))
        #print(query.value("Name"))

    db.close()

if __name__ == '__main__':

    import sys
    import os
    app = QApplication(sys.argv)
    createConnection()
