from collections import defaultdict

interests=[(0,'Hadoop'),(1,'c'),(1,'c++'), (2,'java'),(2,'Data Science'),(2,'Big Data'), (3,'python'),(3,'data mining'),(4,'web mining'),(4,'data structure'),(5,'deep learning'),(5,'machine learning')] 
interest_count = defaultdict(int)
for user_id, interest in interests:
    interest_count[interest] += 1
print(interest_count)

most_popular_interests = sorted(interest_count.items(), key=lambda x: x[1], reverse=True)

print("Most popular interests:")
for interest, count in most_popular_interests:
    print(f"{interest}: {count} users interested")

