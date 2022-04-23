# Write a program that:
# 1. Outputs a summary of each variable to a single text file

# Assumption: Variable is equal to column data in the iris.csv file

# Author: Ciara Doyle

import os

print (os.chdir)

import pandas as pd
import numpy as np
data = pd.read_csv ('iris.csv')

x = data['sepal_length'].describe() # Define each variable and use describe function to get summary details
y = data['sepal_width'].describe()
z = data['petal_length'].describe()
b = data['petal_width'].describe()
c = data['class'].describe()

filelocation = "C:/Users/paulb/Desktop/Programming and Scripting/Project/pands-project/summaryfile.txt" 

print ("SUMMARY OF EACH VARIABLE IN THE IRIS DATASET: ", file = open (filelocation, "a")) # Write a heading to the text file
print ('\r\n', file = open (filelocation, "a")) # Write a empty line to the text file (formatting purposes)
print ('SEPAL LENGTH: ', file = open (filelocation, "a")) # Write the summary details of each variable to the text file
print(x, file = open (filelocation, "a"))
print ('\r\n', file = open (filelocation, "a"))
print ('SEPAL WIDTH: ', file = open (filelocation, "a"))
print(y, file = open (filelocation, "a"))
print ('\r\n', file = open (filelocation, "a"))
print ('PETAL LENGTH: ', file = open (filelocation, "a"))
print(z, file = open (filelocation, "a"))
print ('\r\n', file = open (filelocation, "a"))
print ('PETAL WIDTH: ', file = open (filelocation, "a"))
print(b, file = open (filelocation, "a"))
print ('\r\n', file = open (filelocation, "a"))
print ('CLASS: ', file = open (filelocation, "a"))
print(c, file = open (filelocation, "a"))
print ('\r\n', file = open (filelocation, "a"))





