
---

```markdown
# Day 23 Summary - Hash Tables & Graphs Practice, Bubble Sort Introduction

---

## **Date:** October 31, 2025 (Friday)

---

## **Main Achievements:**

1. **Typing Progress** - 30.6 WPM (slight dip, but consistent)
2. **Doubly Linked List Warm-Up** - Completed with corrections
3. **Hash Tables Practice** - 3 use cases implemented
4. **Graphs Practice** - BFS, DFS, pathfinding from memory
5. **Bubble Sort Learned** - First sorting algorithm mastered
6. **100% Daily Objectives** - All 8 objectives achieved (adjusted to 94%)

---

## **Morning Session: Typing & Warm-Up**

### **Typing Practice:**
- **Speed:** 30.6 WPM
- **Accuracy:** 94.69%
- **Status:** Slight dip from yesterday (31.4 WPM)

### **Analysis:**
- Still within normal variation range
- Overall average: 31.4 WPM, 96.1% accuracy
- Consistency is more important than daily peaks
- No concern - natural fluctuation

---

### **Warm-Up: Doubly Linked List (15 min)**

**Task:** Write complete Doubly Linked List class from memory

**Methods Implemented:**
1. `__init__()`
2. `prepend(data)`
3. `append(data)`
4. `delete(data)`
5. `display()`
6. `display_reverse()`

**Mistakes Made:**

**Mistake 1: Used `self.items = []` instead of `self.head` and `self.tail`**
```python
def __init__(self):
    self.items = []    # ❌ Doubly LL doesn't use a list!
```
**Correction:** Use `self.head = None` and `self.tail = None`

**Mistake 2: Checked `len(self.items)` instead of `self.head`**
```python
if len(self.items) == 0:    # ❌ No items list!
```
**Correction:** Check `if self.head is None:`

**Mistake 3: Swapped `append()` and `prepend()` logic**
- Thought append was front and prepend was back
- Had the implementations backwards

**Correction:** 
- **append** = add to **end** (both have 'e')
- **prepend** = add to **beginning** (pre = before)

**Mistake 4: Typo in method name**
```python
def preppend(self, data):    # ❌ Extra 'p'
```
**Correction:** `def prepend(self, data):`

**Result:** Completed successfully after corrections ✓

**Learning:** Need to reinforce the difference between append (end) and prepend (beginning)

---

## **Intensive Practice Session (30-40 min)**

### **Part 1: Hash Tables Practice (15-20 min)**

**Goal:** Implement 3 use cases and solve 2 problems

#### **Use Case 1: `find_duplicates(arr)` ✓**

**Purpose:** Find all duplicate elements in an array

**How it works:**
1. Create hash table
2. Count occurrences of each element
3. Return elements with count > 1

**Implementation:**
```python
def find_duplicates(array):
    ht = HashTable(len(array))
    
    # Count occurrences
    for num in array:
        count = ht.get(num)
        if count is None:
            count = 0
        ht.insert(num, count + 1)
    
    # Find duplicates
    duplicates = []
    for bucket in ht.table:
        for key, value in bucket:
            if value > 1:
                duplicates.append(key)
    
    return duplicates
```

**Test:** `[1, 2, 3, 2, 4, 1, 5]` → `[1, 2]` ✓

**Mistakes:**
- Initially tried to enumerate HashTable directly
- Fixed by looping through buckets manually

---

#### **Use Case 2: `two_sum(arr, target)` ✓**

**Purpose:** Find indices of two numbers that sum to target

**How it works:**
1. Create hash table to store `{number: index}`
2. For each number, calculate `complement = target - number`
3. Check if complement exists in hash table
4. If yes, return indices

**Implementation:**
```python
def two_sum(array, target):
    ht = HashTable(len(array))
    
    for i, num in enumerate(array):
        complement = target - num
        
        comp_index = ht.get(complement)
        if comp_index is not None:
            return [comp_index, i]
        
        ht.insert(num, i)
    
    return None
```

**Test:** `[2, 7, 11, 15]`, target `9` → `[0, 1]` ✓

**Result:** Perfect implementation!

---

#### **Use Case 3: `group_anagrams(words)` ✓**

**Purpose:** Group words that are anagrams of each other

**How it works:**
1. For each word, sort its letters to create a key
2. Use hash table: `{sorted_key: [list of words]}`
3. Words with same sorted key are anagrams

**Implementation:**
```python
def group_anagrams(words):
    ht = HashTable(len(words))
    
    for word in words:
        key = "".join(sorted(word))
        
        group = ht.get(key)
        if group is None:
            group = []
        
        group.append(word)
        ht.insert(key, group)
    
    result = []
    for bucket in ht.table:
        for key, group in bucket:
            result.append(group)
    
    return result
```

**Test:** `["eat", "tea", "tan", "ate", "nat", "bat"]`  
**Result:** `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]` ✓

---

**Hash Tables Practice Summary:**
- ✅ All 3 use cases implemented correctly
- ✅ Both problems solved
- ✅ Understanding of hash table patterns improving
- **Status:** 70% → 75% mastery

---

### **Part 2: Graphs Practice (15-20 min)**

**Goal:** Write BFS and DFS from memory, solve pathfinding problem

#### **BFS (Breadth-First Search) ✓**

**Implementation:**
```python
def bfs(self, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
    return result
```

**Mistake:**
- Used `if neighbour is not visited:` instead of `if neighbour not in visited:`
- Fixed: Use `not in` for membership checking

**Test:** Graph A-B-C-D-E → `A → B → C → D → E` ✓

---

#### **DFS (Depth-First Search) ✓**

**Implementation:**
```python
def dfs(self, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    
    for neighbour in self.graph[start]:
        if neighbour not in visited:
            result.extend(self.dfs(neighbour, visited))
    
    return result
```

**Mistake:**
- Forgot to add `start` to result initially
- Fixed: `result = [start]` instead of `result = []`

**Test:** Graph A-B-C-D-E → `A → B → D → C → E` ✓

---

#### **Shortest Path (using BFS) ✓**

**Implementation:**
```python
def shortest_path(self, start, end):
    if start == end:
        return [start]
    
    if start not in self.graph:
        return None
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        for neighbour in self.graph[node]:
            if neighbour == end:
                return path + [neighbour]
            
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))
    
    return None
```

**Mistake:**
- Forgot parentheses for tuple: `queue.append(neighbour, path + [neighbour])`
- Fixed: `queue.append((neighbour, path + [neighbour]))`

**Test:** A to E → `A → B → D → E` (4 nodes) ✓

---

**Graphs Practice Summary:**
- ✅ BFS implemented correctly
- ✅ DFS implemented correctly
- ✅ Shortest path working
- ✅ Understanding of graph traversal improving
- **Status:** 60% → 65% mastery

---

**Overall Intensive Practice Assessment:**

**Observation:** "That was tough, I will definitely need more practice on those, but it was still somewhat fresh in my mind"

**Analysis:**
- Hash Tables and Graphs are harder than Bubble Sort
- This is normal - data structures are more complex than algorithms
- Intensive practice is working as designed
- Skills are improving (70% → 75% for Hash Tables, 60% → 65% for Graphs)

**Plan:**
- Continue daily intensive practice
- Both will reach 90%+ with consistent practice
- Estimated 1-2 more weeks to mastery

---

## **Main Learning Session: Bubble Sort (1.5-2 hours)**

### **Introduction to Sorting Algorithms**

**What is Sorting?**
- Arranging elements in specific order (ascending/descending)
- Fundamental CS concept
- Asked in every technical interview

**Why Learn Sorting?**
- Understand algorithm efficiency
- Learn Big O notation
- Foundation for many problems
- Compare different approaches

---

### **Bubble Sort - The Simplest Sort**

#### **Concept:**

**"Bubble" larger elements to the end, one at a time**

**How it works:**
1. Compare adjacent elements
2. If left > right, swap them
3. Repeat until array is sorted

**Name origin:** Larger elements "bubble up" like bubbles in water

---

#### **Visual Understanding:**

**Array:** `[5, 2, 8, 1]`

**Pass 1:**
```
[5, 2, 8, 1] → [2, 5, 8, 1] (swap 5 and 2)
[2, 5, 8, 1] → [2, 5, 8, 1] (no swap)
[2, 5, 8, 1] → [2, 5, 1, 8] (swap 8 and 1)
Result: Largest (8) bubbled to end!
```

**Pass 2:**
```
[2, 5, 1, 8] → [2, 5, 1, 8] (no swap)
[2, 5, 1, 8] → [2, 1, 5, 8] (swap 5 and 1)
Result: Second largest (5) in position!
```

**Pass 3:**
```
[2, 1, 5, 8] → [1, 2, 5, 8] (swap 2 and 1)
Result: Sorted!
```

---

#### **Implementation:**

```python
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):              # For each pass
        for j in range(n - i - 1):  # Up to unsorted portion
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
```

**Understanding the loops:**

**Outer loop:** `for i in range(n)`
- Controls number of passes
- After pass i, last i elements are sorted

**Inner loop:** `for j in range(n - i - 1)`
- Compares adjacent elements
- `n - i - 1` skips already sorted elements

---

#### **Optimization: Early Exit**

**Problem:** Basic version always does n passes, even if sorted earlier

**Solution:** Add flag to detect when no swaps occur

```python
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False    # Track if any swaps occurred
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:    # No swaps = sorted!
            break
    
    return arr
```

**Impact:**
- Without: O(n²) even for sorted arrays
- With: O(n) for sorted arrays

---

#### **Time Complexity:**

**Worst Case:** O(n²)
- Array is reverse sorted
- Must do all comparisons and swaps

**Best Case:** 
- Without optimization: O(n²)
- With optimization: O(n) (already sorted)

**Average Case:** O(n²)

**Space Complexity:** O(1)
- Sorts in place
- No extra space needed

---

#### **When to Use Bubble Sort:**

**✅ Good for:**
- Educational purposes (simplest to understand)
- Small datasets (n < 10)
- Nearly sorted data (with optimization)
- Memory constraints (O(1) space)

**❌ Not good for:**
- Large datasets (too slow)
- Performance-critical applications
- Production code (use built-in sorts)

---

### **Implementation Practice:**

**First attempt:** Implemented with all optimizations ✓

**Test cases:**
```python
arr1 = [5, 2, 8, 1, 9]      → [1, 2, 5, 8, 9] ✓
arr2 = [64, 34, 25, 12, 22, 11, 90] → [11, 12, 22, 25, 34, 64, 90] ✓
arr3 = [1, 2, 3, 4, 5]      → [1, 2, 3, 4, 5] ✓ (early exit!)
```

**All tests passed!** ✓

---

### **Key Learning:**

**Observation:** "It's a lot easier to remember than all the graph and hashtable material"

**Why Bubble Sort is Easier:**
- **Simple pattern:** Compare adjacent, swap if needed
- **Two loops:** Easy to understand structure
- **One concept:** "Bubble" elements up
- **Visual:** Easy to trace execution

**Why Hash Tables/Graphs are Harder:**
- **Multiple concepts:** Many operations to remember
- **Abstract:** Harder to visualize
- **Application-based:** Need to know when/how to use
- **Many patterns:** Different use cases

**This is normal!**
- Algorithms are procedural (step-by-step)
- Data structures are conceptual (need deep understanding)
- With daily practice, Hash Tables/Graphs will become automatic too

---

## **Evening Drill (10-15 min)**

### **Task:** Write Bubble Sort from memory

**Time taken:** 5 minutes

**Result:** Perfect implementation ✓

**Code:**
```python
def bubble_sort(ar):
    n = len(ar)
    
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
                swapped = True
        if not swapped:
            break
    return ar
```

**Assessment:**
- Goal: Under 3 minutes
- Actual: 5 minutes
- Status: Close, but need more practice for speed

**Plan:** Add Bubble Sort to intensive practice tomorrow to build speed

---

## **Skills Reinforced:**

### **Technical Skills:**
✅ **Doubly Linked List** - All methods from memory  
✅ **Hash Tables** - 3 use cases (find_duplicates, two_sum, group_anagrams)  
✅ **Graphs** - BFS, DFS, shortest_path from memory  
✅ **Bubble Sort** - Understanding and implementation  
✅ **Algorithm analysis** - Time/space complexity  

### **Problem-Solving Skills:**
✅ **Pattern recognition** - Hash table use cases  
✅ **Algorithm selection** - BFS for shortest path  
✅ **Debugging** - Fixed multiple implementation errors  
✅ **Optimization** - Early exit for Bubble Sort  

### **Learning Skills:**
✅ **Self-assessment** - Recognized Hash Tables/Graphs need more practice  
✅ **Comparison** - Understood why algorithms are easier than data structures  
✅ **Adaptation** - Requested to add Bubble Sort to intensive practice  
✅ **Persistence** - Completed tough practice session  

---

## **Statistics:**

- **Time spent:** ~6-7 hours
- **Typing practice:** 30.6 WPM, 94.69% accuracy
- **Warm-up exercises:** 1 (Doubly Linked List - 6 methods)
- **Hash Table use cases:** 3 (find_duplicates, two_sum, group_anagrams)
- **Graph algorithms:** 3 (BFS, DFS, shortest_path)
- **Sorting algorithms learned:** 1 (Bubble Sort)
- **Lines of code:** ~250+
- **Test cases passed:** All ✓
- **Daily objectives:** 7.5/8 (94%)

---

## **Key Achievements:**

🏆 Doubly Linked List warm-up completed  
🏆 Hash Tables practice (3 use cases mastered)  
🏆 Graphs practice (BFS, DFS, pathfinding)  
🏆 Bubble Sort learned and implemented  
🏆 All test cases passed  
🏆 94% daily objectives achieved  
🏆 Recognized need for continued intensive practice  

---

## **Key Insights:**

### **On Intensive Practice:**
- Hash Tables and Graphs are challenging (as expected)
- Daily practice is working - skills improving (70%→75%, 60%→65%)
- Need 1-2 more weeks to reach 90%+ mastery
- This is normal and part of the process

### **On Bubble Sort:**
- Much easier to remember than data structures
- Algorithms are procedural, data structures are conceptual
- Simple pattern makes it easy to implement
- 5 minutes from memory (goal: under 3 minutes)

### **On Learning Differences:**
- **Algorithms:** Step-by-step, visual, pattern-based
- **Data Structures:** Conceptual, abstract, application-based
- Both require practice, but different types of understanding
- Data structures take longer to master

### **On Progress:**
- Typing consistent (30.6 WPM, overall 31.4 WPM average)
- Hash Tables: 70% → 75%
- Graphs: 60% → 65%
- Bubble Sort: 80% (new)
- Strong progress across all areas

---

## **Challenges Faced:**

1. **Doubly Linked List - append/prepend confusion**
   - Mixed up which adds to front vs back
   - Fixed: append = end (both have 'e'), prepend = beginning (pre = before)

2. **Hash Tables - looping through structure**
   - Tried to enumerate HashTable directly
   - Fixed: Loop through buckets manually

3. **Graphs - syntax errors**
   - Used `is not` instead of `not in`
   - Forgot parentheses for tuple
   - Fixed: Careful with Python syntax

4. **Bubble Sort - speed**
   - Took 5 minutes instead of 3
   - Solution: Add to intensive practice for speed building

**All challenges overcome through practice and corrections!**

---

## **Roadmap Status:**

**Current Milestone:** Data Structures (85% complete)

**Progress:**
- ✅ Milestone 1: Python Fundamentals (95%)
- ✅ Milestone 2: OOP (90%)
- 🟡 Milestone 3: Data Structures (85%)
  - Stack, Queue, Singly LL, Doubly LL: 90%+ (mastered)
  - BST: 85%
  - Hash Tables: 75% (improving)
  - Graphs: 65% (improving)
  - Bubble Sort: 80% (new)

**Timeline:**
- Day 23 of learning journey
- Estimated 1-2 weeks to complete Milestone 3
- Then move to Milestone 4 (Algorithms)

**Status:** On track, building deep mastery ✓

---

## **Tomorrow's Goals (Day 24 - Nov 1):**

**Morning:**
- Typing practice
- Warm-Up: Binary Search Tree

**Intensive Practice:**
- **Bubble Sort:** 2x from memory (under 3 min each) - NEW!
- **Hash Tables:** 3 more use cases, 2 problems
- **Graphs:** Shortest path variations, 2 problems

**Main Session:**
- Learn Selection Sort
- Implement from memory
- Compare with Bubble Sort

**Evening:**
- Selection Sort drill
- Review and plan

**Goal:** Continue building mastery, learn second sorting algorithm!

---

## **Reflections:**

Today was challenging but productive! The intensive practice session on Hash Tables and Graphs was tough, as expected. These are complex data structures that require deep understanding, not just memorization. The fact that I found them difficult is actually a good sign - it means I'm engaging with the material at the right level.

The contrast with Bubble Sort was interesting. I found it much easier to understand and implement because algorithms are more procedural - they're step-by-step instructions. Data structures, on the other hand, are conceptual - you need to understand not just how they work, but when and why to use them.

The key insight today was recognizing that Hash Tables and Graphs need more practice, and that's okay. The intensive practice phase is designed for exactly this - daily focused practice until these structures become automatic. I'm already seeing improvement (Hash Tables 70%→75%, Graphs 60%→65%), and with continued daily practice, I'll reach 90%+ mastery in 1-2 weeks.

Adding Bubble Sort to intensive practice tomorrow is a smart move. It'll help me build speed (currently 5 min, goal 3 min) and create a solid foundation before learning Selection Sort. Having one sort automatic will make it easier to compare and contrast different sorting algorithms.

The new learning strategy is working well. Daily objectives keep me accountable, intensive practice targets weak areas, and the evening drill reinforces new learning. I'm building both breadth (learning new topics) and depth (mastering through practice).

Ready to continue tomorrow with Binary Search Tree warm-up, more Hash Tables/Graphs practice, and Selection Sort!

---

## **Personal Notes:**

- Typing: 30.6 WPM (slight dip, but consistent overall)
- Hash Tables and Graphs are tough but improving
- Bubble Sort is easier to remember (algorithms vs data structures)
- Need to build speed on Bubble Sort (5 min → 3 min goal)
- Intensive practice is working as designed
- Feeling good about progress despite challenges
- Ready for Selection Sort tomorrow

---

## **Resources Used:**

- Doubly Linked List review
- Hash Tables use cases (find_duplicates, two_sum, group_anagrams)
- Graph algorithms (BFS, DFS, shortest_path)
- Bubble Sort theory and implementation
- Algorithm analysis (Big O notation)
- Optimization techniques (early exit)

---

## **Next Session Preview:**

- Binary Search Tree warm-up
- Bubble Sort intensive practice (2x, under 3 min)
- Hash Tables & Graphs continued practice
- Selection Sort introduction

---

**Total Days Completed:** 23/60 (Phase 1)  
**Progress:** Ahead of schedule ✓  
**Confidence Level:** High 💪  
**Data Structures:** 7/7 learned, 4/7 mastered, 3/7 practicing  
**Sorting Algorithms:** 1/6 learned (Bubble Sort)  
**Daily Objectives:** 94% achieved ✓  

---

End of Day 23 Summary
```