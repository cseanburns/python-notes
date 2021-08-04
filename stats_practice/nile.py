#!/usr/bin/python3

# Helpful R comparison to pandas
# Based on Matloff's fasteR
# Comparisons to R:
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html
# https://www.mit.edu/~amidi/teaching/data-science-tools/conversion-guide/r-python-data-manipulation/

## Basic pandas and matplotlib 

import pandas as pd
import matplotlib.pyplot as plt

# import csv file using pandas
nile = pd.read_csv('data/nile.csv', header = None)

# quick look
nile.head()

nile = nile.rename(columns = {0: 'year', 1: 'flow'})

# get mean of both columns
nile.flow.mean()

# get help
help(plt)

# create histogram
nile.flow.hist()
plt.show()

# create histogram, set bin 50
nile.flow.hist(bins = 50)
plt.show()

# access/slice individual elements in a vector
# start with row 1 (skip row 0)
nile[1:]
# select first row (row 0; column 1)
nile[:1] # or nile[0:1]
# select the first two rows
nile[:2] # or nile[0:2]
# access the first second rows 
nile[1:3]

# mean of sliced rows
# this is different than how R slices, where the equivalent is:
# mean(Nile[80:100])
nile[79:100].mean()

# make a copy
n80100 = nile[79:100]
# get mean 
n80100.mean()
# get standard deviation
n80100.std()

# just to compare
n80100[0:1]
nile[79:80]

# length of data 
len(nile)

## How many times the river exceeded 1200?
# converts to true and false
n1200 = nile > 1200
# provides a count of both the Trues and Falses for both columns
n1200.flow.value_counts()

nile.loc[nile['flow'] > 1200]
len(nile.loc[nile['flow'] > 1200])


