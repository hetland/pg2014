# Rob Hetland
# 2014-09-30
#
#  Plot data based on the polynomial:
# y = 0.01 * x**2 + 0.33 * x + 2.3 + 20 * np.random.randn(1000)

import numpy as np
import matplotlib.pyplot as plt

x, y = np.load('polynomial_data.npy').T
psol = np.polynomial.Polynomial.fit(x, y, 2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'k.')
xpoly = np.linspace(0.0, 100.0, 101)
ax.plot(xpoly, psol(xpoly), 'r-', lw=3.0)
plt.show()

