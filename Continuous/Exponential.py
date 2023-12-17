from scipy.stats import expon
import numpy as np
from plot import plot_pdf, plot_cdf



scale = 2.0
size = 1000
random_numbers = expon.rvs(scale=scale, size=size)


mean = expon.mean(scale=scale)
variance = expon.var(scale=scale)
standard_deviation = expon.std(scale=scale)
median = expon.median(scale=scale)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
print("Median:", median)


x = 3.0
cdf = expon.cdf(x, scale=scale)
print("CDF at", x, ":", cdf)


p = 0.75
quantile = expon.ppf(p, scale=scale)
print("Quantile at", p, ":", quantile)

# Plot the PDF and CDF
x = np.linspace(0, 10, 1000)  # Values of x for plotting
f = expon.pdf(x, scale=scale)  # PDF values
F = expon.cdf(x, scale=scale)  # CDF values

plot_pdf("Exponential", "PDF", x, f)
plot_cdf("Exponential", "CDF", x, F)

