#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assessment 2 - The black death
"""

# Import the packages required for this program
import matplotlib.pyplot as plt  
import matplotlib.image as mpimg
import numpy as np
import csv
import os
import pandas as pd

#Create lists to import the raster data into
r_d = []
h_pop = []

# Import the raster data files
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

# Convert the imported data to numpy arrays
rat_deaths = np.array(r_d) 
human_pop = np.array(h_pop)

# Create a map of the rat deaths
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(rat_deaths)  
color_map.set_cmap("hot_r")
plt.yticks([])
plt.xticks([])
plt.ylabel('Patches')
plt.title("The number of rats caught per week by \n the 8 Rat Catchers' Patches")
plt.colorbar(orientation='horizontal', shrink=0.5, label="Number of rats caught per week", extend='max')
plt.savefig("rats.png", bbox_inches='tight', pad_inches=0.0)

# Create a map of the human population density
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(human_pop)  
color_map.set_cmap("Greens")
plt.xticks([])
plt.yticks([])
plt.title('Human population density in each \n of the 16 London Parishes')
plt.colorbar(orientation='horizontal', shrink=0.5, label="Human population density", extend='max')
plt.savefig("humanpop.png", bbox_inches='tight', pad_inches=0.0)

# Calculate the average deaths based on the equation
# deaths = (0.8 x rat deaths) x (1.3 x population density)  
for i in [rat_deaths]:
    rd2 = i*0.8
for i in [human_pop]:
    hp2 = i*1.3
    
average_deaths = np.multiply(rd2, hp2)

#save the deaths as a excel file - seems to work ok
with open('ave_deaths.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerows(average_deaths)	    
f.close() 

#save the deaths as a text file - works ok
with open('ave_deaths.txt', "w") as f:
    writer = csv.writer(f)
    writer.writerows(average_deaths)	    
f.close() 


# Create a map of the average deaths
plt.ylim(0, 400)
plt.xlim(0, 400)
color_map = plt.imshow(average_deaths)  
color_map.set_cmap("Reds")
plt.xticks([])
plt.yticks([])
plt.title('Average deaths per week \n by geographical location')
plt.colorbar(orientation='horizontal', shrink=0.8, label="Average deaths per week", extend='max')    
plt.savefig("ave_deaths.png", bbox_inches='tight', pad_inches=0.0)  

#Plot all three images together
img1 = mpimg.imread('rats.png')
img2 = mpimg.imread('humanpop.png')
img3 = mpimg.imread('ave_deaths.png')
fig = plt.figure(figsize=(12,12), dpi=100)
fig.add_subplot(1,3,3)
plt.subplot(1,3,1)
plt.axis('off')
plt.imshow(img1)  
plt.subplot(1,3,2)
plt.axis('off')
plt.imshow(img2)
plt.subplot(1,3,3)
plt.axis('off')
plt.imshow(img3)

# Calculating the total number of deaths over the 16 parishes TO FINISH!!!!!
total_deaths = np.sum(average_deaths)
print("The total number of deaths over the 16 parishes per week is " + str(int(round(total_deaths,None)))) #rounds correctly)
