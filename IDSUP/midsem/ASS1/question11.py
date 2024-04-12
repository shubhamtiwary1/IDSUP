#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
# import matplotlib.pyplot as plt
# import numpy as np
# months = np.arange(1, 13)
# max_temperatures = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
# min_temperatures = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

# plt.figure(figsize=(10, 6))
# plt.plot(months, max_temperatures, marker='o', color='red', label='Max Temperature')
# plt.plot(months, min_temperatures, marker='o', color='blue', label='Min Temperature')

# plt.xlabel('Month')
# plt.ylabel('Temperature (°C)')
# plt.title('Temperature Extremes in a Region of India')
# plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# plt.legend()
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
max_temps = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min_temps = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

plt.figure(figsize=(12, 6))
plt.plot(months, max_temps, 'ro-', label='Max Temp (°C)')
plt.plot(months, min_temps, 'bo-', label='Min Temp (°C)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Extremes in a Region of India')
plt.legend()
plt.grid(True)
plt.show()

