import numpy as np
import scipy.stats as stats


import matplotlib.pyplot as plt


def plot_pmf(dis_type, title, x_axis, y_axis):
    plt.title(dis_type+"\n"+title)
    plt.xlabel('state')
    plt.ylabel('Probability')
    plt.bar(x_axis, y_axis)
    plt.show()


def plot_cdf(dis_type, title, x_axis, y_axis):
    plt.title(dis_type+"\n"+title)
    plt.xlabel('state')
    plt.ylabel('Probability')
    plt.step(x_axis, y_axis)
    plt.show()

p = 0.3
rv = stats.bernoulli(p)
x = np.linspace(0, 1, 2)
f = rv.pmf(x)
F = rv.cdf(x)

mean, var = rv.stats(moments="mv")
print(f"mean: {mean}\nVariance: {var}")


plt.title("")


plt.plot(x, f, "bo", ms=8, label="dddddd")
plt.vlines(x, 0, f, colors="b", lw=5, alpha=0.5)

plt.show()


