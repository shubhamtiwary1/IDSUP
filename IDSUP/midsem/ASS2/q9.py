import math
import matplotlib.pyplot as plt

# Values of µ and σ
parameters = [(0, 1), (0, 2), (0, 0.5), (-1, 1)]

# Range for x-axis
x = [-5 + i*0.1 for i in range(101)]

# Plotting the Normal CDFs
for i, (mu, sigma) in enumerate(parameters):
    cdf_values = [0.5*(1 + math.erf((val - mu) / (sigma * math.sqrt(2)))) for val in x]
    #linestyle = ['-', '--', '-.', ':'][i % 4]  # Cycle through different line styles
    label = f"µ={mu}, σ={sigma}"
    plt.plot(x, cdf_values, linestyle="-", label=label)

# Adding labels and title
plt.xlabel('x')
plt.ylabel('CDF')
plt.title('Normal CDFs for Different Values of µ and σ')

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
