import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# average, standard deviation
mu = 1
sigma = 0.5

# range of x
x = np.linspace(-5, 5, 200)

# PDF
pdf = norm.pdf(x, mu, sigma)

# CDF
cdf = norm.cdf(x, mu, sigma)

plt.plot(x, pdf, label='PDF')
plt.plot(x, cdf, label='CDF')
plt.legend()
plt.show()

