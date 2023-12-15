from scipy.stats import binom
import matplotlib.pyplot as plt

n = 6
p = 0.6

r_values = list(range(n + 1))

mean, var = binom.stats(n, p)

dist = [binom.pmf(r, n, p) for r in r_values ]

print("r\tp(r)")
for i in range(n + 1):
 print(str(r_values[i]) + "\t" + str(dist[i]))

print("mean = "+str(mean))
print("variance = "+str(var))

r_values = list(range(n + 1))

dist = [binom.pmf(r, n, p) for r in r_values ]



mean = n * p
variance = n * p * (1 - p)

print(f"mean = {mean}")
print(f"variance = {variance}")



plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title("Probability Mass Function")

plt.xlabel('')
plt.ylabel('Probability')
plt.plot(r_values, dist, "bo", ms=8, label="dddddd")
plt.vlines(r_values, 0, dist, colors="b", lw=5, alpha=0.5)
    
plt.subplot(122)
plt.title("Histogram")
plt.bar(r_values, dist, align='center', alpha=0.7)
plt.xlabel('')
plt.ylabel('Probability')
plt.show()
#########################################################################

