
---

```markdown
# Day 21 Summary - Hash Tables Mastered, Graphs Learned, New Warm-Up Routine

---

## **Date:** October 29, 2025 (Wednesday)

---

## **Main Achievements:**

1. **Typing Practice** - 29.2 WPM (off day, but normal variation)
2. **Morning Warm-Up** - 5 exercises across all structures
3. **Hash Tables Mastered** - All 6 methods (12 exercises)
4. **Word Frequency Counter** - Complete application built
5. **Graphs Learned** - 7th and final data structure!
6. **Basic Graph Built** - All methods working
7. **New Warm-Up Routine** - 3-part system established
8. **Stack Application Practice** - 3 use-case functions

---

## **Morning Session: Typing & Warm-Up**

### **Typing Practice:**
- **Speed:** 29.2 WPM
- **Accuracy:** 95.2%
- **Status:** Off day (down from 35.7 WPM yesterday)

### **Analysis:**
- Natural variation - everyone has off days
- Still maintaining 95%+ accuracy
- Average remains around 32-33 WPM
- Not a concern - just random fluctuation

---

### **Mini "Wax On Wax Off" (5 exercises):**

**Random selection from all 6 structures:**

1. ✅ Hash Table - `_hash()` - Correct first try
2. ✅ BST - `inorder()` - Correct first try
3. ✅ Queue - `enqueue()` - Correct first try
4. ❌ Hash Table - `get()` - Forgot `for` keyword in loop
5. ✅ Doubly LL - `delete()` - Correct first try

**Result:** 5/5 completed, 1 small mistake caught and fixed

**First time including Hash Tables in warm-up!** All 6 structures still solid! ✓

---

## **Part 1: Hash Tables "Wax On Wax Off"**

### **Goal:** Master all Hash Table methods

**Methods Practiced (6 methods × 2 = 12 exercises):**

**Round 1:**
1. ✅ `__init__` - Correct
2. ✅ `_hash` - Correct
3. ❌ `insert` - Used loop variables `k, v` instead of parameters `key, value`
4. ✅ `get` - Correct
5. ✅ `delete` - Correct
6. ❌ `display` - Typo: `self.tables` instead of `self.table`

**Round 2:**
7. ✅ `__init__` - Correct → **MASTERED!**
8. ✅ `_hash` - Correct → **MASTERED!**
9. ✅ `insert` - Correct → **MASTERED!**
10. ✅ `get` - Correct → **MASTERED!**
11. ✅ `delete` - Correct → **MASTERED!**
12. ✅ `display` - Correct → **MASTERED!**

**Result:** All 6 Hash Table methods mastered! 🎉

### **Mistakes Analysis:**

**Mistake 1: Insert - Wrong variables**
```python
self.table[index][i] = (k, v)    # ❌ Loop variables
self.table[index].append((k, v))  # ❌ Loop variables
```
**Learning:** Use the method parameters `key, value`, not loop variables `k, v`

**Mistake 2: Display - Typo**
```python
for i, bucket in enumerate(self.tables):    # ❌ Plural
```
**Learning:** It's `self.table` (singular), not `self.tables`

---

## **Part 2: Word Frequency Counter Application**

### **Overview:**

Built a complete word frequency analysis tool using Hash Tables.

### **Implementation:**

**Class Structure:**
```python
class WordFrequencyCounter:
    def __init__(self):
        self.word_counts = HashTable(size=50)
```

**Methods Implemented:**

1. **`add_text(text)`** - Count words in text
   - Split text into words
   - Convert to lowercase
   - Get current count (or 0)
   - Increment and store

2. **`get_count(word)`** - Get count for specific word
   - Simple wrapper around hash table get

3. **`display_all()`** - Show all word counts
   - Display hash table contents

4. **`most_common()`** - Find most frequent word
   - Loop through all buckets
   - Track max count and word
   - Return tuple (word, count)

5. **`least_common()`** - Find least frequent word
   - Loop through all buckets
   - Track min count (start with infinity!)
   - Return tuple (word, count)

### **Challenges & Solutions:**

**Challenge 1: Initial Implementation Mistakes**

All methods had infinite recursion or wrong logic:
```python
def add_text(self, text):
    self.add_text(text)    # ❌ Calls itself forever!
```

**Solution:** Implement actual logic, not recursive calls

**Challenge 2: Most/Least Common**

Can't use `max()` or `min()` directly on HashTable:
```python
most = max(self.word_counts)    # ❌ Doesn't work
```

**Solution:** Loop through buckets manually:
```python
for bucket in self.word_counts.table:
    for word, count in bucket:
        if count > max_count:
            max_count = count
            max_word = word
```

**Challenge 3: Least Common Starting Value**

Started with 0, but no count is less than 0:
```python
least_count = 0    # ❌ Nothing will be less than 0
```

**Solution:** Start with infinity:
```python
least_count = float('inf')    # ✓ Any count will be less
```

### **Test Results:**

```
=== All Word Counts ===
Index 8: [('the', 6)]
Index 24: [('dog', 2)]
Index 34: [('cat', 3)]
Index 44: [('and', 3)]
... etc

=== Individual Word Counts ===
'the': 6
'cat': 3
'dog': 2
'bird': 1

=== Most Common Word ===
the: 6 times

=== Least Common Word ===
chased: 1 time(s)
```

**Perfect output!** ✓

### **Key Learning:**

Hash Tables provide O(1) lookup for word counting, making this extremely efficient even for large texts!

---

## **Part 3: Graphs - 7th and Final Data Structure!**

### **What is a Graph?**

A collection of **nodes (vertices)** connected by **edges (connections)**.

**Real-world examples:**
- Social networks (people → friendships)
- Maps (cities → roads)
- Websites (pages → links)
- Computer networks (devices → cables)

### **Graph vs Tree:**

**Tree:**
- Hierarchical (parent-child)
- One path between nodes
- No cycles
- Has root

**Graph:**
- Non-hierarchical (any connections)
- Multiple paths possible
- Can have cycles
- No root

### **Key Terminology Learned:**

**Nodes (Vertices):** The points in the graph

**Edges:** The connections between nodes
- **Mental model:** Connection, path, relationship, reference
- **NOT quite a pointer** (like in trees)
- **More like:** "A's list contains B" (reference by name)

**Neighbors:** Nodes directly connected

**Degree:** Number of edges on a node

**Path:** Sequence of edges

**Cycle:** Path that returns to start

### **Types of Graphs:**

**1. Directed vs Undirected**

**Undirected:** Edges go both ways
```
A --- B  (A ↔ B)
```

**Directed:** Edges have direction
```
A --> B  (A → B only)
```

**2. Weighted vs Unweighted**

**Unweighted:** All edges equal
```
A --- B  (just connected)
```

**Weighted:** Edges have values
```
A --5-- B  (distance, cost, time)
```

### **Graph Representation:**

**Adjacency List (what we used):**
```python
graph = {
    'A': ['B', 'C'],    # A connects to B and C
    'B': ['A', 'D'],    # B connects to A and D
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
```

**Why Adjacency List:**
- Space efficient: O(V + E)
- Fast to iterate neighbors
- Easy to add/remove edges

### **Implementation Built:**

**Methods Implemented:**

1. **`__init__()`** - Initialize empty graph
   ```python
   self.graph = {}  # Dictionary: node → list of neighbors
   ```

2. **`add_node(node)`** - Add a node
   ```python
   if node not in self.graph:
       self.graph[node] = []
   ```

3. **`add_edge(node1, node2)`** - Connect two nodes (undirected)
   ```python
   self.add_node(node1)
   self.add_node(node2)
   
   # Add edge both ways (undirected)
   if node2 not in self.graph[node1]:
       self.graph[node1].append(node2)
   if node1 not in self.graph[node2]:
       self.graph[node2].append(node1)
   ```

4. **`display()`** - Show all connections
   ```python
   for node, neighbours in self.graph.items():
       print(f"{node}: {neighbours}")
   ```

5. **`get_neighbour(node)`** - Get node's neighbors
   ```python
   return self.graph.get(node, [])
   ```

### **Test Results:**

```
=== Graph Structure ===
A: ['B', 'C']
B: ['A', 'D']
C: ['A', 'D']
D: ['B', 'C', 'E']
E: ['D']

=== Neighbors ===
A's neighbours: ['B', 'C']
D's neighbours: ['B', 'C', 'E']
E's neighbours: ['D']

=== Visual Representation ===
    A --- B
    |     |
    C --- D --- E
```

**Perfect! Matches the visual!** ✓

### **Conceptual Breakthroughs:**

**Breakthrough 1: Understanding Edges**

**Question:** Is an edge like a pointer?

**Answer:** Not quite! It's more like:
- ✅ A connection (shows relationship)
- ✅ A path (you can travel from A to B)
- ✅ A reference (A's list contains B's name)
- ❌ Not a direct pointer (like `node.left` in trees)

**Key insight:** Edge = Connection = Path = Reference

**Breakthrough 2: Naming Convention**

**Question:** Can I call it `add_connection` instead of `add_edge`?

**Answer:** You could, but "edge" is the industry standard!
- Everyone in CS uses "edge"
- All documentation uses "edge"
- Interviewers expect "edge"
- Graph theory term is "edge"

**Strategy:** Use `add_edge`, but think "connection" internally

**Breakthrough 3: Undirected Edges**

Understanding why we add edge both ways:
```python
# Add edge both ways (undirected)
self.graph[node1].append(node2)  # A → B
self.graph[node2].append(node1)  # B → A
```

This makes it undirected - connection goes both ways!

---

## **Part 4: New Warm-Up Routine Established**

### **The Problem Identified:**

**Self-assessment:** "I can write data structures, but struggle to USE them effectively"

**Example:** Word Frequency Counter - struggled with `most_common()`, `least_common()`

**Gap:** Implementation skills are strong, application skills need work

### **The Solution: 3-Part Gamified Warm-Up**

**Part 1: Build the Structure (10-15 min)**
- Random structure selection
- Write ALL methods from memory
- Goal: 2x correct per method (current practice)

**Part 2: Apply the Structure - GAMIFIED! (15-20 min)**
- 3-5 use-case functions
- **NEW: Each function must be correct TWICE** ⭕⭕
- Track progress with checkboxes
- Goal: Turn weakness into strength!

**Part 3: Test It (5-10 min)**
- Write test cases
- Run and verify
- Fix any bugs

**Total Time:** 35-45 minutes

### **Why This Works:**

✅ **Addresses weakness** - Focuses on application, not just implementation  
✅ **Spaced repetition** - Writing twice = better retention  
✅ **Builds muscle memory** - Common patterns become automatic  
✅ **Gamification** - Checkboxes are satisfying!  
✅ **Confidence building** - "I can do this perfectly twice!"  
✅ **Creates portfolio** - Mini-programs every day  

### **Example Practice Session (Done Today):**

**Structure:** Stack

**Part 1: Build** ✅
- Wrote complete Stack class
- Fixed 2 small issues (`__init__` parameter, `peek` safety check)

**Part 2: Apply** ✅
- `reverse_string(text)` - Use stack to reverse
- `balanced_parentheses(expr)` - Check if brackets balanced
- `undo_system()` - Demonstrate undo functionality

**Part 3: Test** ✅
- 15 test cases total
- All passed!

### **Detailed: Balanced Parentheses**

**Initial confusion:** Where does the matching happen?

**Walkthrough provided:**
```python
Expression: {[()]}

Stack changes:
{           → ['{']
{[          → ['{', '[']
{[(         → ['{', '[', '(']
{[()        → ['{', '[']      ← Matched '(' with ')'
{[()]       → ['{']           ← Matched '[' with ']'
{[()]}      → []              ← Matched '{' with '}'

Empty stack = Balanced! ✓
```

**Key line understood:**
```python
if pairs[opening] != char:
    return False
```

This is where matching happens!
- `opening` = bracket popped from stack
- `pairs[opening]` = what it should close with
- `char` = what we actually found
- If they don't match → not balanced!

**Breakthrough:** LIFO (Last In, First Out) naturally matches how brackets nest!

### **Test Results:**

```
TEST 1: Reverse String
'hello' → 'olleh' ✓
'Python' → 'nohtyP' ✓
'12345' → '54321' ✓

TEST 2: Balanced Parentheses
'(hello)' → True ✓
'(hello]' → False ✓
'{[()]}' → True ✓
'((hello)' → False ✓
'hello)' → False ✓

TEST 3: Undo System
Actions performed → Showed all 3 ✓
Undo last action → Removed last ✓
Remaining actions → Showed remaining ✓
```

**All 15 tests passed!** 🎉

---

## **Skills Reinforced:**

### **Technical Skills:**
✅ **Hash Table mastery** - All 6 methods from memory  
✅ **Graph implementation** - Basic graph from scratch  
✅ **Application development** - Word Frequency Counter  
✅ **Stack applications** - 3 real-world use cases  
✅ **Algorithm implementation** - Balanced parentheses  
✅ **Testing** - Comprehensive test cases  
✅ **Debugging** - Fixed issues independently  

### **Problem-Solving Skills:**
✅ **Self-assessment** - Identified weakness (application skills)  
✅ **Solution design** - Created gamified practice system  
✅ **Pattern recognition** - LIFO matches bracket nesting  
✅ **Breaking down problems** - Step-by-step walkthroughs  
✅ **Testing strategy** - Multiple test cases per function  

### **Learning Skills:**
✅ **Asking questions** - "Is edge like a pointer?"  
✅ **Seeking clarification** - "Walk me through balanced_parentheses"  
✅ **Building mental models** - Edge = connection/path/reference  
✅ **Adapting strategy** - New warm-up routine for weakness  
✅ **Gamification** - Making practice engaging  

---

## **Statistics:**

- **Time spent:** ~6-7 hours
- **Typing practice:** 29.2 WPM, 95.2% accuracy
- **Warm-up exercises:** 5
- **Hash Table exercises:** 12 (all methods 2x)
- **Hash Table application:** 1 (Word Frequency Counter)
- **Graph methods:** 5
- **Stack applications:** 3
- **Test cases written:** 15
- **All tests passed:** 15/15 ✓
- **Lines of code:** ~250+
- **Data structures mastered:** 7/7 complete!

---

## **Key Achievements:**

🏆 Hash Tables mastered (all 6 methods)  
🏆 Word Frequency Counter built  
🏆 Graphs learned (7th and final structure!)  
🏆 Basic Graph implemented  
🏆 New warm-up routine established  
🏆 Stack applications practiced (3 functions)  
🏆 All 15 tests passed  
🏆 **ALL 7 DATA STRUCTURES COMPLETE!** 🎊  

---

## **Key Insights:**

### **On Hash Tables:**
- O(1) lookup makes word counting extremely efficient
- Looping through buckets manually for aggregations
- Start with `float('inf')` for minimum finding
- Perfect for frequency analysis

### **On Graphs:**
- Most flexible data structure
- Edges are connections/paths/references (not quite pointers)
- Adjacency list is space-efficient
- Undirected = add edge both ways
- Industry standard terminology matters ("edge" not "connection")

### **On Stack Applications:**
- LIFO naturally matches bracket nesting
- Perfect for undo systems
- Can reverse sequences
- Matching problems (parentheses, tags, etc.)

### **On Learning:**
- Identifying weaknesses is crucial
- Application skills different from implementation skills
- Gamification makes practice engaging
- Writing twice builds mastery
- Step-by-step walkthroughs clarify confusion

### **On New Warm-Up Routine:**
- 3-part system addresses all aspects
- Part 2 (Apply) is the weakness to strengthen
- Gamification with checkboxes motivates
- 35-45 minutes is sustainable
- Creates portfolio of mini-programs

---

## **Challenges Faced:**

1. **Typing off day**
   - 29.2 WPM (down from 35.7)
   - Normal variation, not a concern
   - Still maintaining accuracy

2. **Hash Table insert - wrong variables**
   - Used loop variables instead of parameters
   - Fixed: Use `key, value` not `k, v`

3. **Word Frequency Counter - initial mistakes**
   - Infinite recursion in methods
   - Fixed: Implement actual logic

4. **Most/least common - can't use max/min**
   - Can't use built-in functions on HashTable
   - Fixed: Loop through buckets manually

5. **Least common - wrong starting value**
   - Started with 0 (nothing less than 0)
   - Fixed: Start with `float('inf')`

6. **Understanding edges**
   - Confused about pointer vs reference
   - Clarified: Connection/path/reference, not pointer

7. **Balanced parentheses - where's the match?**
   - Didn't see where matching happened
   - Clarified: `pairs[opening] != char` line

**All challenges overcome through questions and clarification!**

---

## **Roadmap Status:**

**AHEAD OF SCHEDULE!** 🚀

- **Current:** Day 21 (Oct 29)
- **Original plan:** Should be finishing Week 1-2 (Fundamentals)
- **Actual progress:** Week 5-6 (Data Structures) - **ALL 7 COMPLETE!**
- **Ahead by:** ~2-3 weeks

**Data Structures Progress:**
1. ✅ Stacks (Day 13) - MASTERED
2. ✅ Queues (Day 13) - MASTERED
3. ✅ Singly Linked Lists (Day 14) - MASTERED
4. ✅ Doubly Linked Lists (Day 14) - MASTERED
5. ✅ Binary Search Trees (Day 16) - MASTERED
6. ✅ Hash Tables (Day 20-21) - MASTERED
7. ✅ Graphs (Day 21) - **LEARNED TODAY!**

**ALL 7 DATA STRUCTURES COMPLETE!** 🎊

---

## **Tomorrow's Goals (Day 22 - Oct 30):**

**Morning:**
- Typing practice
- **NEW 3-Part Warm-Up!**
  - Part 1: Build random structure (all methods 2x)
  - Part 2: Apply (3-5 use cases, each 2x) - GAMIFIED!
  - Part 3: Test (verify everything works)

**Main Session:**
- Graph practice (BFS, DFS, pathfinding)
- Or start algorithms (sorting, searching)
- Or build comprehensive project using multiple structures

**Goal:** Continue building application skills with new warm-up routine!

---

## **Reflections:**

Today was transformative! Completing all 7 data structures is a huge milestone. But more importantly, I identified a critical weakness: I can implement structures but struggle to apply them effectively.

The Word Frequency Counter exposed this gap. I could write the HashTable class perfectly, but struggled with `most_common()` and `least_common()`. This isn't about not knowing the structure - it's about not knowing the common patterns for using it.

Creating the new 3-part warm-up routine addresses this directly. Part 2 (Apply) will now be gamified - each use-case function must be correct twice. This builds muscle memory for application patterns, not just implementation patterns.

The Stack practice session validated this approach. After implementing `reverse_string()`, `balanced_parentheses()`, and `undo_system()`, I now have 3 real patterns for using stacks. Writing these twice would cement them even more.

Learning Graphs was exciting - it's the most flexible structure. The conceptual breakthrough about edges being "connections/paths/references" rather than pointers helped me understand the difference from trees. The adjacency list representation makes sense - it's just a dictionary of neighbors.

The balanced parentheses walkthrough was valuable. I understood the concept but couldn't see where the matching happened. The step-by-step visualization showed how LIFO naturally matches bracket nesting. This kind of detailed walkthrough helps build deep understanding.

Completing all 7 data structures feels incredible, but I know the real work is ahead: mastering their application. The new warm-up routine will build this skill systematically, one structure at a time, with gamified repetition.

Ready to start the new routine tomorrow and turn application skills from weakness to strength!

---

## **Personal Notes:**

- Typing: 29.2 WPM (off day, normal variation)
- All 7 data structures complete! 🎊
- New warm-up routine designed
- Application skills identified as weakness
- Gamification strategy for improvement
- Stack applications practiced
- Graphs make sense now
- Edge = connection/path/reference
- Ready for new routine tomorrow
- Feeling accomplished!

---

## **Resources Used:**

- Hash Tables "Wax On Wax Off" (12 exercises)
- Word Frequency Counter project
- Graphs theory and examples
- Step-by-step walkthroughs
- Stack application practice
- Comprehensive testing
- Self-assessment and strategy design

---

## **Next Session Preview:**

- New 3-part warm-up routine (first time!)
- Random structure selection
- Gamified application practice (2x each)
- Continue building application skills

---

**Total Days Completed:** 21/60 (Phase 1)  
**Progress:** Ahead of schedule ✓  
**Confidence Level:** Very High 💪  
**Data Structures:** 7/7 COMPLETE! 🎊  
**Application Skills:** Improving with new routine ✓  
**New Warm-Up:** Ready to start ✓  

---

End of Day 21 Summary
```

---

**Excellent day! All 7 data structures complete!** 🎉 Ready to commit? 🚀
