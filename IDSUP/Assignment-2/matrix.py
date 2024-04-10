#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:27:34 2024

@author: student
"""
from typing import List
array = []
for i in range(3):
    array.append(list(map(int, input("Enter the list elements : ").strip().split())))

print(array)

