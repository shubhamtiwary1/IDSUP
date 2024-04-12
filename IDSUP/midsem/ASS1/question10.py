#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import matplotlib.pyplot as plt
male_age = [53, 51, 71, 31, 33, 39, 52, 27, 54, 30, 64, 26, 21, 54, 52, 20, 59, 32]
female_age = [53, 65, 68, 21, 75, 46, 24, 63, 61, 24, 49, 41, 39, 40, 25, 54, 42, 32, 48, 23, 23]
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.hist(male_age, bins=10, color='blue', edgecolor='black')
plt.title('Male Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(female_age, bins=10, color='red', edgecolor='black')
plt.title('Female Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
