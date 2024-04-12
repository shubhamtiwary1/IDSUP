#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5),(60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]
a = []
b = []
c = []

for salary, tenure in salaries_and_tenures:
    if tenure < 2:
        a.append(salary)
    elif 2 <= tenure <= 5:
        b.append(salary)
    else :
        c.append(salary)

average_salary_a = sum(a) / len(a)
average_salary_b = sum(b) / len(b)
average_salary_c= sum(c) / len(c)

if average_salary_a > average_salary_b and average_salary_a > average_salary_c :
    print("Users with less than two years of experience tend to pay.")
elif average_salary_c > average_salary_b and average_salary_c > average_salary_a :
    print("Users with more than five years of experience tend to pay.")
else:
    print("Users with average amounts of experience don't tend to pay.")