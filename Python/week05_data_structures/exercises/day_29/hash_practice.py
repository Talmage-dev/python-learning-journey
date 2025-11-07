"""Day 29: Intensive Practice - HashTables (Counting)"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable

# Start: 12:35
# Finished: 12:47
# Case 1: (15min)
def first_non_repeating_char(s):
    ht = HashTable(len(s))
    for char in s:
        count = ht.get(char) 
        if count is None:
            count = 0
        ht.insert(char, count +1)
    for k in s:
        value = ht.get(k)
        if value == 1:
            return k
    return None

# Test:
print(first_non_repeating_char("leetcode"))      # → "l"
print(first_non_repeating_char("loveleetcode"))  # → "v"
print(first_non_repeating_char("aabb"))          # → None

# Case 2:
# Start: 12:50
# Finish: 12:57
def most_frequent_element(arr):
    ht = HashTable(len(arr))
    for num in arr:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    highest_count = 0
    highest_num = 0
    for k in arr:
        v = ht.get(k)
        if v > highest_count:
            highest_count = v
            highest_num = k
    return highest_num

# Test:
print(most_frequent_element([1, 3, 2, 1, 4, 1]))
# → 1 (appears 3 times)

print(most_frequent_element([1, 2, 2, 3, 3, 3]))
# → 3 (appears 3 times, most frequent)

print(most_frequent_element([5, 5, 5, 1, 1, 1]))
# → 5 or 1 (both appear 3 times, either is correct)

# Case 3:
# Start: 1:00pm
# Finished: 1:16(needed help)
def can_form_pairs(arr):
    ht = HashTable(len(arr))
    for num in arr:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    for bucket in ht.table:
        for k, v in bucket:
            if v % 2 != 0:
                return False
    return True

# Test:
print(can_form_pairs([1, 2, 3, 1, 2, 3]))
# → True (each number appears 2 times - even)

print(can_form_pairs([1, 2, 3, 1, 2]))
# → False (3 appears 1 time - odd)

print(can_form_pairs([1, 1, 2, 2, 3, 3, 4, 4]))
# → True (all appear even number of times)

print(can_form_pairs([5]))
# → False (5 appears 1 time - odd)

# Case 4:
# Start: 1:20pm
# Finished: 1:35pm
def find_pairs_with_sum(arr, target):
    ht = HashTable(len(arr))

    for num in arr:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    
    pairs = 0
    checked = set()

    for bucket in ht.table:
        for k, v in bucket:
            if k in checked:
                continue
            complement = target - k
            if k == complement:
                pairs += v // 2
            else:
                complement_count = ht.get(complement)
                if complement_count:
                    pairs += min(v, complement_count)
                    checked.add(complement)
            checked.add(k)
    return pairs

print(find_pairs_with_sum([1, 2, 3, 4, 5], 6))    # → 2
print(find_pairs_with_sum([1, 1, 1, 1], 2))       # → 2
print(find_pairs_with_sum([1, 2, 3], 10))         # → 0