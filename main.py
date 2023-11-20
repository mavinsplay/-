import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
import sqlite3

class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.load_data_from_database()

    def load_data_from_database(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM cofee')
        data = cursor.fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

        connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CoffeeApp()
    mainWindow.show()
    sys.exit(app.exec_())
