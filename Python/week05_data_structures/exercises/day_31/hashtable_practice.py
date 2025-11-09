"""Day 31: Instensive Practice - Hash Tables (Pattern)"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

# Problem 1: (12min)
# Start: 14:30
def two_sum(arr, target):
    ht = HashTable(len(arr))
    result = []
    for i, num in enumerate(arr):
        complement = target - num
        exist = ht.get(complement)
        if exist is not None:
            result.append(exist)
            result.append(i)
            return result
        ht.insert(num, i)
    return result

print(two_sum([2, 7, 11, 15], 9))   # → [0, 1]
print(two_sum([3, 2, 4], 6))        # → [1, 2]
print(two_sum([3, 3], 6))           # → [0, 1]

# Problem 2: (12min)
# Start: 14:50
def first_unique_index(s):
    ht = HashTable(len(s))
    result = -1

    for num in s:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    
    for i, num in enumerate(s):
        if ht.get(num) == 1:
            result = i
            return result
        
    return result

print(first_unique_index("leetcode"))      # → 0
print(first_unique_index("loveleetcode"))  # → 2
print(first_unique_index("aabb"))          # → -1

# Problem 3:
# Start: 15:05
def longest_substring_without_repeating(s): # Sliding Window
    ht = HashTable(len(s))
    max_length = 0
    start = 0   # Start of window
    
    for i, char in enumerate(s):
        current_char = ht.get(char)    # have we seen this character before?
        if current_char is not None and current_char >= start:    # if we have and its in our current window
            start = current_char + 1   # move start to after the last occurrence
        ht.insert(char, i)  # update last seen position of this character
        # calculate current length of the window
        current_length = i - start + 1
        max_length = max(max_length, current_length)
    
    return max_length

print(longest_substring_without_repeating("abcabcbb"))  # → 3
print(longest_substring_without_repeating("bbbbb"))     # → 1
print(longest_substring_without_repeating("pwwkew"))    # → 3
print(longest_substring_without_repeating(""))          # → 0

# Problem 4:
# Start 15:35
def find_anagram_indices(s, p):
    if len(p) > len (s):
        return []
    
    htp = HashTable(len(p))
    for char in p:
        count = htp.get(char)
        if count is None:
            count = 0
        htp.insert(char, count + 1)
    
    window_count = HashTable(len(p))
    window_size = len(p)

    for i in range(window_size):
        char = s[i]
        count = window_count.get(char)
        if count is None:
            count = 0
        window_count.insert(char, count + 1)
    
    result = []

    def counts_match():
        for bucket in htp.table:
            for char, count in bucket:
                if window_count.get(char) != count:
                    return False
        return True
    
    if counts_match():
        result.append(0)
    
    for i in range(window_size, len(s)):
        new_char = s[i]
        count = window_count.get(new_char)
        if count is None:
            count = 0
        window_count.insert(new_char, count + 1)

        old_char = s[i - window_size]
        count = window_count.get(old_char)
        window_count.insert(old_char, count - 1)

        if counts_match():
            result.append(i - window_size + 1)
    
    return result

print(find_anagram_indices("cbaebabacd", "abc"))  # → [0, 6]
print(find_anagram_indices("abab", "ab"))         # → [0, 1, 2]