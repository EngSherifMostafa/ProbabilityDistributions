import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1
b = 6

# Generate values for X using numpy.random.uniform
values = np.random.uniform(a, b+1, 1000)  # Generating 1000 samples

# Calculate mean and variance
mean = np.mean(values)
variance = np.var(values)
values = np.arange(a, b+1)
pmf = np.ones_like(values) / (b - a + 1)
# Plot PMF using plt.plot
plt.plot(values, pmf, marker='o', linestyle='', color='blue')
plt.title('Probability Mass Function (PMF) of X')
plt.xlabel('X')
plt.ylabel('P(X)')


#Plot PMF using plt.vlines
plt.vlines(values, ymin=0, ymax=pmf, colors='blue', linestyle='-', linewidth=2)
plt.title('Probability Mass Function (PMF) of X')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.show()


# Display mean and variance
print(f'Mean (μ): {mean}')
print(f'Variance (σ^2): {variance}')
