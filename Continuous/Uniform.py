import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Set the parameters for the uniform distribution
a = 7  # Lower bound
b = 12 # Upper bound

# Generate random variables from the uniform distribution
sample_size = 1
random_vars = uniform.rvs(loc=a, scale=b-a, size=sample_size)

# Calculate the mean and variance
mean = uniform.mean(loc=a, scale=b-a)
variance = uniform.var(loc=a, scale=b-a)

# Plot the PDF
x = np.linspace(a-1 , b+1, 1000)
pdf = uniform.pdf(x, loc=a, scale=b-a)
plt.plot(x, pdf, label='PDF')
plt.xlabel('Random Variable')
plt.ylabel('Probability Density')
plt.title('Uniform Continuous Distribution - PDF')
plt.legend()
plt.show()

# Plot the CDF
x_cdf = np.linspace(a-1, b+1, 1000)
cdf = uniform.cdf(x_cdf, loc=a, scale=b-a)
plt.plot(x_cdf, cdf, label='CDF')
plt.xlabel('Random Variable')
plt.ylabel('Cumulative Probability')
plt.title('Uniform Continuous Distribution - CDF')
plt.legend()
plt.show()

# Print the mean and variance
print("Mean:", mean)
print("Variance:", variance)
