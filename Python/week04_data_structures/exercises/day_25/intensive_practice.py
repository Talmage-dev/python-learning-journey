

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

def find_pairs_with_sum(arr, target):
    ht = HashTable(len(arr))
    pairs = []
    for num in arr:
        looking_for = target - num
        if ht.get(looking_for) is not None:                         # Check if we've seen the complement
            pair = (min(num, looking_for), max(num, looking_for))   # Found a pair, Add it(smaller first to avoid duplicates)
            if pair not in pairs:                                   # Avoid duplicates
                pairs.append(pair)
        ht.insert(num, True)                                        # Mark this number as seen
    return pairs
        
def longest_substring_without_repeating(s):
    ht = HashTable(len(s))
    start = 0
    max_length = 0
    for i,char in enumerate(s):
        if ht.get(char) is not None and ht.get(char) >= start:      # If we've seen this character in current window
            start = ht.get(char) + 1                                # Move window start forward
        ht.insert(char, i)                                          # Update this character's position
        current_length = i - start + 1                              # Get current length
        max_length = max(max_length, current_length)                # Update max length
    return max_length                                               # Return max length

# Test both:
# Test A
print(find_pairs_with_sum([1, 2, 3, 4, 5], 6))  # [(1, 5), (2, 4)]
print(find_pairs_with_sum([1, 2, 3, 4, 5], 7))  # [(2, 5), (3, 4)]

# Test B
print(longest_substring_without_repeating("abcabcbb"))  # 3
print(longest_substring_without_repeating("bbbbb"))     # 1
print(longest_substring_without_repeating("pwwkew"))    # 3

# Problem 2:
def first_non_repeating_char(s):
    ht = HashTable(len(s))
    # Count Occurrances
    for char in s:
        count = ht.get(char)         
        if count is None:           
            count = 0               
        ht.insert(char, count + 1)   
    # Find unique first element
    for char in s:
        if ht.get(char) == 1:
            return char
    return None

# Test:
print(first_non_repeating_char("leetcode"))  # 'l'
print(first_non_repeating_char("loveleetcode"))  # 'v'
print(first_non_repeating_char("aabb"))  # None
