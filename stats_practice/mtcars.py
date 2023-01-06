#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

# Let's export the mtcars data from R
"""
write.csv(mtcars, file = 'data/mtcars.csv', row.names = TRUE)
"""
mtcars = pd.read_csv('data/mtcars.csv')
mtcars.head()
# Below, make the R rownames into its own column
mtcars = mtcars.rename(columns = {"Unnamed: 0": "Make"})
mtcars.head()
mtcars.loc[:, 'mpg'] # Get the second column named 'mpg'

# Scatterplot, two variables
mtcars.plot.scatter(x = 'wt', y = 'mpg')
plt.show()

# Area plot, one variable
mtcars.plot.area(y = 'mpg')
plt.show()

# Histogram, one variable
mtcars['mpg'].plot.hist()
plt.show()
mtcars.hist(column = 'mpg')
plt.show()


