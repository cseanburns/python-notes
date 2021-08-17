# t-test in Pandas

I posted this on [The Text][1], but add it here for future reference.

There are three specific [data structures][6] in [pandas][2] that have distinct attributes and methods. The first two are the main structures for analyzing data:

- [Series][3], like R vectors
- [DataFrame][4], like R dataframes
- [Index][5]

To get started:

```
import pandas as pd
import numpy as np

# create data as Python list
tortillas = [2.1, 2.0, 1.9, 1.7, 2.3, 2.2, 2.0, 2.4, 2.1, 1.9, 2.1, 2.3, 2.0, 2.4]

# get basic stats on list using numpy
np.mean(tortillas)
np.median(tortillas)
np.max(tortillas) - np.min(tortillas)
np.std(tortillas)
round(np.std(tortillas), 2)

# convert list to pandas Series and get basic stats 
tort2 = pd.Series(tortillas, copy = True)
pd.Series.mean(tort2)
pd.Series.median(tort2)
pd.Series.mode(tort2)
pd.Series.max(tort2) - pd.Series.min(tort2)
pd.Series.describe(tort2)
pd.Series.le(tort2, 2.0)

# However, because a pandas Series has its own attributes, we can some shorthand:
tort2.mean()
tort2.median()
tort2.mode()
tort2.max() - tort2.min()
tort2.describe()
tort2.le(2.0) # return Booleans less than 2.0 
```

To perform a **t test**, we need another library, and here [SciPy][7] is common. For a one sample **t test**, I wanted to know if the observed mean was different from a mean of 2.0, which is what I was aiming to get when I was measuring out the dough:

```
from scipy.stats import ttest_1samp

# works on pd.Series or Python Lists
ttest_1samp(tort2, 2.0)
ttest_1samp(tortillas, 2.0)
# These results agree with my R results:
Ttest_1sampResult(statistic=1.8358568490953695, pvalue=0.08934987597048166)
# Save the results
tscore, pvalue = ttest_1samp(tort2, 2.0)
print('t test equals: ', round(tscore, 3))
print('p value equals: ', round(pvalue, 3))
```

It seems that I'd have to calculate the confidence intervals myself if I only used SciPy, but there's a library called [pingouin][8] that can report the important details for the test:

```
import pingouin as pg
pg.ttest(tort2, 2.0)
               T  dof alternative    p-val         CI95%   cohen-d   BF10     power
T-test  1.835857   13   two-sided  0.08935  [1.98, 2.22]  0.490653  1.015  0.397749
```

And the results are the same for the R version of this.

Some [comparisons between R and pandas][9].


[1]:https://cseanburns.net/WWW/index.html#measuring-food-with-pandas
[2]:https://pandas.pydata.org/docs/index.html
[3]:https://pandas.pydata.org/docs/reference/api/pandas.Series.html
[4]:https://pandas.pydata.org/docs/reference/frame.html
[5]:https://pandas.pydata.org/docs/reference/api/pandas.Index.html
[6]:https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html
[7]:https://docs.scipy.org/doc/scipy/reference/stats.html
[8]:https://pingouin-stats.org/index.html
[9]:https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_r.html

