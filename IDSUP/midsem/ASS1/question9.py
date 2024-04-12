import matplotlib.pyplot as plt
import math

# Define the range of x values
x = [i for i in range(-10, 11)]

# Calculate the y values for each function
y1 = [xi * math.sin(xi) for xi in x]
y2 = [xi**2 * math.sin(xi) for xi in x]
y3 = [xi**3 * math.sin(xi) for xi in x]
y4 = [xi**4 * math.sin(xi) for xi in x]

# Plot the functions
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='xsin(x)')
plt.plot(x, y2, label='x^2sin(x)')
plt.plot(x, y3, label='x^3sin(x)')
plt.plot(x, y4, label='x^4sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of x*sin(x), x^2*sin(x), x^3*sin(x), and x^4*sin(x)')
plt.legend()
plt.grid(True)
plt.show()
