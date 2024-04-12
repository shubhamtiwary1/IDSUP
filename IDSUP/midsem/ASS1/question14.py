#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
import matplotlib.pyplot as plt
test1_grades = [99, 90, 85, 97, 80]
test2_grades = [100, 85, 60, 90, 70]
plt.figure(figsize=(10, 6))
plt.scatter(test1_grades, test2_grades, color='black')
plt.xlabel('Test 1 Grades')
plt.ylabel('Test 2 Grades')
plt.title('Scatter Plot with Unequal Axis')



plt.figure(figsize=(10, 6))
plt.scatter(test1_grades, test2_grades, color='blue')
plt.xlabel('Test 1 Grades')
plt.ylabel('Test 2 Grades')
plt.title('Scatter Plot with Equal Axis')
plt.grid(True)
plt.axis('equal') 
plt.show()
