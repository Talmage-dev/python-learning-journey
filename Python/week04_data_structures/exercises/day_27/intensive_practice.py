"""Day 27: Intensive Practice - Hash Tables"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

# Case 1:
# Time Start: 10:40
# Time Finished: 10:53

def group_anagrams(words):
    # Create hashtable
    ht = HashTable(len(words))
    
    # Get individual words
    for word in words:
        key = "".join(sorted(word))     # Join them
        group = ht.get(key)             # Check if they are already seen
        if group is None:               # If they haven't
            group = []                  # empty array
        group.append(word)              # otherwise add them to the existing group
        ht.insert(key, group)           # add key and group to hashtable
    
    # Get the groups
    result = []
    for bucket in ht.table:
        for key, group in bucket:
            result.append(group)
    
    return result

# Test 1
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Test 2
words = ["abc", "bca", "cab", "xyz", "zyx"]
print(group_anagrams(words))
# Expected: [["abc", "bca", "cab"], ["xyz", "zyx"]]

# Test 3
words = ["hello", "world"]
print(group_anagrams(words))
# Expected: [["hello"], ["world"]]

# Case 2:
# Time Started: 11:00am
# Time Ended: 11:15
# Note: didn't get close to finishing, didn't even figure out the logic

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    # Pass 1: Add all numbers to hash table
    ht = HashTable(len(nums))
    for num in nums:
        ht.insert(num, True)  # Pattern: SEEN (just checking existence)
    
    longest = 0
    
    # Pass 2: Find sequences
    for num in nums:
        # Check if this is the START of a sequence
        if ht.get(num - 1) is None:  # num-1 doesn't exist, so num is a start!
            current_num = num
            current_length = 1
            
            # Count forward from this start
            while ht.get(current_num + 1) is not None:
                current_num += 1
                current_length += 1
            
            # Update longest if this sequence is longer
            longest = max(longest, current_length)
    
    return longest

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # → 4
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # → 9
print(longest_consecutive_sequence([9, 1, 4, 7, 3, 2, 8, 5, 6]))  # → 9
print(longest_consecutive_sequence([100, 200, 300]))  # → 1