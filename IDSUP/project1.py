#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:30:41 2024

@author: student

Data Science Project 1 ------------------------------------------->>>>>>>>

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
   
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

1.	Creation of DataSciencester Network
2.	Find the total number of connections and average connections of the network
3.	Sort from “most friends” to “least friends”
4.	Find the friends of friends


"""
from collections import OrderedDict
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" }, 
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
   
]

friendship_pair = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

friendships = {user["id"]:[] for user in users}

for i,j in friendship_pair:
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)

sums=0
for i in friendships:
    sums += len(friendships[i])

average = sums/len(friendships)

print("Total no of connections : ", sums)
print("Average connections : ",average)

def sorteddict(friendships):
    tempfriends = friendships
    tempfriends = dict(sorted(tempfriends.items(), key=lambda item: len(item[1]), reverse = True))
    print("Sorted Dictionary is : \n",tempfriends)
sorteddict(friendships)

