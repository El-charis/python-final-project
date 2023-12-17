"""
    This is a number guessing script with a GUI using PyQt6
    You will be ask for a number within the range of your choice
    and it'll be compared to the generated random number
"""

#           IMPORTTIMG ALL THE NECESSARY LIBRARIES
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow,QFrame, QVBoxLayout, QGridLayout, QHBoxLayout, QScrollBar, QScrollArea,QInputDialog, QLineEdit,  QMessageBox, QApplication, QWidget, QStackedWidget, QSizePolicy
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap, QIcon, QImage
from PyQt6.QtCore import QTimer,pyqtSlot, QDate, Qt, pyqtSlot
import datetime
import random
import sys
import ast

# creating the class for the MainWindow Interface
class NumGuessing(QMainWindow):
    def __init__(self):
        super(NumGuessing, self).__init__()

        loadUi("NumGuessing.ui", self) #To Load the UI 

# Connecting button clicks to corresponding functions
        self.setrange.clicked.connect(self.getrange)
        self.submit.clicked.connect(self.checkguess)
        
    def getrange(self):  # defining the getrange func to set the range to custom range
        rang = []
        start = self.start.text()  # start 
        to = self.to.text()   # end
        rang.append(int(start))
        rang.append(int(to))
        self.range.setText(f"Range set from {start} to {to}")
        return rang
        
    def checkguess(self):    # defining the function to compare the input number and the generated random integer
        inp = self.num.text()
        num_range = self.getrange()
        start = num_range[0]
        end = num_range[1]
        rand = random.randint(start, end)
        
        if start > int(inp) > end:   # Handling the error if number given is out of range
            self.check.setText("Invalid input ❌❌❌")
            self.check.setStyleSheet("color:red;")
            
        if int(inp) == rand:     # if the number given is the same as the random integer
            self.check.setText("Correct! ✅✅✅")
            self.check.setStyleSheet("color:green;")
            self.lcd.display(f"{rand}")
        else: # if the number given is not same as the random integer
            self.check.setText("Incorrect! ❌❌❌")
            self.check.setStyleSheet("color:red;")
            self.lcd.display(f"{rand}")
            

app = QApplication(sys.argv)  #   creating the app instance
home = NumGuessing()          # Creating an instance of the NumGuessing class


# Creating a stacked widget and adding the NumGuessing instance
widget = QStackedWidget()
widget.addWidget(home)

# Setting the fixed height and width of the widget and displaying it
widget.setFixedHeight(660)
widget.setFixedWidth(900)
widget.show()

# Running the application
try:
    print("1")
    app.exec()
except:
    print("Exiting!!!")