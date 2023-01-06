# Basic Linear Regression in Python
import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([30, 30, 32, 33, 34, 35, 36, 38, 40, 41, 41, 43, 45, 45, 47, 48]).reshape((-1, 1))
y = np.array([59, 63, 62, 67, 65, 61, 69, 66, 68, 65, 73, 68, 71, 74, 71, 75])
print(y)
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# Another method, which provides more info like R
import numpy as np
import statsmodels.api as sm
x = np.array([30, 30, 32, 33, 34, 35, 36, 38, 40, 41, 41, 43, 45, 45, 47, 48]).reshape((-1, 1))
y = np.array([59, 63, 62, 67, 65, 61, 69, 66, 68, 65, 73, 68, 71, 74, 71, 75])
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
print(results.summary())

# Save Python History
import readline
readline.write_history_file('/home/sean/pylinregression')
