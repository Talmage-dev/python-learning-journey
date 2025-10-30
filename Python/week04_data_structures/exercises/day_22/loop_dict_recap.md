
Let's dive into Lists and Dictionaries! 🚀

---

# Lists & Dictionaries - Complete Guide

---

## **PART 1: LISTS**

### **Basic List:**
```python
fruits = ["apple", "banana", "cherry", "date"]
```

---

### **1. Looping Through Lists**

#### **Method 1: Simple for loop**
```python
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry, date
```

#### **Method 2: With index (enumerate)**
```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date
```

#### **Method 3: While loop**
```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

### **2. Accessing Elements**

```python
fruits = ["apple", "banana", "cherry", "date"]

# By index
first = fruits[0]        # "apple"
last = fruits[-1]        # "date"
second_last = fruits[-2] # "cherry"

# Slicing
first_two = fruits[0:2]  # ["apple", "banana"]
last_two = fruits[-2:]   # ["cherry", "date"]
middle = fruits[1:3]     # ["banana", "cherry"]
```

---

### **3. Nested Lists**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access outer list
row = matrix[0]          # [1, 2, 3]

# Access inner element
element = matrix[0][1]   # 2 (row 0, column 1)

# Loop through nested list
for row in matrix:
    for num in row:
        print(num, end=" ")
# Output: 1 2 3 4 5 6 7 8 9
```

---

### **4. Common List Methods**

```python
fruits = ["apple", "banana"]

# Add
fruits.append("cherry")        # ["apple", "banana", "cherry"]
fruits.extend(["date", "fig"]) # ["apple", "banana", "cherry", "date", "fig"]
fruits.insert(1, "blueberry")  # Insert at index 1

# Remove
fruits.pop()           # Remove last, returns "fig"
fruits.pop(0)          # Remove at index 0, returns "apple"
fruits.remove("date")  # Remove by value

# Other
length = len(fruits)   # Get length
fruits.sort()          # Sort in place
fruits.reverse()       # Reverse in place
```

---

### **5. List Comprehensions**

```python
# Create new list from existing
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
# [2, 4, 6, 8, 10]

# With condition
evens = [n for n in numbers if n % 2 == 0]
# [2, 4]

# From nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

---

## **PART 2: DICTIONARIES**

### **Basic Dictionary:**
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}
```

---

### **1. Looping Through Dictionaries**

#### **Method 1: Loop through keys (default)**
```python
for key in person:
    print(key)
# Output: name, age, city
```

#### **Method 2: Loop through keys explicitly**
```python
for key in person.keys():
    print(key)
# Output: name, age, city
```

#### **Method 3: Loop through values**
```python
for value in person.values():
    print(value)
# Output: Alice, 25, NYC
```

#### **Method 4: Loop through key-value pairs (MOST COMMON)**
```python
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: NYC
```

---

### **2. Accessing Dictionary Values**

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Direct access (can crash if key doesn't exist!)
name = person["name"]        # "Alice"
# age = person["country"]    # ❌ KeyError!

# Safe access with .get() (RECOMMENDED)
name = person.get("name")           # "Alice"
country = person.get("country")     # None (no crash!)
country = person.get("country", "Unknown")  # "Unknown" (default value)
```

---

### **3. Nested Dictionaries (THE TRICKY ONE!)**

```python
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "coding"]
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "hobbies": ["gaming", "music"]
    }
}
```

#### **Accessing nested values:**
```python
# Get user1's name
name = users["user1"]["name"]  # "Alice"

# Get user2's first hobby
hobby = users["user2"]["hobbies"][0]  # "gaming"

# Safe access
name = users.get("user1", {}).get("name")  # "Alice"
name = users.get("user3", {}).get("name")  # None (no crash!)
```

#### **Looping through nested dictionary:**
```python
# Loop through all users
for user_id, user_data in users.items():
    print(f"User ID: {user_id}")
    print(f"  Name: {user_data['name']}")
    print(f"  Age: {user_data['age']}")
    print(f"  Hobbies: {', '.join(user_data['hobbies'])}")

# Output:
# User ID: user1
#   Name: Alice
#   Age: 25
#   Hobbies: reading, coding
# User ID: user2
#   Name: Bob
#   Age: 30
#   Hobbies: gaming, music
```

---

### **4. Common Dictionary Methods**

```python
person = {"name": "Alice", "age": 25}

# Add/Update
person["city"] = "NYC"           # Add new key
person["age"] = 26               # Update existing
person.update({"country": "USA", "age": 27})  # Update multiple

# Remove
age = person.pop("age")          # Remove and return value
person.pop("missing", None)      # Safe remove (no crash)
del person["city"]               # Delete key

# Check
if "name" in person:             # Check if key exists
    print(person["name"])

# Get all
keys = person.keys()             # dict_keys(['name'])
values = person.values()         # dict_values(['Alice'])
items = person.items()           # dict_items([('name', 'Alice')])
```

---

### **5. Dictionary Comprehensions**

```python
# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# Transform dictionary
prices = {"apple": 1.0, "banana": 0.5}
doubled = {k: v * 2 for k, v in prices.items()}
# {'apple': 2.0, 'banana': 1.0}

# Filter dictionary
expensive = {k: v for k, v in prices.items() if v > 0.7}
# {'apple': 1.0}
```

---

## **COMMON PATTERNS YOU'VE USED:**

### **Pattern 1: Graph (Dictionary of Lists)**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D']
}

# Loop through
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

# Access
neighbors_of_a = graph['A']  # ['B', 'C']
```

### **Pattern 2: Hash Table (Dictionary of Values)**
```python
word_counts = {
    'the': 5,
    'cat': 2,
    'dog': 3
}

# Loop through
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Update count
word = "cat"
word_counts[word] = word_counts.get(word, 0) + 1
```

### **Pattern 3: Nested Dictionary (Dictionary of Dictionaries)**
```python
students = {
    'Alice': {'age': 20, 'grade': 'A'},
    'Bob': {'age': 21, 'grade': 'B'}
}

# Loop through
for name, info in students.items():
    print(f"{name}: Age {info['age']}, Grade {info['grade']}")

# Safe access
age = students.get('Alice', {}).get('age', 0)
```

---

## **QUICK REFERENCE CHEAT SHEET:**

```python
# LISTS
for item in list:                    # Loop through items
for i, item in enumerate(list):      # Loop with index
item = list[0]                       # Access by index
sublist = list[1:3]                  # Slice
list.append(item)                    # Add to end
list.pop()                           # Remove from end

# DICTIONARIES
for key in dict:                     # Loop through keys
for value in dict.values():          # Loop through values
for key, value in dict.items():      # Loop through pairs (MOST COMMON!)
value = dict.get(key, default)       # Safe access
dict[key] = value                    # Add/update
if key in dict:                      # Check if exists

# NESTED DICTIONARIES
for outer_key, inner_dict in nested.items():
    for inner_key, value in inner_dict.items():
        print(f"{outer_key}.{inner_key} = {value}")
```
