# Create a dictionary to store the network
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
network = {}

# Add users to the network
for user in users:
    network[user["id"]] = set()

# Add friendships to the network
for friendship in friendship_pairs:
    user1, user2 = friendship
    network[user1].add(user2)
    network[user2].add(user1)

# Find total number of connections and average connections
total_connections = sum(len(friends) for friends in network.values())
average_connections = total_connections / len(network)
print(network.items())
# Sort from "most friends" to "least friends"
sorted_users = sorted(network.items(), key=lambda x: len(x[1]), reverse=True)

# Find the friends of friends
friends_of_friends = {}
for user_id, friends in network.items():
    fof = set()
    for friend in friends:
        fof.update(network[friend])
    fof -= friends
    fof.discard(user_id)
    friends_of_friends[user_id] = fof

# Print results
print("Total number of connections:", total_connections)
print("Average connections:", average_connections)
print("Users sorted by most friends:")
print(sorted_users)
# for user_id, friends in sorted_users:
#     print(f"{users[user_id]['name']}: {len(friends)} friends")
print("Friends of friends:")
print(friends_of_friends)
# for user_id, fof in friends_of_friends.items():
#     print(f"{users[user_id]['name']} - Friends of friends: {[users[f]['name'] for f in fof]}")
