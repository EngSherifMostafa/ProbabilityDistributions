import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Set the parameters for the binomial distribution
n = 30 # Number of trials
p = 0.5 # Probability of success

# Generate random variables from the binomial distribution
sample_size = 100
random_vars = binom.rvs(n, p, size=sample_size)

# Calculate the mean and variance
mean = binom.mean(n, p)
variance = binom.var(n, p)

# Plot the PMF
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)
plt.stem(x, pmf, basefmt=' ', label='PMF')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.title('Binomial Distribution - PMF')
plt.legend()
plt.show()

# Plot the CDF
cdf = binom.cdf(x, n, p)
plt.plot(x, cdf, 'bo', label='CDF')
plt.step(x, cdf, label='CDF', where='post')
plt.xlabel('Random Variable')
plt.ylabel('Cumulative Probability')
plt.title('Binomial Distribution - CDF')
plt.legend()
plt.show()

# Print the mean and variance
print("Mean:", mean)
print("Variance:", variance)
