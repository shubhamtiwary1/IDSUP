import math
import matplotlib.pyplot as plt

# Define the range for x-axis
x = [i / 10 for i in range(-50, 51)]  # Range from -5 to 5 with step 0.1

# Define the µ and σ values for each plot
parameters = [(0, 1), (0, 2), (0, 0.5), (-1, 1)]

# Plot each Normal PDF with different line styles
for idx, (mu, sigma) in enumerate(parameters):
    # Calculate the PDF values for the given µ and σ
    y = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(t - mu) ** 2 / (2 * sigma ** 2)) for t in x]
    label = f"µ={mu}, σ={sigma}"
    plt.plot(x, y, label=label, linestyle='-')
    # Plot the PDF
    # if idx == 0:
    #     plt.plot(x, y, label=f"µ={mu}, σ={sigma}", linestyle='-', color='black')
    # elif idx == 1:
    #     plt.plot(x, y, label=f"µ={mu}, σ={sigma}", linestyle='--', color='blue')
    # elif idx == 2:
    #     plt.plot(x, y, label=f"µ={mu}, σ={sigma}", linestyle=':', color='red')
    # elif idx == 3:
    #     plt.plot(x, y, label=f"µ={mu}, σ={sigma}", linestyle='-.', color='green')

# Add labels and title
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Normal Probability Density Functions')

# Add legend
plt.legend()

# Display the plot
plt.show()
