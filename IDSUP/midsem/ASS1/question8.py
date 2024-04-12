#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import matplotlib.pyplot as plt
years = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]
applicants_per_year = [921261, 929198, 1043739, 1186454, 1194938, 1304495, 1356805, 1282000, 479651]
plt.figure(figsize=(10, 6))
plt.scatter(years, applicants_per_year, color='blue', marker='o')
plt.title('Number of Applicants per Year')
plt.xlabel('Year')
plt.ylabel('Number of Applicants')
plt.grid(True)
plt.show()
