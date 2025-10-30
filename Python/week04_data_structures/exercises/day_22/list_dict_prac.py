"""List / Dictionary Practice"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 1:
# Your code here - use enumerate!
for i, v in enumerate(fruits):
    print(f"{i}: {v}")
# Expected output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date
# 4: elderberry

# 2:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Your code here - nested loop!
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
# Expected output: 1 2 3 4 5 6 7 8 9

# 3:
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "country": "USA"
}

# Your code here - use .items()!
for key, value in person.items():
    print(f"{key}: {value}")
# Expected output:
# name: Alice
# age: 25
# city: NYC
# country: USA

# 4:
data = {
    "name": "Bob",
    "age": 30
}

# Your code here - use .get() with defaults!
name = data.get("name", "Unknown")     # Get "name", default "Unknown"
age = data.get("age", 0)  # Get "age", default 0
city = data.get("city", "Not Specified")  # Get "city" (doesn't exist!), default "Not specified"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# Expected output:
# Name: Bob
# Age: 30
# City: Not specified

# 5:
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "coding", "gaming"]
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "hobbies": ["music", "sports"]
    },
    "user3": {
        "name": "Charlie",
        "age": 22,
        "hobbies": ["art", "cooking", "travel"]
    }
}

# Task 1: Print all user IDs and names
for key, value in users.items():
    print(f"{key}: {value["name"]}")
# Expected:
# user1: Alice
# user2: Bob
# user3: Charlie

# Task 2: Print user2's age
print(users["user2"]["age"])

# Task 3: Print user1's second hobby (index 1)
print(users["user1"]["hobbies"][1])

# Task 4: Loop through all users and print their name and number of hobbies
for user_id, user_info in users.items():
    print(f"{user_info["name"]} has {len(user_info["hobbies"])} hobbie/s")
# Expected:
# Alice has 3 hobbies
# Bob has 2 hobbies
# Charlie has 3 hobbies