import math
import random
import matplotlib.pyplot as plt

# Parameters
n = 100
p = 0.75
num_points = 100

# Calculate binomial probabilities
def binomial_probability(n, k, p):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * (p**k) * ((1-p)**(n-k))

#probabilities = [binomial_probability(n, k, p) for k in range(n+1)]

# Generate binomial samples
binomial_samples = [sum(random.random() < p for _ in range(n)) for _ in range(num_points)]

# Calculate mean and standard deviation
mean = n * p
std_dev = math.sqrt(n * p * (1 - p))

# Calculate normal approximation
def normal_approximation(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean)**2) / (2 * std_dev**2))

normal_values = [normal_approximation(x, mean, std_dev) for x in range(n+1)]

# Plot histogram of binomial samples
plt.hist(binomial_samples, bins=10, density=True,label='Binomial Samples')

# Plot line chart for normal approximation
plt.plot(range(n+1), normal_values, color='red', linestyle='dashed', label='Normal Approximation')

plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution vs. Normal Approximation')
plt.legend()
plt.show()
