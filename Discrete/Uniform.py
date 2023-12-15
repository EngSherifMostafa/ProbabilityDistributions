import numpy as np
import matplotlib.pyplot as plt

# Define the interval [a, b]
a = 1
b = 5

# Generate uniform random variable
uniform_data = np.random.uniform(a, b, size=1000)

# Calculate mean and variance
mean = np.mean(uniform_data)
variance = np.var(uniform_data)

# Probability Mass Function (pmf)
def uniform_pmf(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0

# Cumulative Distribution Function (cdf)
def uniform_cdf(x, a, b):
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    else:
        return 1

# Print mean and variance
print("Mean:", mean)
print("Variance:", variance)

# Plot the histogram of the generated data
plt.hist(uniform_data, bins=20, density=True, alpha=0.5, color='g', label='Histogram')

# Plot the probability mass function (pmf)
x_values = np.linspace(a - 1, b + 1, 100)
pmf_values = [uniform_pmf(x, a, b) for x in x_values]
plt.plot(x_values, pmf_values, 'r-', label='PMF')

# Plot the cumulative distribution function (cdf)
cdf_values = [uniform_cdf(x, a, b) for x in x_values]
plt.plot(x_values, cdf_values, 'b-', label='CDF')

plt.title('Uniform Distribution')
plt.xlabel('Random Variable')
plt.ylabel('Probability')
plt.legend()
plt.show()
