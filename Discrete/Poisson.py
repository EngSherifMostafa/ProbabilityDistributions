import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from numpy import random

# Generate a random 1x10 distribution for occurrence 2:
x = random.poisson(lam=2, size=10)
print(x)

# We will need an array of the k values for which we will compute the Poisson PMF
k = np.arange(0, 16)
print(k)

# Calculate the Poisson PMF
pmf = poisson.pmf(k, mu=6)
pmf = np.round(pmf, 5)
for val, prob in zip(k, pmf):
    print(f"k-value {val} has probability = {prob}")

# Calculate the Poisson CDF
cdf = poisson.cdf(k, mu=6)
cdf = np.round(cdf, 3)
for val, prob in zip(k, cdf):
    print(f"k-value {val} has probability = {prob}")

# Plot Poisson CDF using step plot
# Plot Poisson PMF using bar plot
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.title("Probability Mass Function")

plt.xlabel('k')
plt.ylabel('Probability')
plt.plot(k, pmf, "bo", ms=8, label="dddddd")
plt.vlines(k, 0, pmf, colors="b", lw=5, alpha=0.5)

plt.subplot(122)
plt.title("Histogram")
plt.bar(k, pmf, align='center', alpha=0.7)
plt.xlabel('k')
plt.ylabel('Probability')
plt.show()

plt.title("Cumulative Distribution Function")
plt.plot(k, cdf, 'bo', label='CDF')
plt.step(k, cdf, where='post', label='CDF')
plt.xlabel('k')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()
# Calculate the first four moments: expectation, variance
mu = 6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print("Expectation is : \n", mean)
print("Variance is : \n", var)
print("3rd Moment is : \n", skew)
print("4th Moment is : \n", kurt)