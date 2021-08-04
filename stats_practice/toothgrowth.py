#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
 
# export ToothGrowth data from R and import csv file using pandas
"""
write.csv(ToothGrowth,
          file = 'ToothGrowth.csv', row.names = FALSE)``
"""
ToothGrowth = pd.read_csv('data/ToothGrowth.csv')
ToothGrowth.head()
tg = ToothGrowth
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

# We can convert the supp variable to a category:
tg['suppC'] = tg["supp"].astype('category')

# group by, part 1
grouped = tg.groupby('suppC')
grouped.describe()

# group by, part 2 
import numpy as np
grouped.aggregate(np.sum)
grouped.aggregate(np.mean)

grouped.agg([np.sum, np.mean, np.std])

(grouped.agg([np.sum, np.mean, np.std])
        .rename(columns = {'sum': 'Sum',
                           'mean': 'Mean',
                           'std': 'StDev'}))


