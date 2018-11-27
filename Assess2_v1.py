#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assessment 2 - The black death
"""

#import packages ? mat plot, 
import matplotlib.pyplot as plot  
import numpy as np
import csv
import os
import pandas as pd


#create 
rat_deaths = []
human_deaths = []
rat_catchers = ["Oliver", "John", "Charlie", "Steve", "David", "Little John", "Robin"]


# import raster data

f = open('death.rats.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rats = []				
    for value in row:	              
        rats.append(value)		  
    rat_deaths.append(rats)      
f.close() 

f = open('death.parishes.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    people = []				
    for value in row:	              
        people.append(value)		  
    human_deaths.append(people)     
f.close()

##Create a scatter plot of the rat deaths
plot.ylim(0, 400)
plot.xlim(0, 400)
color_map = plot.imshow(rat_deaths)  
color_map.set_cmap("hot_r")
plot.yticks([])
plot.xticks([])
plot.ylabel('Patches')
plot.title("Rat deaths by Rat Catcher's Patch")
plot.colorbar(orientation='horizontal', shrink=0.45, label="Number of rat deaths")





##Create a scatter plot of the human deaths
plot.ylim(0, 400)
plot.xlim(0, 400)
plot.imshow(human_deaths)
plot.xlabel('x coordinate')
plot.ylabel('y coordinate')
plot.title('Human deaths by London Parish')
plot.show()



for i in range(len(data)):
    for j in range(len(data[j])):
	data[i][j] = 10
    
# to compare two @D arrayes e.g one map on top of the other as long as they are the same size
    #NB boundary issues. Assuming no data missing then just need to do it for the data we have then stop
    #see lecture notes on control flow
for i in range(len(dataA)):
    for j in range(len(dataA[i])):
	dataA[i][j] = dataB[i][j]


#display the two images

# calculate the 