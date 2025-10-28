# Day 20 Summary - Hash Tables Learned

---

## **Date:** October 28, 2025 (Tuesday)

---

## **Main Achievements:**

1. **Typing Progress** - Hit 35.7 WPM (new personal best!)
2. **Morning Warm-Up** - 5 exercises across all structures
3. **Learned Hash Tables** - 6th data structure!
4. **Built Hash Table** - Complete implementation from scratch

---

## **Morning Session: Typing & Warm-Up**

### **Typing Practice:**
- **Speed:** 35.7 WPM 🎉 **NEW PERSONAL BEST!**
- **Accuracy:** 96.5%
- **Weak keys progress:**
  - 'a': 28.2 → 27.9 WPM (slight dip but still strong)
  - 'r': 22.6 → **26.5 WPM** (+3.9!) **HUGE IMPROVEMENT!**

### **Analysis:**
- New personal best speed!
- 'r' key had breakthrough (+17% in one day!)
- Keybr's focused practice is working perfectly
- Should see fewer 'r' typos in code now

---

### **Mini "Wax On Wax Off" (5 exercises):**

**Random selection from all 5 structures:**

1. ✅ BST - `insert()` - Correct first try
2. ✅ Queue - `is_empty()` - Correct first try
3. ✅ Doubly LL - `prepend()` - Correct first try
4. ❌ Stack - `peek()` - Used index 0 instead of -1 (mixed up with Queue)
5. ❌ BST - `_search_recursive()` - Used `self.node` instead of `node` parameter

**Result:** 5/5 completed, 2 small mistakes caught and fixed

**Mistakes Analysis:**
1. **Stack peek** - Confused LIFO (index -1) with FIFO (index 0)
2. **BST search** - Used wrong variable (self.node vs node parameter)

**Both fixed immediately!** All structures still solid! ✓

---

## **Learning Session: Hash Tables**

### **What is a Hash Table?**

A data structure that stores **key-value pairs** with **O(1) average lookup time**.

**Real-world examples:**
- Python dictionaries (they ARE hash tables!)
- Phone book (name → number)
- Dictionary (word → definition)
- Database indexes
- Caches

---

### **Key Concepts Learned:**

#### **1. Hash Function**

Converts a key into an index:

```python
def _hash(self, key):
    return hash(key) % self.size

# Example:
hash("apple") = 5647382910    # Big number
5647382910 % 10 = 0           # Index in table

Properties:
- Deterministic (same input → same output)
- Fast (O(1))
- Uniform distribution
- Not reversible

Key insight: The hash value is NOT a memory location - it's a deterministic number generated from the key's content!

- - -

2. Structure

A list of lists (buckets):
self.table = [
    [],                          # Index 0 (empty)
    [("cat", "meow")],           # Index 1 (one item)
    [("dog", "woof"),            # Index 3 (collision!)
     ("pig", "oink")],
    [("apple", "red")],          # Index 4 (one item)
] 

Important understanding:
- Index is just a number (0, 1, 2...)
- Keys are stored INSIDE tuples
- Each bucket can hold multiple (key, value) pairs

- - -

3. Collisions

When two keys hash to the same index:
hash("apple") % 10 = 5
hash("grape") % 10 = 5  # Collision!

Solution: Chaining
- Store both at same index in a list
- table[5] = [("apple", "red"), ("grape", "purple")]

- - -

4. Why So Fast?

Traditional search (O(n)):
for item in list:  # Check EVERY item
    if item.key == "apple":
        return item.value

Hash table (O(1)):
index = hash("apple") % 10     # Know exactly where to look!
for k, v in table[index]:      # Only check ONE bucket
    if k == "apple":
        return v

Key insight: Hash function tells us exactly which bucket to check, so we skip most of the table!

- - -

Implementation Built:

Methods Implemented:

1. __init__ (size=10) - Initialize table with empty buckets
2. _hash(key) - Convert key to index
3. insert(key, value) - Add or update key-value pair
4. get(key) - Retrieve value by key
5. delete(key) - Remove key-value pair
6. display() - Show all items

- - -

Insert Method - Key Logic:
def insert(self, key, value):
    index = self._hash(key)
    
    # Check if key exists, update if so
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            self.table[index][i] = (key, value)  # Update!
            return
    
    # Otherwise append (new key or collision)
    self.table[index].append((key, value))

Two scenarios handled:
1. Key exists → Update value (no duplicate keys!)
2. Key is new → Append to bucket (handles collisions)

Important understanding: Hash tables don't allow duplicate keys - one key can only have one value!

- - -

Test Results:
=== After Inserting ===
Index 2: [('orange', 'orange fruit')]
Index 4: [('apple', 'red fruit'), ('grape', 'purple fruit')]  ← Collision!
Index 9: [('banana', 'yellow fruit')]

=== Getting Values ===
apple: red fruit
banana: yellow fruit
cherry: None  ← Not found

=== Updating apple ===
apple: green fruit  ← Updated!

=== Deleting banana ===
Index 2: [('orange', 'orange fruit')]
Index 4: [('apple', 'green fruit'), ('grape', 'purple fruit')]
← banana gone!

=== Testing More Items ===
Index 1: [('dog', 'woof')]
Index 2: [('orange', 'orange fruit')]
Index 4: [('apple', 'green fruit'), ('grape', 'purple fruit')]
Index 5: [('pig', 'oink')]
Index 8: [('cat', 'meow')]

Perfect output! ✓
- Collision handling worked (apple & grape at index 4)
- Update worked (apple: red → green)
- Delete worked (banana removed)
- Get worked (cherry returned None)
- Distribution across indices

- - -

Conceptual Breakthroughs:

Breakthrough 1: Understanding the Hash Value

Initial confusion: Is the big number a memory location?

Clarification: No! It's a deterministic number generated from the key's content.

- Same input always gives same output
- Like a fingerprint for the key
- Fast to compute
- Spreads values evenly

Breakthrough 2: Understanding the Structure

Initial confusion: Is the index the key?
Clarification: No! The structure is:

- Index is just a number (0, 1, 2...)
- Keys are stored INSIDE tuples at each index
- table[5] = [("apple", "red"), ("grape", "purple")]

Breakthrough 3: Understanding the Search

Initial confusion: Do we search for the big number?

Clarification: Two-step process:
1. Hash key → Get index (O(1))
2. Search that specific bucket for key (O(1) average)

Why it's fast: We only check ONE bucket, not the whole table!

Breakthrough 4: Understanding Collisions vs Updates

Initial confusion: Is the loop for collisions?

Clarification: The loop handles BOTH:
1. Update - Same key, new value (replace old)
2. Collision - Different key, same index (append)

Key insight: One key = one value (no duplicates!)

- - -

Skills Reinforced:

Technical Skills:
✅ Hash function implementation - Convert key to index
✅ Collision handling - Chaining with lists
✅ Insert logic - Update vs append
✅ Search optimization - Direct bucket access
✅ Delete operation - Remove from bucket
✅ Tuple unpacking - for k, v in bucket
✅ Enumerate usage - for i, (k, v) in enumerate
✅ List comprehension - [[] for _ in range(size)]

Problem-Solving Skills:
✅ Asking clarifying questions - Understanding concepts deeply
✅ Visual thinking - Drawing mental models
✅ Pattern recognition - Similar to dictionaries
✅ Testing - Comprehensive test cases
✅ Debugging - Syntax errors caught quickly

Learning Skills:
✅ Conceptual understanding - Not just memorizing
✅ Asking "why" - Understanding the reasoning
✅ Building mental models - Visualizing structure
✅ Connecting concepts - Relating to Python dicts

- - -

Statistics:

Time spent: ~4-5 hours
Typing practice: 35.7 WPM, 96.5% accuracy (best!)
Warm-up exercises: 5
New data structure: Hash Tables (6th!)
Methods implemented: 6
Test cases: 8
Conceptual breakthroughs: 4
Lines of code: ~60 (Hash Table implementation)

- - -

Key Achievements:

🏆 Hit 35.7 WPM (new personal best!)
🏆 'r' key breakthrough (+17% improvement!)
🏆 Learned Hash Tables (6th data structure!)
🏆 Built complete hash table from scratch
🏆 All methods working perfectly
🏆 Handled collisions correctly
🏆 Deep conceptual understanding
🏆 Connected to Python dictionaries
🏆 All 5 previous structures still solid

- - -

Key Insights:

On Hash Tables:

- They're what Python dictionaries are built on!
- O(1) lookup is incredibly powerful
- Hash function is the magic that makes it fast
- Collisions are normal and handled with chaining
- One key can only have one value
- Trade-off: Speed for no order

On Learning:

- Asking clarifying questions leads to deep understanding
- Visual models help grasp abstract concepts
- Connecting new concepts to familiar ones (Python dicts) helps
- Building from scratch solidifies understanding
- Testing reveals how it actually works

On Typing:

- Weak key practice is working!
- 'r' key improved 17% in one day
- Should see fewer typos in code
- Consistent practice pays off
- Speed steadily increasing

On Retention:

- Daily warm-ups keep skills sharp
- All 5 previous structures still solid
- Small mistakes caught and fixed quickly
- Muscle memory building
- Confidence growing

- - -

Challenges Faced:

1. Understanding hash value
- Thought it was memory location
- Clarified: Deterministic number from key content
- Learning: Ask questions when confused

2. Understanding structure
- Thought index was the key
- Clarified: Index is number, keys inside tuples
- Learning: Visual models help

3. Understanding search process
- Thought we search for big number
- Clarified: Hash → index, then search bucket
- Learning: Two-step process

4. Understanding insert loop
- Thought it was only for collisions
- Clarified: Handles both update and collision
- Learning: One piece of code, two purposes

5. Syntax error in append
- Wrote self.table[index.append]
- Fixed: self.table[index].append
- Learning: Slow down on syntax

All challenges overcome through asking questions and clarification!

- - -

Roadmap Status:

AHEAD OF SCHEDULE! 🚀

Current: Day 20 (Oct 28)
Original plan: Should be finishing Week 3
Actual progress: Week 5-6 (Data Structures) - 6 structures learned!
Ahead by: ~2-3 weeks

Data Structures Progress:

1. ✅ Stacks (Day 13) - MASTERED
2. ✅ Queues (Day 13) - MASTERED
3. ✅ Singly Linked Lists (Day 14) - MASTERED
4. ✅ Doubly Linked Lists (Day 14) - MASTERED
5. ✅ Binary Search Trees (Day 16) - MASTERED
6. ✅ Hash Tables (Day 20) - LEARNED TODAY!
7. ⬜ Graphs (next)

6 out of 7 data structures complete!

- - -

Personal Milestone:

Language Learning Plan Created!

Set up 3-6 year roadmap to learn 6 languages:

1. Spanish
2. French
3. Portuguese
4. Arabic
5. Mandarin
6. German

Plan:

1 hour/day language learning alongside coding!

This shows:

Commitment to continuous learning and growth! 🌍

- - -

Tomorrow's Goals (Day 21 - Oct 29):

Morning:
- Typing practice (aim for 36+ WPM)
- Mini warm-up (last 3 days including Hash Tables)

Main Session:
- Hash Tables "Wax On Wax Off" practice
- Build application project using Hash Tables
- Possibly start Graphs (7th and final data structure!)

Goal: Solidify Hash Tables and complete data structures!

- - -

Reflections:

Today was excellent! Learning Hash Tables felt natural because I could connect it to Python dictionaries I've been using all along. The "aha!" moment was realizing that dictionaries ARE hash tables - suddenly everything clicked.

The conceptual breakthroughs came from asking clarifying questions. When I was confused about whether the hash value was a memory location, asking led to understanding it's a deterministic number. When I thought the index was the key, asking revealed the actual structure. This pattern of asking "why" and "how" leads to deep understanding, not just surface memorization.

Building the hash table from scratch was satisfying. Each method built on the previous one, and seeing it all work together in the test was rewarding. The collision handling (apple and grape both at index 4) proved the chaining works. The update logic (apple: red → green) showed one key = one value. The delete (banana removed) demonstrated proper removal.

The typing breakthrough on the 'r' key (+17% in one day!) is huge. Going from 22.6 to 26.5 WPM means it's catching up to my other keys. This should reduce typos in code like "recusive" instead of "recursive". Keybr's algorithm is working perfectly.

The morning warm-up continues to work well. All 5 previous structures are still solid - just 2 small mistakes that I caught and fixed immediately. The daily practice is building muscle memory and confidence.

Creating the language learning plan shows I'm thinking long-term about continuous growth. Balancing coding (2-4 hours) with language learning (1 hour) is sustainable and exciting.

Ready to practice Hash Tables tomorrow and possibly finish all 7 data structures!

- - -

Personal Notes:

- Typing: 35.7 WPM, 96.5% accuracy (best yet!)
- 'r' key breakthrough: +17% improvement!
- Hash Tables clicked quickly
- Connected to Python dictionaries
- All previous structures still solid
- Language learning plan created
- Feeling great about progress
- 6/7 data structures complete!

- - -

Resources Used:

- Morning warm-up routine
- Hash Tables theory and examples
- Step-by-step implementation
- Comprehensive testing
- Clarifying questions and answers
- Visual models and diagrams

- - -

Next Session Preview:

- Hash Tables practice
- Application project
- Possibly start Graphs
- Complete all 7 data structures!

- - -

Total Days Completed: 20/60 (Phase 1)
Progress: Ahead of schedule ✓
Confidence Level: Very High 💪
Data Structures: 6/7 mastered!
Typing Speed: 35.7 WPM (best!) ✓
Retention Strategy: Working perfectly ✓
Language Learning: Plan created ✓

- - -

End of Day 20 Summary