
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import poisson


def print_pause(message):
    print(message)
    time.sleep(2)


def poisson_drv():
    # Set the parameter
    rate_poisson = 2  # Average rate (lambda) for the Poisson distribution
    print("A service center receives an average of 2 customers per hour.")
    print_pause("What is the probability of receiving at most 3 customers in the next hour?")
    print_pause("We can use the Poisson random variable for this scenario.")
    print_pause(f"The average rate (lambda) is {rate_poisson} customers per hour.")

    # Generate Poisson random variable
    poisson_rvs = poisson.rvs(mu=rate_poisson, size=1000)

    # Calculate PMF and CDF
    k_values = np.arange(0, 10)  # Adjust the range based on your scenario
    pmf_values = poisson.pmf(k_values, mu=rate_poisson)
    cdf_values = poisson.cdf(k_values, mu=rate_poisson)

    # Calculate mean and variance
    mean_poisson = poisson.mean(mu=rate_poisson)
    variance_poisson = poisson.var(mu=rate_poisson)

    # Display mean and variance
    print_pause(f"The MEAN value = {mean_poisson}")
    print_pause(f"The VARIANCE value = {variance_poisson}")

    cdf = poisson.cdf(3, mu=rate_poisson)
    print_pause("To calculate the probability of receiving at most 3 customers in the next hour,")
    print_pause(f"We must calculate the CDF of 3, which is approximately {cdf:.4f}")
    time.sleep(4)

    print_pause("Now let's visualize the PMF and CDF:")
    time.sleep(3)
    show_x = int(input("Show? (1 for Yes, 0 for No): "))
    if show_x == 1:
        plt.figure(figsize=(12, 6))

        plt.subplot(121)
        plt.plot(k_values, pmf_values, "bo", ms=8, label="Poisson PMF")
        plt.vlines(k_values, 0, pmf_values, colors="b", lw=5, alpha=0.5)
        plt.title('Poisson Distribution PMF')
        plt.xlabel('k')
        plt.ylabel('Probability')

        plt.subplot(122)
        plt.step(k_values, cdf_values, where='post')
        plt.title('Poisson Distribution CDF')
        plt.xlabel('k')
        plt.ylabel('Probability')
        plt.tight_layout()
        plt.show()


print("Choose the number of Example that you want : ")
print("1- Binomial random variable ")
print("2- Poisson random variable ")


poisson_drv()

