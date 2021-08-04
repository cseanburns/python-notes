#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

# Regular plot with two lines
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth = 2, markersize = 12, label = "First")
plt.plot(x, y2, "go-", linewidth = 2, markersize = 12, label = "Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc = "upper left")
plt.show() # or to save the plot: plt.savefig("myplot.pdf")

# Plotting logspace
x = np.logspace(-1, 1, 40)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x, y1, "bo-", linewidth = 2, markersize = 12, label = "First")
plt.loglog(x, y2, "go-", linewidth = 2, markersize = 12, label = "Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([1, 10, 1, 100])
plt.legend(loc = "upper left")
plt.show() # Or to save: plt.savefig("mylogplot.pdf")

# Histograms
x = np.random.normal(size = 1000)
plt.hist(x)
plt.hist(x, bins = np.linspace(-5, 5, 21));

## Gamma distribution
x = np.random.gamma(2, 3, 100000)
plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative = 30)
plt.subplot(224)
plt.hist(x, bins = 30, cumulative = 30, histtype = "step")
plt.show()
