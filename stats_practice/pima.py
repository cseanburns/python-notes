#!/usr/bin/python3

import pandas as pd

"""
Importing data from URL. Note that since we're using 'pd.read_csv', the data
will automatically be a pandas.DataFrame
"""
pima = pd.read_csv('http://heather.cs.ucdavis.edu/FasteR/data/Pima.csv', header = 0)

"""
Cf. ``df.shape`` to R's ``dim(df)``
Note on when to use paranthesis

We write pima.shape and not pima.shape() because DataFrame.shape is a **property**

See the documentation at
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html

At the top of the page, the documentation is helpful here in that it states:

*property* DataFrame.shape

Compare that to something like a method, such as DataFrame.bool()
Also, try ``help(DataFrame.bool`` in the Python IDLE

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bool.html

Near the top of the page, the document refers to:

DataFrame.bool()
"""
pima.shape # equiv to R's dim(df)

# cf. to R table()
pima.test.value_counts()
pima["test"].value_counts()
