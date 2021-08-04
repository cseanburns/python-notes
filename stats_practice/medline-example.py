#!/usr/bin/python3

# pandas tutorial:
# https://pandas.pydata.org/pandas-docs/stable/10min.html
# the data here is based on a real research project, but this is just practicing
# with pandas
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data file
searches = pd.read_csv('data/data.csv')

# look at data
print(searches)
searches.head(5)

# summary, descriptive statistics of data frame
searches.describe()

# basic scatterplot
plt.scatter(searches['pubmed'], searches['ovid'])
plt.title("PubMed and Ovid Search Counts")
plt.xlabel("PubMed")
plt.ylabel("Ovid")
plt.show()

plt.scatter(searches['pubmed'], searches['proquest'])
plt.title("PubMed and ProQuest Search Counts")
plt.xlabel("PubMed")
plt.ylabel("Proquest")
plt.show()

plt.scatter(searches['pubmed'], searches['ebscohost'])
plt.title("PubMed and EBSCOhost Search Counts")
plt.xlabel("PubMed")
plt.ylabel("EBSCOhost")
plt.show()

plt.scatter(searches['pubmed'], searches['wos'])
plt.title("PubMed and WoS Search Counts")
plt.xlabel("PubMed")
plt.ylabel("WoS")
plt.show()
