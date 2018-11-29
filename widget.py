# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QInputDialog
from PyQt5.QtCore import QCoreApplication # for slots and signals


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Altering the parameters'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
            
        
            
        self.InitUI()


    def InitUI(self):
        self.button = QPushButton("Calculate the average deaths", self)    
        self.button.move(200,200)
        self.button.resize(280,40)
        #button.clicked.connect(self.CalAveDeaths)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        
 #   def CalcAveDeaths(self):
 #       ratscaught = int(self.ratscaught.value())
  #      humanpop = (self.humanpop.value())
   #     average_deaths = ((0.8*ratscaught) * (1.3*humanpop))
    #    average_deaths_string = "The average number of deaths per week is: " + int(average_deaths)  

#make application loop and exit window
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
















import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600,400)
    w.move(100,100)
    w.setWindowTitle("Altering the parameters")
    w.show()

    sys.exit(app.exec_())

























import sys

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Altering the parameters'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.CalcAveDeaths()
      
 
        self.show()
 
    def CalcAveDeaths(self):
        ratscaught = int(self.ratscaught.value())
        humanpop = (self.humanpop.value())
        average_deaths = ((0.8*ratscaught) * (1.3*humanpop))
        average_deaths_string = "The average number of deaths per week is: " + int(average_deaths)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

