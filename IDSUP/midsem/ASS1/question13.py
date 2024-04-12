#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import matplotlib.pyplot as plt
mentions = [500, 505]
years = [2017, 2018]

# plt.figure(figsize=(8, 6))
# plt.bar(years, mentions, color='skyblue')
# plt.xlabel('Year')
# plt.ylabel('Mentions')
# plt.title('Bar Chart without Starting Y-axis from 0')
# plt.show()

# plt.figure(figsize=(8, 6))
plt.bar(years, mentions, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Mentions')
plt.title('Bar Chart with Y-axis Starting from 0')
plt.ylim(0) 
plt.show()
