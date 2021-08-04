#!/usr/bin/python3

# Helpful R comparison to pandas
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html

## Based on Matloff's fasteR

## Lesson 1: First Python3/Pandas Steps

import pandas as pd
import matplotlib.pyplot as plt

# export nile data from R and import csv file using pandas
# ``write.csv(nile, file = 'nile.csv', row.names = FALSE)``
# import csv file using pandas
nile = pd.read_csv('data/nile.csv', header = None)

# Get column names
list(nile)

# Get dimensions of df
nile.shape

# get mean
nile.mean()
nile.mean(axis = 0)

# get histogram of the the second column
nile.hist(column = 1)
plt.show()

# get histogram, bin by 10 instead of default
nile.hist(bins = 10, column = 1)
nile.hist(bins = 10, column = 1, grid = False)
plt.show()

# get a scatterplot
nile.plot.scatter(0, 1)
plt.show()
nile.plot.scatter(0, 1, colormap = 'viridis')
plt.show()

# to get help:
help(plt)

# access/slice individual elements in a vector
# access the first row 
nile[0:1]
# access the second row 
nile[1:2]
# access first row, second column
nile.iloc[0,1]

# build a vector/list
x = [2, 5, 6]

# mean of sliced rows
# this is different than how R slices, where the equivalent is:
# mean(Nile[80:100])
nile[79:100].mean()
# get mean of part of second column
nile[1][79:100].mean()

# make a copy
n80100 = nile[79:100]
# get mean 
n80100.mean()
# get standard deviation
n80100.std()

# just to compare
n80100[0:1]
nile[79:80]

# length of vector
len(nile)

## Lesson 2: More on Vectors

# Sum some numbers
sum([5, 12, 13])

# How many times the river exceeded 1200 (2nd column)
# There's got to be a better way
n1200 = nile > 1200 # converts to true and false
n1200.value_counts() # provides a count of both the Trues and Falses

# a better way
nile.loc[nile[1] > 1200]
len(nile.loc[nile[1] > 1200])

## Lesson 3: Data Frames

# export ToothGrowth data from R and import csv file using pandas
#write.csv(ToothGrowth, file = 'ToothGrowth.csv', row.names = FALSE)

ToothGrowth = pd.read_csv('data/ToothGrowth.csv')
ToothGrowth.head()
tg = ToothGrowth

# Get the mean of the 'len' column
tg.len.mean()

# couple of ways to access a cell in a data frame
# one by positions, the next using a column label
tg.iat[2,0]
tg.at[2, 'len']

# extract subset of a data frame
tg.loc[1:4, ['len', 'dose']]

# get a column
tg.loc[:, 'len']

# length of dataframe
len(tg)
len(tg.loc[:, 'len'])
len(tg.loc[:, 'supp'])
len(tg.loc[:, 'dose'])
tg.loc[:, 'len'].head()
tg.loc[:, 'len'].head(n = 10)

# Create a dataframe from two lists
x = [5, 12, 13]
y = ['abc', 'de', 'z']
d = pd.DataFrame({'x': x, 'y': y})

# Create a dataframe from two lists
# create two lists
# use pandas to make a dataframe out of the lists with a dictionary 
x = [5, 12, 13]
y = ['abc', 'de', 'z']
d = pd.DataFrame({'x':x, 'y':y})

## Lesson 4: Factor Class

# We can convert the supp variable to a category:
tg['suppC'] = tg["supp"].astype('category')

# This kind of works but there will be a better way that I need to find:
grouped = tg.groupby('suppC')
grouped.describe()

# This works a little better:
import numpy as np
grouped.aggregate(np.sum)
grouped.aggregate(np.mean)

## Lesson 5: Apply (cf. to tapply function)

grouped.agg([np.sum, np.mean, np.std])

(grouped.agg([np.sum, np.mean, np.std])
        .rename(columns = {'sum': 'Sum',
                           'mean': 'Mean',
                           'std': 'StDev'}))

# Let's export the mtcars data from R
# ``write.csv(mtcars, file = 'mtcars.csv', row.names = TRUE)``
mtcars = pd.read_csv('data/mtcars.csv')
mtcars.head()
# Below, make the R rownames into its own column
mtcars = mtcars.rename(columns = {"Unnamed: 0": "Make"})
mtcars.head()
mtcars.loc[:, 'mpg'] # Get first column

## Lesson 6: Data Cleaning

pima = pd.read_csv('http://heather.cs.ucdavis.edu/FasteR/data/Pima.csv',
        header = 0)
pima.shape # equiv to R's dim(df)
# below two are the best I can find that are cf to R table()
pima.glucose.value_counts()
pima["glucose"].value_counts()
