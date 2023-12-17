from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

n_ofEarthQuack = 20
n_ofyears = 22
mean = n_ofyears / n_ofEarthQuack  # lambda = 1/mean

# What is the probability of the next earthquake in the next 6 months?
time_period = 0.5  # 6 months
x = 1 / (mean * 12)  # Rate lambda for 1 event per mean years
probability_next_6_months = expon.pdf(time_period, scale=1 / x)

print("Probability of earthquake in the next 6 months:", probability_next_6_months)

# Plot the PDF and CDF for visualization
x_values = np.linspace(0, 5, 100)
pdf_values = expon.pdf(x_values, scale=1 / x)
cdf_values = expon.cdf(x_values, scale=1 / x)

# Plot the PDF
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x_values, pdf_values, label='PDF')
plt.title('Exponential Distribution PDF')
plt.xlabel('Time (years)')
plt.ylabel('Probability Density')
plt.legend()

# Plot the CDF
plt.subplot(1, 2, 2)
plt.plot(x_values, cdf_values, label='CDF', color='orange')
plt.title('Exponential Distribution CDF')
plt.xlabel('Time (years)')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.tight_layout()
plt.show()
