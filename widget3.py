# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:54:02 2018

@author: medctai
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:30:05 2018

@author: medctai

Version 2


"""
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QCoreApplication # for slots and signals


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Altering the parameters'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 300
            
    
        self.InitUI()


    def InitUI(self):
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText('Please enter the average number of rats caught')
        self.lineedit1.setGeometry(50,50,240,30)
        
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText('Please enter the population density')
        self.lineedit2.setGeometry(50,90,190,30)
        
        self.button = QPushButton("Calculate the average deaths", self)    
        self.button.setGeometry(50,150,100,30)
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
    # QMessageBox.about(self, 'Average deaths', 'average_deaths_string')

#make application loop and exit window
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())