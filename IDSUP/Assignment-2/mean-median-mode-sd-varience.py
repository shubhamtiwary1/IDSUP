#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:25:41 2024

@author: student

MEAN :-
some basic properties of mean:-
1) It may not be an element of the collection.
2)Even if all element of the collection are integers the mean may not be an integer.
3)It lies somewhere between the smallest and the larges date. It may not lies exactly in the middle.
4) If all the data in the collection have the same units then the mean also has the same unit.
5) The mean is affected by the value at the extrem ends.
Find mean of :- 20 200 20 140 40 20 50 200 200


def mean(l):
    return sum(l)/len(l)
l1 = [20,200,20,140,40,20,50,200,200]
print(mean(l1))
"""

"""
Median is the middle most value of the sorted data it denotes a positional average.
some properties :
    1) it is the middle data if the number of data is odd.
    2) it is the average of two middle most values if the no. of data is even.
    3) the median is not affected by the values at the extrem ends.

def median(l):
    l.sort()
    n=len(l)
    if(n%2 == 0):
        return (l[n//2]+l[n//2-1])/2
    return l[n//2]
l1 = [20,200,20,140,40,20,50,200,200]
l2 = [50,140,200,200,200,20,20,20,40,40]
print(median(l1))
print(median(l2))
"""

"""
MODE
Mode is the most common element in the data set.
EX : [20,200,20,140,40,20,50,200,200]

from collections import Counter
def mode(l):
    c=Counter(l)
    mode_l=[]
    for i,j in c.items():
        if j==max(c.values()):
            mode_l.append(i)
    return mode_l
l1 = [20,200,20,140,40,20,50,200,200]
print(mode(l1))

"""


"""
DISPERSION:
The literal meaning of dispersion is scatterdness i.e. how far the data spread
Range is directly proportional to the sprread of data, thus the bigger the range the more spread out data an vice-versa.

"""

"""
VARIENCE : 
varience is a complex measure of dispersion. A higher varience indicate that the data more spread out from the mean while a lower variece indicate that the data points are closer to the mean\
Varience provides a measure of dispersion in square unites of the data.
Fomula for varience of sample data is given by : s^2 = 1/n-1 summation i=1 to n (xi - xbar)^2.


def varience(l1):
    lsum=0
    for i in l1:
        lsum += pow((i-mean(l1)), 2)
    return 1/(len(l1)-1) * lsum
def mean(l):
    return sum(l)/len(l)
l1=[20,200,20,140,40,20,50,200,200]
print(varience(l1))

"""
"""
STANDARD DEVIATION :-
it is another measure of the spread of data points from the mean.
it is the  square roor of varience.
A higher standard deviation means that there is a lot of varience in the observed data around the mean.
It denotes variability
A lowered standard devation means that much of the data observed is clustered tightly around the mean. it denotes consistency.
It provides a measure of dispersion in the origina units of the data.

def sd(l1):
    return math.sqrt(varience(l1))
l1=[20,200,20,140,40,20,50,200,200]

"""

"""
Practical question: 
The sales data of two employess A and B for the firest 6 months are given as follows:
    MONTHS          EMPLOYEE A          EMPLOYEE B
    jaN             3000                5000
    feb             3500                2500
    mar             4000                5000
    apr             3500                2000
    may             4000                5500
    jun             4500                2500
    
the above value show that although the average sales of A and B are the same the sale of B vary more month to month compared to 
A these kind of analysis helps supervisers make informed decision about resourse allocation, performance evalution, and strategic planning 

"""
jkjskkoigi