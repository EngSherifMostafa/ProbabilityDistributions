import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the Gaussian distribution
mu = 0      # Mean
sigma = 1   # Standard deviation

# Generate random variables from the Gaussian distribution
sample_size = 1000
random_vars = np.random.normal(loc=mu, scale=sigma, size=sample_size)

# Calculate the mean and variance
mean = np.mean(random_vars)
variance = np.var(random_vars)

# Print the mean and variance
print("Mean:", mean)
print("Variance:", variance)

# Plot the PDF
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
plt.plot(x, pdf, label='PDF')
plt.xlabel('Random Variable')
plt.ylabel('Probability Density')
plt.title('Gaussian Continuous Distribution - PDF')
plt.legend()
plt.show()

# Plot the CDF
sorted_vars = np.sort(random_vars)
cdf = np.linspace(0, 1, sample_size)
plt.plot(sorted_vars, cdf, label='CDF')
plt.xlabel('Random Variable')
plt.ylabel('Cumulative Probability')
plt.title('Gaussian Continuous Distribution - CDF')
plt.legend()
plt.show()
