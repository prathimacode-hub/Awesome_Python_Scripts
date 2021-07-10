# Import Required Modules

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sqlite3
import sys

#-----------------------------------------------------------------------------------------------------------------------------------------------------

conn = sqlite3.connect('todo.db')  # connect to database

cur = conn.cursor()  # enable data manipulation

cur.execute('CREATE TABLE if not exists todo_list(list_item text)')   # create todo_list table

conn.commit()  # commit new changes

conn.close()  # close connection

#-----------------------------------------------------------------------------------------------------------------------------------------------------


class To_Do(object):  # Creating a class for the All Function
    
    def setupUi(self, MainWindow):  # set properties for main window
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 339)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)  # create central widget area on main window
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

       
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)   # create entry (lineEdit), buttons and list widget
        self.add_item_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_item())
        self.save_all_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_all_items())
        self.delete_item_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_item())
        self.clear_items_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_item())
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)

       
        self.lineEdit.setObjectName("lineEdit")   # set object properties of widgets
        self.add_item_pushButton.setObjectName("add_item_pushButton")
        self.save_all_pushButton.setObjectName("save_all_pushButton")
        self.delete_item_pushButton.setObjectName("delete_item_pushButton")
        self.clear_items_pushButton.setObjectName("clear_items_pushButton")
        self.listWidget.setObjectName("listWidget")

        
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 470, 31))   # set widgets geometry
        self.add_item_pushButton.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.save_all_pushButton.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.delete_item_pushButton.setGeometry(QtCore.QRect(250, 50, 111, 31))
        self.clear_items_pushButton.setGeometry(QtCore.QRect(370, 50, 111, 31))
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 470, 241))

        
        _translate = QtCore.QCoreApplication.translate   # create instance fot translate
        
       
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List "))   # create instance fot translate set widgets text
        self.add_item_pushButton.setText(_translate("MainWindow", "Add Task"))
        self.save_all_pushButton.setText(_translate("MainWindow", "Save Tasks"))
        self.delete_item_pushButton.setToolTip(_translate("MainWindow", "Delete Task"))
        self.clear_items_pushButton.setText(_translate("MainWindow", "Clear Tasks"))

        
        self.lineEdit.setFont(QFont('times', 14)) # set text font
        self.add_item_pushButton.setFont(QFont('times', 14 ))
        self.save_all_pushButton.setFont(QFont('Ariel', 14))
        self.delete_item_pushButton.setFont(QFont('times', 14))
        self.clear_items_pushButton.setFont(QFont('times', 14))
        self.listWidget.setFont(QFont('times', 14))

        
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter Task"))   # set tooltip text to display it while user hover over the widget
        self.add_item_pushButton.setToolTip(_translate("MainWindow", "Add Task"))
        self.save_all_pushButton.setToolTip(_translate("MainWindow", "Save all Tasks"))
        self.delete_item_pushButton.setText(_translate("MainWindow", "Delete Task"))
        self.clear_items_pushButton.setToolTip(_translate("MainWindow", "Clear Tasks"))
        
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Task")) # set place holder text for entry i.e lineEdit widget
        
        self.get_items()

#-----------------------------------------------------------------------------------------------------------------------------------------------------
        
    def get_items(self):
       
        conn = sqlite3.connect('todo.db')  # connect to database
        
        cur = conn.cursor() # enable data manipulation
        cur.execute('SELECT * FROM todo_list')  # select data from table
        
        rows = cur.fetchall() # fetch data
         
        conn.commit() # commit new changes
        conn.close()  # close connection
        
        for row in rows: # iterate through each row
            self.listWidget.addItem(str(row[0])) # add data in list 

#-----------------------------------------------------------------------------------------------------------------------------------------------------
            
    def add_item(self):
        
        item = self.lineEdit.text() # get user entered item
        self.listWidget.addItem(item) # add entered item in list
        item = self.lineEdit.setText("")  # clear item entry

#-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def save_all_items(self):
        
        conn = sqlite3.connect('todo.db')  # connect to database
        
        cur = conn.cursor()  # enable data manipulation
        cur.execute('DELETE FROM todo_list')  # delete data from table
       
        
        items = []   # create empty list to store items of list widget
        
        
        for i in range(self.listWidget.count()): # iterate throgh list widget items
            items.append(self.listWidget.item(i)) # append each item to items list
       
        for item in items:  # iterate through items list
            cur.execute("INSERT INTO todo_list VALUES (:item)",{'item':item.text()})  # insert items into table
       
        conn.commit()  # commit new changes
        conn.close()  # close connection

#-----------------------------------------------------------------------------------------------------------------------------------------------------
        
    def delete_item(self):
        
        clicked = self.listWidget.currentRow()  # get index number for selected row or item
        self.listWidget.takeItem(clicked)    # delete item from list widget

#-----------------------------------------------------------------------------------------------------------------------------------------------------

    def clear_item(self):
        
        self.listWidget.clear()  # clear list items

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Main Loop Function

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = To_Do()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
