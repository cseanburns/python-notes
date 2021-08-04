## Vectors

### Create a list of integers:

```
# tuple
x = (1, 2, 3, 4) 
x = ("one", "two", "three", "four") # tuple

# list
x = ([1, 2, 3, 4) 

# string vector
import pandas as pd
x = pd.Series(["a", "b", "c"], dtype="string") # string
# Or:
x = (["a", "b", "c"]) # string
x = x.astype("string")

# Boolean
x = (True, False, True, False)
x = ([True, False, True, False])

# NaN
import numpy as np
x = (1, 2, np.nan, 3)
x = ([1, 2, np.nan, 3])

# Concatenate two lists/tuples
x = (1, 2, 3)
y = (4, 5, 6)
z = x + y

# Sum two lists/tuples
z = np.add(x, y)

# Category data
z = pd.Series(z, dtype="category")

# Factorize
z = pd.factorize(z)

# Generate a normal distribution
# (mean, sd, length)
x = np.random.normal(1, 0.5, 20) 
```

### Create a dataframe:

```
# Import CSV file
df = pd.read_csv('data.csv')

# Create from existing vectors
a = (1, 2, 3, 4, 5)
b = (5.4, 3.3, 2.5, 6.2, 2.9)
# Create a template
data = { 'A': a, 'B': b }
# Create the dataframe
data = pd.DataFrame(data)
```

### Slicing a dataframe:

```
# retrieve the first three rows
data[:3]
# exclude the last two rows
data[:-2]
# retrieve the first column
data['A']
# retrieve the item in data.iloc[row, column]
# row 2, column 2:
data.iloc[1,1]
# row 5, column 1:
data.iloc[4,0]
```

### Manipulate data in a data frame

```
data.iloc[4,0] + 100
data.iloc[4,0] / 2.3
np.log(data.iloc[4,0])
data['A'] * 2
```

### Add a column/variable to a data frame

```
data.head() # look at the top of the data frame
data['C'] = data['A'] * 2
data['C'] = np.log(data['A'])
```

### Categorize a column

```
# data.csv
x,y,z
1,5.5,"young"
2,3.4,"young"
3,2.5,"old"
4,6.3,"young"
5,2.9,"old"

# Category data
df = pd.read_csv("data.csv")
df2 = df2.copy()
df2['z'] = df2['z'].astype('category')
df2['z'] = df2['z'].cat.codes

# Ordinal data
df = pd.read_csv("data.csv")
df['z'] = df['z'].astype('category')
df['z'] = df['z'].cat.reorder_categories(['young','old'], ordered = True)
df2['z'] = df2['z'].cat.codes
```

### Descriptive stats

```
np.min(df['y'])
np.max(df['y'])
np.round(df['y'])
np.max(df['y']) - np.min(df['y'])
np.sum(df['y'])
from scipy.stats import rankdata
df['y2'] = rankdata(df['y'])
np.quantile(df['y'], 0.25)
np.quantile(df['y'], 0.50)
np.quantile(df['y'], 0.75)
np.var(df['y'])
np.std(df['y'])
np.mean(df['y'])
np.median(df['y'])
len(df['y'])
plt.hist(df['y'])
plt.show()
x = np.random.normal(1, 0.5, 1000)
plt.hist(x)
plt.show()
y = np.random.normal(2, 1.4, 1000)
np.corrcoef(x, y)
from scipy.stats.stats import pearsonr
pearsonr(x, y) # correlation and significance
```

### Linear regression

Using the cars data from R.

```
imort numpy as np
import pandas as pd
import statsmodels.api as sm
df = pd.read_csv('cars.csv')
df.head()
type(df)
lm = sm.OLS.from_formula('speed ~ dist', df)
result = lm.fit()
print(result.summary())
```

This was helpful for the linear regression:
http://www.science.smith.edu/~jcrouser/SDS293/labs/lab2-py.html

Create a scatter plot of the cars data.

```
import matplotlib.pyplot as plt
df.plot(kind = 'scatter',
x = 'dist',
y = 'speed',
color = 'red',
title = 'Cars Data from R')
```
