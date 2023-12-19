from scipy.stats import expon
import numpy as np
from plot import plot_pdf, plot_cdf
n_ofEarthQuakes = 113    # Earthquakes happened from 1800 to 2023
n_ofyears = 223
mean = n_ofEarthQuakes / n_ofyears  # lambda = 1/mean

time_period = 1  # 1 year
x = 1 / mean  # Rate lambda for 1 event per mean years
probability_next_year = expon.pdf(time_period, scale=1 / x)

print("Probability of earthquake in the next year:", probability_next_year)

# Plot the PDF and CDF
x_values = np.linspace(0, 5, 100)
pdf_values = expon.pdf(x_values, scale=1 / x)
cdf_values = expon.cdf(x_values, scale=1 / x)
plot_pdf("Exponential", "PDF", x_values, pdf_values)
plot_cdf("Exponential", "CDF", x_values, cdf_values)
