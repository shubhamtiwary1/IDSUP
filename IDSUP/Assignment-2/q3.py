#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:10:14 2024

@author: student
"""

def extractRow(mat, n):
    return mat[n];

def extractColumn(mat, n):
    
    temp = []
    for j in range(0, 3):
        temp.append(mat[j][n])
    return temp
    

print(extractRow([[1,2,3],[4,5,6],[7,8,9]], 1))
print(extractColumn([[1,2,3],[4,5,6],[7,8,9]], 1))



Matrix = List[List[float]]
def mats(mat : Matrix) -> Matrix:
    return mat[0]
    
mat = []
r = 3
for i in range(r):
    #row = []
    #for j in range(3):
    mat.append(input("Enter : "))

print(mats(mat))