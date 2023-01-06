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
plt.clf() # clear plot
heights.boxplot()
plt.show()
plt.clf()

# Generate a histogram
pd.DataFrame.hist(heights)
plt.show()
plt.clf()
heights.hist()
plt.show()
plt.clf()

# Get the names of the variables
heights.columns

# Generate a scatter plot
heights.plot.scatter(x = 'Height3', y = 'Height20')
plt.show()

# Generate a multi-line plot
heights.plot.line()
plt.show()

## Linear Regression

### Method 1 (More like R output by default)
import statsmodels.api as sm
x = heights['Height3']
x = sm.add_constant(x)
y = heights['Height20']
model1 = sm.OLS(y, x).fit()
predictions = model1.predict(x)
print_model = model1.summary()
print(print_model)

### Method 2
from sklearn.linear_model import LinearRegression
x = heights['Height3']
x = sm.add_constant(x)
y = heights['Height20']
model2 = LinearRegression()
model2.fit(x,y)
r_sq = model2.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model2.intercept_)
print('slope:', model2.coef_)
