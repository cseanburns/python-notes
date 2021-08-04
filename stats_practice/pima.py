#!/usr/bin/python3

import pandas as pd

# Importing data from URL
pima = pd.read_csv('http://heather.cs.ucdavis.edu/FasteR/data/Pima.csv', header = 0)

# cf. to R's dim(df)
pima.shape # equiv to R's dim(df)

# cf. to R table()
pima.test.value_counts()
pima["test"].value_counts()
