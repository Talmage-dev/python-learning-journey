# Day 20: Hash Tables Reference

## Date: October 28, 2025 (Tuesday)

---

## What is a Hash Table?

A **hash table** is a data structure that stores **key-value pairs** with **super fast lookup** - O(1) average time!

**Real-world examples:**
- Python dictionaries
- Phone book (name → phone number)
- Dictionary (word → definition)
- Database indexes
- Caches

---

## Key Concepts

### 1. Hash Function

Converts a key into an index (array position):

```python
Key → Hash Function → Index → Value

"apple" → hash("apple") → 5 → "red fruit"
"banana" → hash("banana") → 2 → "yellow fruit"

How it works:

def _hash(self, key):
    return hash(key) % self.size

# Example:
hash("apple") = 5647382910    # Big number
5647382910 % 10 = 0           # Fits in table (index 0)

Properties:
- Deterministic - Same input always gives same output
- Fast - O(1) computation
- Uniform distribution - Spreads values evenly
- Not reversible - Can't get key from hash

- - -

2. Structure
self.table = [
    [],                           # Index 0 (empty)
    [("cat", "meow")],           # Index 1 (one item)
    [],                           # Index 2 (empty)
    [("dog", "woof"),            # Index 3 (collision! two items)
     ("pig", "oink")],
    [("apple", "red")],          # Index 4 (one item)
    # ... etc
]

Each bucket can hold:
- Zero items (empty)
- One item (no collision)
- Multiple items (collision handled by chaining)

- - -

3. Collisions

What is a collision? When two different keys hash to the same index:
hash("apple") % 10 = 5
hash("grape") % 10 = 5  # Collision!

Solution: Chaining Store multiple items at the same index in a list:
table[5] = [("apple", "red"), ("grape", "purple")]

Visual:
Index 5: [🍎 apple, 🍇 grape]  ← Both stored here!

- - -

4. Operations

Insert - O(1) average
def insert(self, key, value):
    index = self._hash(key)
    
    # Check if key exists, update if so
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            self.table[index][i] = (key, value)  # Update
            return
    
    # Otherwise append (new key or collision)
    self.table[index].append((key, value))

Two scenarios:

1. Key exists → Update value (no duplicates!)
2. Key is new → Append to bucket (handles collisions)

Get - O(1) average
def get(self, key):
    index = self._hash(key)
    
    # Search for key in bucket
    for k, v in self.table[index]:
        if k == key:
            return v
    
    return None  # Not found

Why so fast:
- Hash tells us exactly which bucket to check
- Only search one bucket, not entire table!

Delete - O(1) average
def delete(self, key):
    index = self._hash(key)
    
    # Search for key in bucket
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            del self.table[index][i]
            return True
    
    return False  # Not found

- - -

Complete Implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Convert key to index"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Add or update key-value pair"""
        index = self._hash(key)
        
        # Check if key exists, update if so
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        # Otherwise append
        self.table[index].append((key, value))
    
    def get(self, key):
        """Get value by key"""
        index = self._hash(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        """Remove key-value pair"""
        index = self._hash(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        
        return False
    
    def display(self):
        """Show all key-value pairs"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

- - -

Time Complexity

| Operation | Average | Worst Case |

|-----------|---------|------------|

| Insert    | O(1)    | O(n)       |

| Get       | O(1)    | O(n)       |

| Delete    | O(1)    | O(n)       |

| Space     | O(n)    | O(n)       |

Why "average" vs "worst"?
- Average: Few collisions, small buckets
- Worst: All keys hash to same index (one big bucket)

- - -

When to Use Hash Tables

✅ Use when you need:
- Fast lookup by key
- Key-value associations
- Counting occurrences
- Removing duplicates
- Caching/memoization
- Checking membership
❌ Don't use when you need:
- Sorted order (use BST instead)
- Range queries
- Ordered iteration
- Minimum/maximum values

- - -

Comparison with Other Structures

Hash Table vs List

Hash Table:
- Lookup: O(1)
- No order
- Key-value pairs

List:
- Lookup: O(n)
- Maintains order
- Index-value pairs

Hash Table vs BST

Hash Table:
- Lookup: O(1) average
- No order
- Simple implementation

BST:
- Lookup: O(log n)
- Sorted order
- In-order traversal
- Range queries

Hash Table vs Dictionary (Python)

They're the same! Python dictionaries ARE hash tables!
# Python dict
d = {"apple": "red"}
d["apple"]  # O(1) lookup

# Your hash table
ht = HashTable()
ht.insert("apple", "red")
ht.get("apple")  # O(1) lookup

- - -

Common Patterns

Pattern 1: Counting Occurrences
def count_words(text):
    ht = HashTable()
    for word in text.split():
        count = ht.get(word) or 0
        ht.insert(word, count + 1)
    return ht

Pattern 2: Removing Duplicates
def remove_duplicates(items):
    ht = HashTable()
    result = []
    for item in items:
        if ht.get(item) is None:
            ht.insert(item, True)
            result.append(item)
    return result

Pattern 3: Two Sum Problem
def two_sum(nums, target):
    ht = HashTable()
    for i, num in enumerate(nums):
        complement = target - num
        if ht.get(complement) is not None:
            return [ht.get(complement), i]
        ht.insert(num, i)
    return None

- - -

Key Insights

Why Hash Tables are Fast:

1. Direct access - Hash tells us exactly where to look
2. No searching - Don't check every item
3. Small buckets - Even with collisions, buckets are tiny

The Trade-off:

Pros:
- Super fast lookup (O(1))
- Simple to use
- Flexible keys

Cons:
- No order
- Extra space for empty buckets
- Hash function overhead
- Collisions can slow down

Load Factor:
load_factor = number_of_items / table_size

# Good: 0.7 or less (70% full)
# Bad: > 1.0 (more items than buckets)

When load factor gets high:
- More collisions
- Slower operations
- Solution: Resize table (rehashing)

- - -

Common Mistakes

Mistake 1: Trying to have multiple values per key
# ❌ Wrong - can't have two values for same key
ht.insert("apple", "red")
ht.insert("apple", "green")
# Result: "apple" → "green" (updated, not both!)

# ✓ Right - use list as value
ht.insert("apple", ["red", "green"])

Mistake 2: Forgetting to check if key exists
# ❌ Wrong - might return None
value = ht.get("apple")
value.upper()  # Crashes if None!

# ✓ Right - check first
value = ht.get("apple")
if value:
    value.upper()

Mistake 3: Modifying keys after insertion
# ❌ Wrong - hash changes!
key = [1, 2, 3]  # Mutable list
ht.insert(key, "value")
key.append(4)  # Hash is now different!
ht.get(key)  # Won't find it!

# ✓ Right - use immutable keys
key = (1, 2, 3)  # Tuple
ht.insert(key, "value")

- - -

Summary

Hash Table:
- Stores key-value pairs
- O(1) average lookup
- Uses hash function to find index
- Handles collisions with chaining
- Same concept as Python dictionaries

Key Methods:
insert(key, value) - Add or update
get(key) - Retrieve value
delete(key) - Remove pair
_hash(key) - Convert key to index

When to use:
- Need fast lookup
- Key-value associations
- Counting, caching, deduplication

- - -

End of Day 20 Reference