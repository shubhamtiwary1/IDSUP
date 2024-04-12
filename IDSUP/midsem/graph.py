# from matplotlib import pyplot as plt

# #Data to plot:
# years=[1950,1960,1970,1980,1990,2000,2010]
# gdp=[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

# #Plotting the figure:
# plt.plot(years,gdp,color='red',marker='s',linestyle='dashdot')
# #color->changes graph color; marker->points to specific data points;
# #linestyle='dashdot' -> gives a line comprising dashes and dots.
# #'dashdot' can be replaced with the following:
# #'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dotted'

# #Title of the graph on top of the graph:
# plt.title("Nominal GDP") 

# #x-axis label:
# plt.xlabel("Years\n(a)") 

# #y-axis label:
# plt.ylabel("Billions of dollars") 

# #Display the figure:
# plt.show() 


# from collections import Counter
# from matplotlib import pyplot as plt

# # Exam grades
# grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# # Bucket grades by decile, but put 100 in with the 90s
# histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
# print(histogram)

# # Plotting the histogram
# plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
#         histogram.values(),                 # Heights of bars
#         10,                                 # Width of each bar
#         edgecolor=(0, 0, 0)                 # Black edges for bars
#         )

# # Setting plot properties
# plt.axis([-5, 105, 0, 5])       # x-axis from -5 to 105, y-axis from 0 to 5
# plt.xticks([10 * i for i in range(11)])  # x-axis labels at 0, 10,...,100
# plt.xlabel("Decile")            # x-axis label
# plt.ylabel("# of Students")     # y-axis label
# plt.title("Distribution of Exam 1 Grades")  # Plot title

# # Displaying the plot
# plt.show()


# import matplotlib.pyplot as plt

# # Data to plot
# x_values = [1, 2, 3, 4, 5]
# y_values = [10, 15, 7, 20, 12]
# marker_labels = ['a', 'b', 'c', 'd', 'e']

# # Plotting the scatter plot
# plt.figure(figsize=(8, 6))  # Optional: Set figure size (width, height)
# plt.scatter(x_values, y_values, color=['red', 'green', 'blue', 'orange', 'black'],
#             marker='o', s=100, edgecolors='black', alpha=0.5, label='Scatter Plot')

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot Example')

# # Annotate points with marker labels
# for i, (x, y, label) in enumerate(zip(x_values, y_values, marker_labels)):
#     plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

# # Add legend (optional)
# plt.legend()

# # Display the plot
# plt.grid(True)  # Optional: Add gridlines
# plt.tight_layout()  # Optional: Adjust spacing between elements
# plt.show()


# Histogram
# import matplotlib.pyplot as plt

# # Given data
# data = [83, 95, 91, 87, 0, 85, 82, 100, 67, 73, 77, 0]

# # Create a histogram with enhanced customization
# plt.hist(data, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

# # Add labels and title with bold fontweight
# plt.xlabel('Values', fontweight='bold')
# plt.ylabel('Density', fontweight='bold')
# plt.title('Enhanced Histogram Example', fontweight='bold')
# plt.xticks([10*i for i in range(11)])
    
# # Add gridlines
# plt.grid(True, linestyle='--', alpha=0.5)
# # Show the plot
# plt.show()


import matplotlib.pyplot as plt

# Data to plot
movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

# Plotting the figure
plt.figure(figsize=(10, 6))  # Optional: Set figure size (width, height) in inches

bars = plt.bar(movies, num_oscars, color=['red', 'green', 'blue', 'orange', 'black'],
             edgecolor='black', linewidth=1.2, alpha=0.8)  # Adjust bar transparency

# Title and labels
plt.title("Classic Movies: Number of Oscars Won", fontsize=16)  # More descriptive title
plt.xlabel("Movie Name", labelpad=10)  # Add padding between label and axis
plt.ylabel("Number of Oscars", fontsize=14)

# Y-axis limits with some extra space at the top
plt.ylim(0, max(num_oscars) + 1.5)

# Display data values above bars
for i, value in enumerate(num_oscars):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=12)

# Add gridlines on both axes
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Display legend (optional)
# plt.legend()  # Uncomment if you want a legend for the bars

# Display the plot
plt.tight_layout()  # Adjust spacing for better layout
plt.show()
