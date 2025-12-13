import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# average
mu = np.array([0, 0])
# var, cov mat
#Sigma = np.array([[1, 0.5],
#                  [0.5, 1]])
Sigma = np.array([[0.1, 0.05],
                  [0.05, 0.1]])



# create grid
x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
pos = np.dstack((x, y))

# 2D ND PDF
rv = multivariate_normal(mu, Sigma)
pdf = rv.pdf(pos)

plt.contourf(x, y, pdf, levels=50, cmap='viridis')
plt.colorbar()
plt.show()

