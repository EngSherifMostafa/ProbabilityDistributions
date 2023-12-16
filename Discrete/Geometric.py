import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

p = 0.5

# Calculate the mean and variance and printing them
mean = stats.geom.mean(p)
variance = stats.geom.var(p)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
##########################################
x = np.arange(1, 11)
rv = stats.geom(p)

# Calculate the(PMF) for the given x values and plotting it
pmf = rv.pmf(x)

plt.plot(x, pmf, 'bo', ms=8, label='PMF')
plt.vlines(x, 0, pmf, colors='b', lw=5, alpha=0.5)
plt.title('Probability Mass Function')
plt.show()

# Calculate the (CDF) for the given x values and plotting it
cdf = rv.cdf(x)

plt.step(x, cdf, where='post', color='r', label='CDF')
plt.title('Cumulative Distribution Function')
plt.show()