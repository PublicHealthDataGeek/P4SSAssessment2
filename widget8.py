
"""
Version 8
Author: C Tait
Last update 07/12/18
Final version - unless equation is going to alter
"""

# Import the relevent packages for this program
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox, QLabel

# Create a class for the GUI
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Altering the parameters'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 600
        self.InitUI()

## Create the structure within the GUI including the text, text boxes and 
#call the relevent methods
    def InitUI(self):
        self.label1 = QLabel(self)
        self.label1.setText('Average deaths = (0.8 x rats caught) x (1.2 x population density)')
        self.label1.resize(400,30)
        self.label1.move(20,10)
        
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText('Please enter the average number of rats caught')
        self.lineedit1.setGeometry(50,50,320,30)
        
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText('Please enter the population density')
                                          
        self.lineedit2.setGeometry(50,90,320,30)
        
        self.button = QPushButton("Calculate the average deaths", self)    
        self.button.setGeometry(50,150,320,50)
        self.button.clicked.connect(self.CalcAveDeaths)
        
        self.label2 = QLabel(self)
        self.label2.setText('Average deaths = (? x rats caught) x (? x population density)')                         
        self.label2.resize(300,30)
        self.label2.move(20,260)
        
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setPlaceholderText('Please enter the multipler of the  average number of rats caught')                                        
        self.lineedit3.setGeometry(50,300,320,30)
        
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setPlaceholderText('Please enter the multiplier for the population density')
        self.lineedit4.setGeometry(50,350,320,30)
        
        self.button2 = QPushButton("Recalculate the average deaths based on these new values", self)                                   
        self.button2.setGeometry(50,400,320,50)
        self.button2.clicked.connect(self.ReCalcAveDeaths)
    
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

## Create the calculations underpining the GUI and show the results       
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

# Make application loop and exit
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())