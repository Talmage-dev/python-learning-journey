""" Day 23: Intensive Practice """

# Part 1: Hash Tables
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Get index
        index = self._hash(key)

        # Check if key exists, update if so update key's values
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
            
        # Otherwise append new key value pair
        self.table[index].append((key, value))

    def get(self, key):
        # Get index
        index = self._hash(key)
        
        # look for key
        for k, v in self.table[index]:
            if k == key:    # When key found
                return v    # Return value
        
        return None         # Key not found

# Implementation:
# Case 1: find duplicates in an array    
def find_duplicates(array):
    # =====================
    # Setup
    # =====================
    
    # Create Hashtable
    ht = HashTable(len(array))

    # Count Occurrances
    for num in array:
        count = ht.get(num)         # get element
        if count is None:           # if it doesn't have a count
            count = 0               # count starts at 0
        ht.insert(num, count + 1)   # if it has a count, a 1 to the count

    # =====================
    # Find Duplicates
    # =====================

    # create a list to store duplicates
    duplicates = []

    # find and add duplicates to list
    for bucket in ht.table:             # look at each bucket in the hashtable
        for key, value in bucket:       # for every key, value in the bucket
            if value > 1:               # if the count(v) is > than 1
                duplicates.append(key)  # add the element(k) to the list

    return duplicates 

# # Test
# a1 = [1, 2, 3, 2, 4, 1, 5]
# result = find_duplicates(a1)
# print(f"Duplicates: {result}")

# Case 2: Find 2 numbers in array that sum to target, return their indices.
def two_sum(array, target):
    # =====================
    # Setup
    # =====================
    # create hash table:
    ht = HashTable(len(array))

    # =====================
    # Find pair
    # =====================
    for i, num in enumerate(array):     # for each element in the array
        complement = target - num       # find the num you need to add up to the target

        # Look to see if complment is in the array
        comp_index = ht.get(complement) # get compliment from the array
        if comp_index is not None:      # if it is found
            return [comp_index, i]      # return
        
        # Store/Add current number and its index to the hashtable
        ht.insert(num, i)

    return None # No pair found

# # Test
# a2 = [2, 7, 11, 15]
# target = 9
# result1 = two_sum(a2, target)
# print(f"Indices: {result1}")
# print(f"Values: {a2[result1[0]]} + {a2[result1[1]]} = {target}")

#Case 3: Group words that are anagrams of each other
def group_anagrams(words):
    # ======================
    # Setup
    # ======================
    # Create hashtable
    ht = HashTable(len(words))

    # ======================
    # Sort Words
    # ======================
    for word in words:
        # Sort letter to create key
        key = "".join(sorted(word))         #"eat" -> "aet"

        # Get existing group or create new one
        group = ht.get(key)
        if group is None:
            group = []
        
        # Add word to group
        group.append(word)
        ht.insert(key, group)
    
    # =======================
    # Collect all groups
    # =======================
    result = []
    for bucket in ht.table:
        for key, group in bucket:
            result.append(group)
    
    return result

# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(f"Result: {result}")