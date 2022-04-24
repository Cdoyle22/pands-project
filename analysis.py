# Write a program that:
# 1. Outputs a summary of each variable to a single text file,
# 2. Saves a histogram of each variable to png files, and
# 3. Outputs a scatter plot of each pair of variables.
# 4. Performs any other analysis you think is appropriate

#4.1 Demonstrate the differences in each variable for each class of iris.
#4.2 Write average petal length, width, sepal length, width of each class to a text file.



#Author: Ciara Doyle


# https://code.visualstudio.com/docs/datascience/data-science-tutorial 
# shows how to use VS Code and Jupyter notebooks to view data


# %% [markdown]
# Write a program that:
# 3.1 Outputs a summary of each variable to a single text file
# 
# Import the iris.csv file to Jupyter Variables:

# %%
import pandas as pd

data = pd.read_csv ('iris.csv')


# %% [markdown]
# To understand the data and how it appears, we can print out the first two rows of the data using pandas head function:

# %%
data.head(2)

# %% [markdown]
# To summarise the count, mean standard deviation, minimum, maximum, 25 percentile, 50 percentile, 75 percentile for a specific variable (column) use the describe function:

# %%
x = data['sepal_length'].describe()
print (x)

# %% [markdown]
# Define each of the variables with the describe function to summarize:

# %%
y = data['sepal_width'].describe()
z = data['petal_length'].describe()
b = data['petal_width'].describe()
c = data['class'].describe()

# %% [markdown]
# To write the output of the summary of each variable to a text file (summaryfile.txt):

# %%
filelocation = "C:/Users/paulb/Desktop/Programming and Scripting/Project/pands-project/summaryfile.txt" 
print ("SUMMARY OF EACH VARIABLE IN THE IRIS DATASET: ", file = open (filelocation, "a")) 
print ('\r\n', file = open (filelocation, "a"))
print ('SEPAL LENGTH: ', file = open (filelocation, "a"))
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


# %% [markdown]
# 3.2 Saves a histogram of each variable to png files: 
# 
# https://www.w3schools.com/python/matplotlib_histograms.asp#:~:text=In%20Matplotlib%2C%20we%20use%20the,the%20function%20as%20an%20argument. 
# 
# https://matplotlib.org/3.5.0/gallery/statistics/hist.html 

# %%
import matplotlib.pyplot as plt
from matplotlib import colors 

#Set the figure size
plt.rcParams["figure.figsize"] = [10.00, 10.00]
plt.rcParams["figure.autolayout"] = True


# Plot the histogram
plt.hist(data['sepal_length'], color = 'pink')


#Save the histogram
plt.title ('Sepal Length')
plt.xlabel ('Sepal length')
plt.ylabel ('Count')
plt.savefig('sepal_length.png')

plt.show()

# %% [markdown]
# 3.3 Outputs a scatter plot of each pair of variables:
# 
# a) sepal length and sepal width
# b) petal length and petal width
# 
# There are 150 plotted points for each pair of variables 

# %%
import seaborn as sns
import matplotlib.pyplot as plt

x = data['sepal_length']
y = data['sepal_width']

z= data['class']

sns.scatterplot(x, y, c= 'purple', hue = z)

plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.title ('Scatter plot of each pair of Variables in iris dataset')
plt.xlabel ('Sepal length')
plt.ylabel ('Sepal_Width')
plt.show()

# %% [markdown]
# 4.1 Demonstrate the differences in each variable for each class of iris.

# %%

import seaborn as sns
import matplotlib.pyplot as plt

plot = sns.FacetGrid(data, hue="class")
plot.map(sns.histplot, "sepal_length").add_legend()

plot = sns.FacetGrid (data, hue="class")
plot.map(sns.histplot, "sepal_width").add_legend()

plot = sns.FacetGrid(data, hue="class")
plot.map(sns.histplot, "petal_length").add_legend()

plot = sns.FacetGrid(data, hue="class")
plot.map(sns.histplot, "petal_width").add_legend()

plt.show()



