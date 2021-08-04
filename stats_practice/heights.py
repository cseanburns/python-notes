#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

## Basic Vectors (or lists)

# build a vector
x = [2, 5, 6]

# Sum some numbers
sum([5, 12, 13])

## Data Frames

# Create a dataframe from two lists
# First create two lists
# Join the two lists
x = [5, 12, 13]
y = ['abc', 'de', 'z']
d = pd.DataFrame({'x':x, 'y':y})

## Heights Dataframe

# Read and label data
heights = pd.read_csv("data/height.csv", header = 0)
heights = pd.DataFrame(heights.values, columns = ['Height3', 'Height20'])

# Confirm data type
type(heights)

# Look at the head; two ways
pd.DataFrame.head(heights)
heights.head()

# Describe data frame (like R ``summary``)
pd.DataFrame.describe(heights)        
heights.describe()

# Generate a boxplot
pd.DataFrame.boxplot(heights)
plt.show()
heights.boxplot()
plt.show()

# Generate a histogram
pd.DataFrame.hist(heights)
plt.show()
heights.hist()
plt.show()

# Get the names of the variables
heights.columns

# Generate a scatter plot
heights.plot.scatter(x = 'Height3', y = 'Height20')
plt.show()

# Generate a multi-line plot
heights.plot.line()
plt.show()

## Linear Regression

## Note: these two methods disagree; need to understand why

### Method 1
x = heights[['Height3']]
y = heights[['Height20']]

import statsmodels.api as sm
model1 = sm.OLS(x,y)
results = model1.fit()
print(results.summary())

### Method 2
from sklearn.linear_model import LinearRegression
model2 = LinearRegression()
model2.fit(x,y)
r_sq = model2.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
