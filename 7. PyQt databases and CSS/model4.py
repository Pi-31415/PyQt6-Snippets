from PyQt6.QtWidgets import QMessageBox, QApplication, QTableView, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlTableModel, QSqlRelation, QSqlRelationalDelegate
from PyQt6.QtCore import Qt

def initializeModel(model):
    model.setTable('drinks')
    model.EditStrategy.OnRowChange
    model.setHeaderData(1, Qt.Orientations.Horizontal, 'Name')
    model.setHeaderData(2, Qt.Orientations.Horizontal, 'Type of drink')
    model.setRelation(2, QSqlRelation('category', 'id', 'drinktype'))
    model.select()

def createView(model):
    view = QTableView()
    view.setModel(model)
    view.setItemDelegate(QSqlRelationalDelegate(view))
    view.hideColumn(0)
    view.setColumnWidth(1, 150)
    view.setColumnWidth(2, 150)
    return view

def addRecord():
    model.insertRow(model.rowCount())
    view.scrollToBottom()
    
def delRecord():
    model.deleteRowFromTable(view.currentIndex().row())
    model.select()

if __name__ == '__main__':
    import sys
    import os

    app = QApplication(sys.argv)
    filename = os.path.join(os.path.dirname(__file__), "pyqt101.db")

    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName(filename)
    if not con.open():
        QMessageBox.critical(None, "Cannot open database",
                             "Unable to establish a database connection.\n",
                             QMessageBox.Cancel)
        sys.exit(1)

    model = QSqlRelationalTableModel()
    initializeModel(model)

    view = createView(model)

    vbox = QVBoxLayout()
    vbox.addWidget(view)
    btnAdd = QPushButton("&Add record")
    btnAdd.clicked.connect(addRecord)
    vbox.addWidget(btnAdd)
    btnDel = QPushButton("&Delete record")
    btnDel.clicked.connect(delRecord)
    vbox.addWidget(btnDel)

    window = QWidget()
    window.setWindowTitle("Database demo 4")
    window.setLayout(vbox)
    window.resize(340, 300)
    window.show()
    sys.exit(app.exec())
