from PyQt6.QtWidgets import QMessageBox, QApplication, QTableView, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate, QSqlTableModel
from PyQt6.QtCore import Qt

def initializeModel(model):
    model.setTable('booksauthors')
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.dataChanged.connect(model.submitAll)
    model.setRelation(0, QSqlRelation("authors", "id", "name"))
    model.setRelation(1, QSqlRelation("books", "id", "title"))
    model.setHeaderData(0, Qt.Horizontal, 'Author name(s)')
    model.setHeaderData(1, Qt.Horizontal, 'Book title')
    model.select()    

def createView(model):
   view = QTableView()
   view.setModel(model)
   view.setItemDelegateForColumn(0, QSqlRelationalDelegate(view))
   view.setColumnWidth(1, 200)
   view.setColumnWidth(0, 200)
   return view

def addRecord():
    # We insert an empty record into which the user can enter their data
    sqm.insertRow(sqm.rowCount())

def delRecord() :    
    sqm.removeRow(view1.currentIndex().row())
    # We reload the data in the model, to remove an empty "garbage" record
    sqm.select()

if __name__ == '__main__':

    import sys
    import os
    qApp = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "pyqt101.db")
    
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
            "Unable to establish a database connection.\n",
            QMessageBox.Cancel)
        sys.exit(1)

    sqm = QSqlRelationalTableModel()
    initializeModel(sqm)

    view1 = createView(sqm)

    vbox = QVBoxLayout()    

    btnAdd = QPushButton("&Add a record")
    btnAdd.clicked.connect(addRecord)

    btnDel = QPushButton("&Delete record")
    btnDel.clicked.connect(delRecord)

    vbox.addWidget(view1)
    vbox.addWidget(btnAdd)
    vbox.addWidget(btnDel)

    window = QWidget()
    window.setLayout(vbox)
    window.setWindowTitle("Database demo 3")
    window.resize(470, 420)
    window.show()
    
    sys.exit(qApp.exec())
