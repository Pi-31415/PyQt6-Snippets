from PyQt6.QtWidgets import QMessageBox, QApplication, QTableView
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt6 import QtCore

class MainWindow(QTableView):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Database demo 1')
        self.resize(230, 254)

        filename = os.path.join(os.path.dirname(__file__), "pyqt101.db")
    
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
    
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\n",
                QMessageBox.Cancel)
            return False

        sqm = QSqlQueryModel(parent = self)
        sqm.setQuery("SELECT * FROM `authors`")

        sqm.setHeaderData(1, QtCore.Qt.Orientations.Horizontal, 'Author names')

        self.setModel(sqm)
        self.hideColumn(0)
        db.close()


if __name__ == '__main__':

    import sys
    import os
    qApp = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(qApp.exec())
