"""Day 26: Intensive Practice - Hash Tables"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import HashTable, Graph

# HashTables

# Case 1:
def isomorphic_strings(s, t):
    s_to_t = HashTable(len(s))
    t_to_s = HashTable(len(t))

    # create maps and check them
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if char_s is already mapped
        mapped_t = s_to_t.get(char_s)
        if mapped_t is not None:
            # It's already mapped - does it map to the same character?
            if mapped_t != char_t:
                return False # Conflict, mapped to different character
        else:
            s_to_t.insert(char_s, char_t) # Not mapped yet, create map
        
        # Check if char_t is already mapped (reverse direction now)
        mapped_s = t_to_s.get(char_t)
        if mapped_s is not None:
            # It's already mapped - does it map to the same character?
            if mapped_s != char_s:
                return False # Conflict
        else:
            t_to_s.insert(char_t, char_s) # Not mapped yet, create map
    
    return True # No conflicts, they are isomophic

print(isomorphic_strings("egg", "add"))     # True
print(isomorphic_strings("foo", "bar"))     # False
print(isomorphic_strings("paper", "title")) # True
print(isomorphic_strings("badc", "baba"))   # False

# Case 2:
def contains_duplicate_within_k(arr, k):
    ht = HashTable(len(arr))

    # Loop
    for i in range(len(arr)):
        num = arr[i]

        # Check if seen
        last_index = ht.get(num)
        # Check distance from current to last
        if last_index is not None:
            distance = i - last_index
            # if distance is <= k
            if distance <= k:
                return True 

        # Update last index to current
        ht.insert(num, i)
    
    return False # Loop finished

print(contains_duplicate_within_k([1, 2, 3, 1], 3))         # True
print(contains_duplicate_within_k([1, 0, 1, 1], 1))         # True
print(contains_duplicate_within_k([1, 2, 3, 1, 2, 3], 2))   # False
print(contains_duplicate_within_k([99, 99], 2))             # True
