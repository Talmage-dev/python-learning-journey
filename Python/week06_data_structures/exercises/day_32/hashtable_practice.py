"""Day 32: Intensive Practice - Hashtables (Grouping)"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

# Problem 1: (12min)
# Start: 16:13

def group_by_first_letter(words):
    ht = HashTable(len(words))
    result = {}
    for word in words:
        key = word[0]
        group = ht.get(key)
        if group is None:
            group = []
        group.append(word)
        ht.insert(key, group)
    for bucket in ht.table:
        for k, v in bucket:
            result[k] = v
    return result

print(group_by_first_letter(["apple", "banana", "apricot", "blueberry", "cherry"]))
# → {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

print(group_by_first_letter(["dog", "cat", "duck", "cow"]))
# → {'d': ['dog', 'duck'], 'c': ['cat', 'cow']}

print(group_by_first_letter(["hello"]))
# → {'h': ['hello']}

# Problem 2: (10min)
# Start: 16:25

def group_by_length(words):
    ht = HashTable(len(words))
    result = {}
    for word in words:
        key = len(word)
        group = ht.get(key)
        if group is None:
            group = []
        group.append(word)
        ht.insert(key, group)
    for bucket in ht.table:
        for k, v in bucket:
            result[k] = v
    return result

print(group_by_length(["a", "to", "at", "tea", "bat", "cat"]))
# → {1: ['a'], 2: ['to', 'at'], 3: ['tea', 'bat', 'cat']}

print(group_by_length(["hello", "world", "hi", "bye"]))
# → {5: ['hello', 'world'], 2: ['hi'], 3: ['bye']}

print(group_by_length(["same", "size"]))
# → {4: ['same', 'size']}

# Problem 3:(10min)
# Start: 16:30

def group_students_by_grade(students):
    ht = HashTable(len(students))
    # students is a list of tuples: [(name, grade), ...]
    result = {}
    for student in students:
        key = student[1]
        group = ht.get(key)
        if group is None:
            group = []
        group.append(student[0])
        ht.insert(key, group)
    for bucket in ht.table:
        for k, v in bucket:
            result[k] = v
    return result

students1 = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "C"), ("Eve", "B")]
print(group_students_by_grade(students1))
# → {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Eve'], 'C': ['David']}

students2 = [("John", "A"), ("Jane", "A")]
print(group_students_by_grade(students2))
# → {'A': ['John', 'Jane']}

students3 = [("Solo", "A")]
print(group_students_by_grade(students3))
# → {'A': ['Solo']}

# Problem 4: (12min)
# Start: 16:36
def group_numbers_by_range(numbers):
    ht = HashTable(len(numbers))
    result = {}
    
    for num in numbers:
        # Calculate range start
        range_start = (num // 10) * 10
        
        # Create range label
        key = f"{range_start}-{range_start + 9}"
        
        # Get existing group or create new
        group = ht.get(key)
        if group is None:
            group = []
        
        group.append(num)
        ht.insert(key, group)
    
    # Extract to dictionary
    for bucket in ht.table:
        for k, v in bucket:
            result[k] = v
    
    return result

print(group_numbers_by_range([5, 15, 23, 8, 42, 17, 3, 51]))
# → {'0-9': [5, 8, 3], '10-19': [15, 17], '20-29': [23], '40-49': [42], '50-59': [51]}

print(group_numbers_by_range([1, 2, 3]))
# → {'0-9': [1, 2, 3]}

print(group_numbers_by_range([10, 20, 30]))
# → {'10-19': [10], '20-29': [20], '30-39': [30]}