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
r_d = []
h_pop = []
rat_catchers = ["Oliver", "John", "Charlie", "Steve", "David", "Little John", "Robin"]


# import raster data

f = open('death.rats.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rats = []				
    for value in row:	              
        rats.append(value)		  
    r_d.append(rats)      
f.close() 

f = open('death.parishes.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    people = []				
    for value in row:	              
        people.append(value)		  
    h_pop.append(people)     
f.close()

# Convert imported data to numpy arrays
rat_deaths = np.array(r_d) 
human_pop = np.array(h_pop)

##Create a scatter plot of the rat deaths
plot.ylim(0, 400)
plot.xlim(0, 400)
color_map = plot.imshow(rat_deaths)  
color_map.set_cmap("hot_r")
plot.yticks([])
plot.xticks([])
plot.ylabel('Patches')
plot.title("The number of rats caught per week by the 8 Rat Catchers' Patches")
plot.colorbar(orientation='horizontal', shrink=0.45, label="Number of rats caught per week")

##Create a scatter plot of the human population
fig, ax = plot.subplots()
plot.ylim(0, 400)
plot.xlim(0, 400)
color_map = plot.imshow(human_pop)  
color_map.set_cmap("hot_r")
plot.xlabel('x coordinate')
plot.ylabel('y coordinate')
plot.title('Human population density in each of the 16 London Parishes')
plot.colorbar(orientation='horizontal', shrink=0.8, label="Human population density")

for (i, j), z in np.ndenumerate(human_deaths):
    ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center')
plot.show()

for (j,i),label in np.ndenumerate(human_deaths):
    text(label,ha='center',va='center')
    ax2.text(i,j,label,ha='center',va='center')

# Calculate average deaths   
for i in [rat_deaths]:
    rd2 = i*0.8
for i in [human_pop]:
    hp2 = i*1.3
    
average_deaths = np.multiply(rd2, hp2)

# plot average deaths

fig, ax = plot.subplots()
plot.ylim(0, 400)
plot.xlim(0, 400)
color_map = plot.imshow(average_deaths)  
color_map.set_cmap("hot_r")
plot.xlabel('x coordinate')
plot.ylabel('y coordinate')
plot.title('Average deaths per week')
plot.colorbar(orientation='horizontal', shrink=0.8, label="Average deaths per week")    
    
    
    
    
    
    
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