
"""
Version 6
Author: C Tait
Last update 29/11/18

This version has a bigger gui that allows you to also specify the other parameters.
output limited to 1 dp.    

NEed to figure out why label isnt the right length.  plus add other free text and then make the line edit boxes smaller etc

"""
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt5.QtCore import QCoreApplication # for slots and signals


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Altering the parameters'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 600
        self.InitUI()

    def InitUI(self):
        label = QLabel('Average number of rats caught per week = ', self)
        label.move(10,10)
        
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText('Please enter the average number of rats caught')
        self.lineedit1.setGeometry(50,50,310,30)
        
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText('Please enter the population density')
        self.lineedit2.setGeometry(50,90,310,30)
        
        self.button = QPushButton("Calculate the average deaths", self)    
        self.button.setGeometry(50,150,310,30)
        self.button.resize(310,50)
        self.button.clicked.connect(self.CalcAveDeaths)
        
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setPlaceholderText('Please enter the multipler of the average number of rats caught')
        self.lineedit3.setGeometry(50,300,310,30)
        
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setPlaceholderText('Please enter multiplier for the population density')
        self.lineedit4.setGeometry(50,350,310,30)
        
        self.button2 = QPushButton("Recalculate the average deaths based on these new values", self)    
        self.button2.setGeometry(50,400,100,30)
        self.button2.resize(310,50)
        self.button2.clicked.connect(self.ReCalcAveDeaths)
    
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        
    def CalcAveDeaths(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        average_deaths = "{0:.1f}".format((0.8*num1) * (1.3*num2))
        average_deaths_string = "The average number of deaths per week is " + str(average_deaths)  
        QMessageBox.about(self, 'Average deaths', average_deaths_string)

    def ReCalcAveDeaths(self):
        num1 = float(self.lineedit1.text())
        num2 = float(self.lineedit2.text())
        num3 = float(self.lineedit3.text())
        num4 = float(self.lineedit4.text())
        average_deaths2 = "{0:.1f}".format((num3*num1) * (num4*num2))
        average_deaths2_string = "The new average number of deaths per week is " + str(average_deaths2)  
        QMessageBox.about(self, 'New average deaths', average_deaths2_string)


#make application loop and exit window
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())