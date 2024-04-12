from matplotlib import pyplot as plt
import random

num = [random.randint(0, 101) for _ in range(101)]

plt.hist(num, bins = 10, color = 'green', edgecolor = "black")
plt.xlabel("values")
plt.ylabel("frequency")
plt.title("Q5")
#plt.show()


import math
def mean(l):
    return sum(l)/len(l)

def sd(l):
    ele=[(x-mean(l))**2 for x in l]
    return math.sqrt(sum(ele)/(len(l)-1))
    
def normal_pdf(l):
    ele=[math.exp(-(x-mean(l))**2/(2*sd(l)**2)) for x in l]
    norm=[x/(sd(l)*math.sqrt(2*math.pi)) for x in ele]
    return norm

from collections import Counter
x = [2,1,5,3,4,4,2,4,4,5,5,3,5,3]
y = Counter(x)
print(y)

def ziplist(l1, l2):
    zippedlsit = list(zip(l1, l2))
    print(zippedlsit)
def zip_and_unzip(list1, list2):
    # Zip the two lists together
    zipped_lists = list(zip(list1, list2))

    # Print the zipped list
    print("Zipped list:")
    for i, (item1, item2) in enumerate(zipped_lists):
        print(f"Index {i}: {item1}, {item2}")

    # Unzip the zipped list
    unzipped_list1, unzipped_list2 = zip(*zipped_lists)

    return list(unzipped_list1), list(unzipped_list2)

# Example lists
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3, 4, 5]

# Zip and unzip the lists
ziplist(list1, list2)
unzipped_list1, unzipped_list2 = zip_and_unzip(list1, list2)

# Print the unzipped lists
print("\nUnzipped lists:")
print("List 1:", list(unzipped_list1))
print("List 2:", list(unzipped_list2))



