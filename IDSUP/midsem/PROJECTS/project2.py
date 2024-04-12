from collections import defaultdict
users=[
    {'id':0,'name':'Ashok'},
    {'id':1, 'name':'Rahul'},
    {'id':2, 'name':'Sarita'},
    {'id':3, 'name':'Rohan'},
    {'id':4, 'name':'Akhaya'},
    {'id':5, 'name':'Prakash'},
    {'id':6, 'name':'Madhabi'},
    {'id':7, 'name':'Spandan'}
   
    ]
interests=[(0,'python'),(0,'java'),(1,'java'),(2,'python'),(2,'java'),(3,'python'),(4,'c'),(5,'c'),
           (6,'python'),(7,'java')]

user_ids_by_interest = defaultdict(list) 
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
print(dict(user_ids_by_interest))

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
print(dict(interests_by_user_id))

user_id = 0
user_interests = set(interests_by_user_id[user_id])
most_common_user = 0
most_common_interests = 0
for other_user_id, interests in interests_by_user_id.items():
    if other_user_id != user_id:
        common_interests = len(user_interests.intersection(set(interests)))
        print(user_interests.intersection(set(interests)))
        if common_interests > most_common_interests:
            most_common_user = other_user_id
            most_common_interests = common_interests
print(f"User {most_common_user} has the most interests in common with user {user_id}")
