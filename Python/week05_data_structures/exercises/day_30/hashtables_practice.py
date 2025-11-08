"""Day 30: Intensive Practice - HashTables (Seen)"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

# Counting - quick recap (10min)
def character_frequency(s):
    ht = HashTable(len(s))
    result = {}
    for char in s:
        count = ht.get(char)
        if count is None:
            count = 0
        ht.insert(char, count + 1)
    for bucket in ht.table:
        for k, v in bucket:
            result[k] = v
    return result

print(character_frequency("hello"))
# → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(character_frequency("mississippi"))
# → {'m': 1, 'i': 4, 's': 4, 'p': 2}

print(character_frequency("aaa"))
# → {'a': 3}

# Problem 1: (12min)
def contains_duplicate(arr):
    ht = HashTable(len(arr))
    for num in arr:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    for bucket in ht.table:
        for k, v in bucket:
            if v > 1:
                return True
    return False

# Better approach:
# def contains_duplicate(arr):
#     ht = HashTable(len(arr))
    
#     for num in arr:
#         if ht.get(num) is not None:
#             return True
        
#         ht.insert(num, True) 
    
#     return False 

print(contains_duplicate([1, 2, 3, 1]))      # → True
print(contains_duplicate([1, 2, 3, 4]))      # → False
print(contains_duplicate([1, 1, 1, 1]))      # → True

# Problem 2: (10 min)
def find_unique_elements(arr):
    ht = HashTable(len(arr))
    result = []

    for num in arr:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    for bucket in ht.table:
        for k, v in bucket:
            if v == 1:
                result.append(k)
    return result

print(find_unique_elements([1, 2, 2, 3, 4, 4, 5]))
# → [1, 3, 5] (appear only once)

print(find_unique_elements([1, 1, 2, 2, 3, 3]))
# → [] (all appear twice)

print(find_unique_elements([5, 5, 5, 6, 7]))
# → [6, 7] (appear only once)

# Problem 3: (12min)
def has_pair_with_sum(arr, target):
    ht = HashTable(len(arr))
    for num in arr:
        comp = target - num
        if ht.get(comp) is not None:
            return True
        ht.insert(num, True)
    return False

print(has_pair_with_sum([1, 2, 3, 9], 8))
# → False (no two numbers add to 8)

print(has_pair_with_sum([1, 2, 4, 4], 8))
# → True (4 + 4 = 8)

print(has_pair_with_sum([1, 4, 3, 9], 8))
# → False (no pair adds to 8)

print(has_pair_with_sum([3, 5, 2, -4, 8, 11], 7))
# → True (3 + 4 = 7, or -4 + 11 = 7)

# Problem 4: (15min)
def find_intersection(arr1, arr2):
    ht = HashTable(len(arr1))
    ht2 = HashTable(len(arr2))
    result = []
    for num in arr1:
        ht.insert(num, True)
    for num in arr2:
        if ht.get(num) is True:
            ht2.insert(num, True)
    for bucket in ht2.table:
        for k, v in bucket:
            result.append(k)
    return result

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# → [3, 4] (appear in both)

print(find_intersection([1, 2, 2, 3], [2, 2, 3, 4]))
# → [2, 3] (no duplicates in result)

print(find_intersection([1, 2, 3], [4, 5, 6]))
# → [] (no common elements)

print(find_intersection([1, 1, 1], [1, 1]))
# → [1] (1 appears in both, return once)