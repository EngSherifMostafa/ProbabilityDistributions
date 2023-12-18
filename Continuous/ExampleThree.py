from scipy.stats import expon
import numpy as np
from plot import plot_pdf, plot_cdf


n_ofEarthQuack = 20
n_ofyears = 22
mean = n_ofyears / n_ofEarthQuack  # lambda = 1/mean

# What is the probability of the next earthquake in the next 6 months?
time_period = 6  # 6 months
x = 1 / (mean * 12)  # Rate lambda for 1 event per mean years
probability_next_6_months = expon.pdf(time_period, scale=1 / x)

print("Probability of earthquake in the next 6 months:", probability_next_6_months)

# Plot the PDF and CDF for visualization
x_values = np.linspace(0, 5, 100)
pdf_values = expon.pdf(x_values, scale=1 / x)
cdf_values = expon.cdf(x_values, scale=1 / x)
plot_pdf("Exponential", "PDF", x_values, pdf_values)
plot_cdf("Exponential", "CDF", x_values, cdf_values)




