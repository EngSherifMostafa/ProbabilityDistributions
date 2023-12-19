from scipy.stats import expon
import numpy as np
from plot import plot_pdf, plot_cdf


n_ofEarthQuakes = 113    #Earthquakes happend from 1800 to 2023
n_ofyears = 223   
mean = n_ofEarthQuakes / n_ofyears  # lambda = 1/mean


time_period = 50  # 50 years
x = 1 / (mean)  # Rate lambda for 1 event per mean years
probability_next_50_years = expon.pdf(time_period, scale=1 / x)

print("Probability of earthquake in the next 50 years:", probability_next_50_years)

# Plot the PDF and CDF for visualization
x_values = np.linspace(0, 5, 100)
pdf_values = expon.pdf(x_values, scale=1 / x)
cdf_values = expon.cdf(x_values, scale=1 / x)
plot_pdf("Exponential", "PDF", x_values, pdf_values)
plot_cdf("Exponential", "CDF", x_values, cdf_values)
