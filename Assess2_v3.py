#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assessment 2 - The black death
"""

#import packages ? mat plot, 
import matplotlib.pyplot as plt  
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
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(rat_deaths)  
color_map.set_cmap("hot_r")
plt.yticks([])
plt.xticks([])
plt.ylabel('Patches')
plt.title("The number of rats caught per week by the 8 Rat Catchers' Patches")
plt.colorbar(orientation='horizontal', shrink=0.6, label="Number of rats caught per week", extend='max')

##Create a scatter plot of the human population
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(human_pop)  
color_map.set_cmap("Greens")
plt.xticks([])
plt.yticks([])
plt.title('Human population density in each of the 16 London Parishes')
plt.colorbar(orientation='horizontal', label="Human population density", extend='max')

# Calculate average deaths   
for i in [rat_deaths]:
    rd2 = i*0.8
for i in [human_pop]:
    hp2 = i*1.3
    
average_deaths = np.multiply(rd2, hp2)

#test calculation



# plot average deaths
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(average_deaths)  
color_map.set_cmap("Reds")
plt.xticks([])
plt.yticks([])
plt.title('Average deaths per week by geographical location')
plt.colorbar(orientation='vertical', shrink=0.8, label="Average deaths per week", extend='max')    
    


    
#calculate the total nummber of deaths by finding all the 
###total_deaths = np.unique(average_deaths, return_counts=True)  
#needs more thuinking - h9w does this fit with the parishes...?

np.unique(rd2)
np.unique(hp2)
    
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