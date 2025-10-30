
---

```markdown
# Day 22 Summary - Graph Algorithms & Lists/Dictionaries Refresher

---

## **Date:** October 30, 2025 (Thursday)

---

## **Main Achievements:**

1. **Typing Progress** - 31.4 WPM (bounce back from yesterday!)
2. **New 3-Part Warm-Up** - Queue edition complete
3. **Graph Algorithms Mastered** - BFS, DFS, path finding
4. **Deep Understanding** - Step-by-step walkthroughs
5. **Lists & Dictionaries Refresher** - Fundamentals reinforced

---

## **Morning Session: Typing & Warm-Up**

### **Typing Practice:**
- **Speed:** 31.4 WPM
- **Accuracy:** 95.99%
- **Status:** Bounce back from yesterday's 29.2 WPM

### **Analysis:**
- Back to average (31-32 WPM range)
- Normal variation - yesterday was just an off day
- Consistency is more important than daily peaks
- Still maintaining 95%+ accuracy

---

### **3-Part Warm-Up: Queue Edition**

**NEW ROUTINE - First Full Implementation!**

#### **Part 1: Build the Structure (10-15 min)**

**Task:** Write complete Queue class from memory

**Methods Implemented:**
1. `__init__()`
2. `enqueue(item)`
3. `dequeue()`
4. `peek()`
5. `is_empty()`

**Mistakes Made:**
1. Used `self.items.is_empty()` instead of `self.is_empty()` - Lists don't have is_empty() method!
2. Used `self.items.__len__()` instead of `len(self.items)` - Don't use dunder methods directly
3. Fixed both issues and completed successfully

**Result:** Queue class complete ✓

---

#### **Part 2: Apply - GAMIFIED! (15-20 min)**

**Task:** Implement 3 use-case functions, each correct TWICE ⭕⭕

**Function 1: `hot_potato(names, num)` ⭕⭕**

Classic elimination game using Queue.

**How it works:**
1. Put all names in queue
2. Pass potato `num` times (dequeue and enqueue back)
3. After `num` passes, eliminate person (dequeue, don't enqueue)
4. Repeat until one person left

**Mistakes:**
- Round 1: Used `self` parameter (these are standalone functions, not class methods!)
- Round 2: Perfect! ✓

**Result:** MASTERED ✓✓

---

**Function 2: `task_scheduler(tasks)` ⭕⭕**

Process tasks in FIFO order.

**How it works:**
1. Add all tasks to queue
2. Process each task in order (dequeue)
3. Print processing status

**Mistakes:**
- Round 1: Used `self` parameter, typo "schedular" instead of "scheduler"
- Round 2: Perfect! ✓

**Result:** MASTERED ✓✓

---

**Function 3: `print_queue_simulation()` ⭕⭕**

Simulate printer queue.

**How it works:**
1. Add print jobs to queue
2. Process each job in order
3. Display queue status

**Mistakes:**
- Round 1: Used `self` parameter, had unused `jobs` parameter
- Round 2: Perfect! ✓

**Result:** MASTERED ✓✓

---

#### **Part 3: Test It (5-10 min)**

**Test Results:**

```
TEST 1: Hot Potato
David, Charlie, Eve, Bob eliminated
Winner: Alice ✓

TEST 2: Task Scheduler
All 4 tasks processed in FIFO order ✓
Compile → Run → Deploy → Send

TEST 3: Print Queue
3 jobs added, 3 jobs printed in order ✓
Sonic.jpg → CV.docx → world_history.pdf
```

**All 15 test cases passed!** ✓

---

### **3-Part Warm-Up Assessment:**

**What Worked:**
✅ Build phase reinforced implementation  
✅ Apply phase (2x each) built mastery  
✅ Test phase verified everything works  
✅ Created complete mini-program  
✅ Gamification (checkboxes) was motivating  

**What to Improve:**
- Remember: Use-case functions are standalone, not class methods (no `self`)
- Double-check function signatures before implementing

**Overall:** New routine is working perfectly! This addresses the application skills weakness identified on Day 21.

---

## **Main Session: Graph Algorithms**

### **Overview:**

Learned and implemented the two fundamental graph traversal algorithms plus practical path-finding functions.

---

### **BFS (Breadth-First Search)**

#### **Concept:**

**"Breadth" = Width** - Explore level by level, like ripples in water.

**Key insight:** The name tells you the exploration pattern!

#### **How it works:**
1. Start at a node
2. Visit all neighbors (level 1)
3. Then visit their neighbors (level 2)
4. Continue until all visited

**Data Structure:** Queue (FIFO)

#### **Implementation:**

```python
def bfs(self, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

#### **Step-by-Step Walkthrough:**

**Graph:**
```
    A --- B
    |     |
    C --- D --- E
```

**BFS from A:**

**Iteration 1:**
- Process A
- Add B, C to queue
- visited: `{'A', 'B', 'C'}`
- queue: `['B', 'C']`
- result: `['A']`

**Iteration 2:**
- Process B
- Add D to queue
- visited: `{'A', 'B', 'C', 'D'}`
- queue: `['C', 'D']`
- result: `['A', 'B']`

**Iteration 3:**
- Process C
- All neighbors already visited
- queue: `['D']`
- result: `['A', 'B', 'C']`

**Iteration 4:**
- Process D
- Add E to queue
- visited: `{'A', 'B', 'C', 'D', 'E'}`
- queue: `['E']`
- result: `['A', 'B', 'C', 'D']`

**Iteration 5:**
- Process E
- All neighbors already visited
- queue: `[]` (empty - done!)
- result: `['A', 'B', 'C', 'D', 'E']`

**Final Order:** A → B → C → D → E (level by level!)

#### **Key Points:**

1. **Queue ensures level-by-level:**
   - FIFO means we process all level N before level N+1

2. **Mark visited when adding to queue:**
   - Prevents duplicates in queue
   - More efficient than marking when processing

3. **Why mark when adding?**
   - If we marked when processing, nodes could be added to queue multiple times
   - By marking when adding, we ensure each node is queued only once

#### **When to Use BFS:**

✅ Finding shortest path (unweighted)  
✅ Finding closest nodes  
✅ Level-order traversal  
✅ When solution is likely close to start  
✅ Social networks (degrees of separation)  

---

### **DFS (Depth-First Search)**

#### **Concept:**

**"Depth" = Deep** - Go as deep as possible, then backtrack.

**Key insight:** Like exploring a maze - follow one path to the end, then try another!

#### **How it works:**
1. Start at a node
2. Go as deep as possible down one path
3. When stuck, backtrack
4. Try another path
5. Continue until all visited

**Data Structure:** Recursion (uses call stack)

#### **Implementation:**

```python
def dfs(self, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in self.graph[start]:
        if neighbor not in visited:
            result.extend(self.dfs(neighbor, visited))
    
    return result
```

#### **Step-by-Step Walkthrough:**

**Graph:**
```
    A --- B
    |     |
    C --- D --- E
```

**DFS from A:**

**Call 1: dfs('A')**
- visited: `{'A'}`
- result: `['A']`
- Recurse on B (first neighbor)

**Call 2: dfs('B')**
- visited: `{'A', 'B'}`
- result: `['B']`
- Recurse on D

**Call 3: dfs('D')**
- visited: `{'A', 'B', 'D'}`
- result: `['D']`
- Recurse on C

**Call 4: dfs('C')**
- visited: `{'A', 'B', 'D', 'C'}`
- result: `['C']`
- All neighbors visited
- Return `['C']` to dfs('D')

**Back to Call 3:**
- result: `['D', 'C']`
- Recurse on E

**Call 5: dfs('E')**
- visited: `{'A', 'B', 'D', 'C', 'E'}`
- result: `['E']`
- Return `['E']` to dfs('D')

**Back to Call 3:**
- result: `['D', 'C', 'E']`
- Return to dfs('B')

**Back to Call 2:**
- result: `['B', 'D', 'C', 'E']`
- Return to dfs('A')

**Back to Call 1:**
- result: `['A', 'B', 'D', 'C', 'E']`
- Done!

**Final Order:** A → B → D → C → E (deep first!)

#### **Key Points:**

1. **Recursion handles backtracking automatically:**
   - Call stack tracks where to return
   - No need to manually manage backtracking

2. **Visited set is shared:**
   - Same set used by all recursive calls
   - Prevents infinite loops

3. **Explores one complete path first:**
   - Goes as deep as possible
   - Then backtracks to try alternatives

#### **When to Use DFS:**

✅ Exploring all paths  
✅ Detecting cycles  
✅ Topological sorting  
✅ When solution is likely far from start  
✅ Maze solving  
✅ File system traversal  

---

### **BFS vs DFS Comparison:**

#### **Exploration Pattern:**

**BFS:** A → B, C → D → E (level by level)  
**DFS:** A → B → D → C → E (deep first)

#### **Data Structure:**

**BFS:** Queue (FIFO - First In, First Out)  
**DFS:** Recursion/Stack (LIFO - Last In, First Out)

#### **Memory Usage:**

**BFS:**
- Stores entire level in queue
- Wide graphs = lots of memory

**DFS:**
- Stores only current path in call stack
- Deep graphs = lots of memory

#### **Key Insight:**

**Size doesn't matter - shape does!**

- **Wide graph** (many neighbors) → DFS better for memory
- **Deep graph** (long chains) → BFS better for memory

#### **Use Cases:**

| Need | Use |
|------|-----|
| Shortest path | BFS |
| Any path | DFS |
| All paths | DFS |
| Closest nodes | BFS |
| Cycle detection | DFS |
| Level-order | BFS |

---

### **Path Finding Functions**

#### **find_path() - Any Path (DFS)**

Find **any** path from start to end.

**Implementation:**
```python
def find_path(self, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path
    
    if start not in self.graph:
        return None
    
    for neighbor in self.graph[start]:
        if neighbor not in path:
            newpath = self.find_path(neighbor, end, path)
            if newpath:
                return newpath
    
    return None
```

**How it works:**
1. Add current node to path
2. If reached end, return path
3. Try each neighbor recursively
4. If any neighbor finds path, return it
5. If no path found, return None

**Key feature:** Returns first path found (may not be shortest)

---

#### **shortest_path() - Shortest Path (BFS)**

Find **shortest** path from start to end.

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
        
        for neighbor in self.graph[node]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

**How it works:**
1. Store (node, path) tuples in queue
2. Process nodes level by level
3. When we reach end, return the path
4. First path found = shortest (BFS guarantee!)

**Key feature:** Guaranteed shortest path

---

#### **Test Results:**

**Graph:**
```
    A --- B
    |     |
    C --- D --- E
    |           |
    F -----------
```

**find_path('A', 'E'):**
- Result: `A → B → D → C → F → E` (6 nodes)
- Went deep first, explored one complete path

**shortest_path('A', 'E'):**
- Result: `A → B → D → E` (4 nodes)
- Level by level, found shortest

**BFS found 33% shorter path!** 🎯

---

### **Conceptual Breakthroughs:**

#### **Breakthrough 1: Names Describe Patterns**

**Question:** Why "breadth" and "depth"?

**Answer:** The names literally describe the exploration pattern!
- **Breadth** = Width = Explore wide (all neighbors at level)
- **Depth** = Deep = Explore deep (one path completely)

**This insight made everything click!**

#### **Breakthrough 2: Size vs Shape**

**Initial thought:** BFS for small graphs, DFS for large?

**Clarification:** It's not about size, it's about:
- What you're looking for (shortest vs any path)
- Where solution likely is (close vs far)
- Graph shape (wide vs deep)
- Memory constraints

**Key insight:** Choose based on problem, not graph size!

#### **Breakthrough 3: Queue = Level by Level**

**Understanding:** FIFO (First In, First Out) naturally creates level-by-level exploration
- Add all level 1 nodes before processing them
- Add all level 2 nodes before processing them
- First time we reach a node = shortest path!

#### **Breakthrough 4: Recursion = Automatic Backtracking**

**Understanding:** The call stack handles backtracking automatically
- Go deep (recursive calls)
- Backtrack (returning from calls)
- Try all paths (loop through neighbors)

**No need to manually manage backtracking!**

---

## **Lists & Dictionaries Refresher**

### **Why This Session:**

**Self-assessment:** "I'm forgetting how to loop through or extract from them, especially nested dictionaries"

**Reason:** When focused on data structures, fundamentals can get rusty

**Solution:** Comprehensive refresher with practice exercises

---

### **Lists Review:**

#### **Looping:**

**Method 1: Simple for loop**
```python
for fruit in fruits:
    print(fruit)
```

**Method 2: With index (enumerate)**
```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

**Method 3: While loop**
```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

#### **Nested Lists:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access
element = matrix[0][1]  # 2

# Loop
for row in matrix:
    for num in row:
        print(num, end=" ")
```

---

### **Dictionaries Review:**

#### **Looping:**

**Method 1: Keys (default)**
```python
for key in dict:
    print(key)
```

**Method 2: Values**
```python
for value in dict.values():
    print(value)
```

**Method 3: Key-value pairs (MOST COMMON!)**
```python
for key, value in dict.items():
    print(f"{key}: {value}")
```

#### **Safe Access:**

```python
# Direct access (can crash!)
name = person["name"]

# Safe access with .get()
name = person.get("name", "Unknown")  # Default if missing
```

**Key learning:** Always use `.get()` with defaults for safety!

#### **Nested Dictionaries:**

```python
users = {
    "user1": {
        "name": "Alice",
        "hobbies": ["reading", "coding"]
    }
}

# Access
name = users["user1"]["name"]
hobby = users["user1"]["hobbies"][0]

# Safe access
name = users.get("user1", {}).get("name")
```

---

### **Practice Exercises:**

**Exercise 1: List with enumerate** ✓
- Looped through fruits with index
- Used `enumerate()` correctly

**Exercise 2: Nested list** ✓
- Looped through 2D matrix
- Printed all numbers in single line

**Exercise 3: Dictionary .items()** ✓
- Looped through key-value pairs
- Used `.items()` correctly

**Exercise 4: Safe dictionary access** ✓
- Used `.get()` with defaults
- **Mistake:** Initially forgot to add default values
- **Learning:** Always provide defaults, even for keys that exist!

**Exercise 5: Nested dictionary** ✓
- Accessed nested values
- Looped through nested structure
- **Mistake:** Used index 0 instead of 1 for "second" hobby
- **Learning:** Index 0 = first, Index 1 = second!

---

### **Key Takeaways:**

**Lists:**
```python
for i, item in enumerate(list):    # Loop with index
for row in matrix:                  # Nested loop
    for item in row:
```

**Dictionaries:**
```python
for key, value in dict.items():    # Loop through pairs
value = dict.get(key, default)     # Safe access
nested = dict[key1][key2]          # Nested access
```

**Nested Dictionaries:**
```python
# Access pattern
users["user1"]["name"]
users["user1"]["hobbies"][0]

# Loop pattern
for user_id, user_data in users.items():
    name = user_data["name"]
```

---

## **Skills Reinforced:**

### **Technical Skills:**
✅ **Queue implementation** - From memory  
✅ **Queue applications** - 3 real-world use cases  
✅ **BFS algorithm** - Level-by-level traversal  
✅ **DFS algorithm** - Deep-first traversal  
✅ **Path finding** - Any path and shortest path  
✅ **List operations** - Looping, enumerate, nested  
✅ **Dictionary operations** - .items(), .get(), nested  

### **Problem-Solving Skills:**
✅ **Pattern recognition** - Names describe algorithms  
✅ **Algorithm selection** - BFS vs DFS based on problem  
✅ **Debugging** - Fixed self parameter issues  
✅ **Safe coding** - Using .get() with defaults  

### **Learning Skills:**
✅ **Asking for clarification** - Requested walkthroughs  
✅ **Deep understanding** - Step-by-step analysis  
✅ **Identifying gaps** - Recognized need for refresher  
✅ **Practice** - Completed exercises to reinforce  

---

## **Statistics:**

- **Time spent:** ~6-7 hours
- **Typing practice:** 31.4 WPM, 95.99% accuracy
- **Warm-up exercises:** 5 (Queue class + 3 applications)
- **Graph algorithms:** 4 (BFS, DFS, find_path, shortest_path)
- **Practice exercises:** 5 (lists and dictionaries)
- **Walkthroughs requested:** 3 (BFS, DFS, path finding)
- **Lines of code:** ~200+
- **Test cases passed:** 15/15 ✓

---

## **Key Achievements:**

🏆 New 3-part warm-up routine working perfectly  
🏆 Queue applications mastered (3 functions, 2x each)  
🏆 BFS algorithm implemented and understood  
🏆 DFS algorithm implemented and understood  
🏆 Path finding functions working correctly  
🏆 Deep understanding through walkthroughs  
🏆 Lists & dictionaries refreshed  
🏆 All practice exercises completed  

---

## **Key Insights:**

### **On New Warm-Up Routine:**
- Build + Apply + Test = Complete mastery
- Gamification (2x each) is motivating
- Creates complete mini-programs daily
- Addresses application skills weakness
- Takes 35-45 minutes (sustainable)

### **On Graph Algorithms:**
- Names literally describe the pattern (breadth vs depth)
- Choose based on problem, not graph size
- BFS = shortest path, DFS = any path
- Queue creates level-by-level (FIFO)
- Recursion handles backtracking (call stack)

### **On Understanding:**
- Step-by-step walkthroughs build deep understanding
- Asking "why" leads to insights
- Visual models help grasp concepts
- Connecting to familiar concepts (ripples, maze) helps

### **On Fundamentals:**
- Need periodic refreshers when focused on advanced topics
- Practice exercises reinforce patterns
- Safe coding practices (`.get()` with defaults) prevent bugs
- Fundamentals are foundation for everything else

---

## **Challenges Faced:**

1. **Queue warm-up - self parameter**
   - Used `self` in standalone functions
   - Fixed: These are functions that USE Queue, not methods OF Queue
   - Learning: Check function signatures carefully

2. **BFS/DFS understanding**
   - Needed step-by-step walkthroughs
   - Solution: Detailed iteration-by-iteration analysis
   - Learning: Deep understanding > surface memorization

3. **Dictionary .get() defaults**
   - Forgot to add default values
   - Fixed: Always provide defaults for safety
   - Learning: Good practice even when key exists

4. **List indexing**
   - Used index 0 for "second" item
   - Fixed: Index 0 = first, Index 1 = second
   - Learning: Off-by-one errors are common

**All challenges overcome through practice and clarification!**

---

## **Roadmap Status:**

**AHEAD OF SCHEDULE!** 🚀

- **Current:** Day 22 (Oct 30)
- **Original plan:** Should be in Week 3-4 (OOP)
- **Actual progress:** Week 5-6 (Data Structures + Algorithms)
- **Ahead by:** ~3 weeks

**Data Structures Progress:**
1. ✅ Stacks - MASTERED
2. ✅ Queues - MASTERED (reinforced today!)
3. ✅ Singly Linked Lists - MASTERED
4. ✅ Doubly Linked Lists - MASTERED
5. ✅ Binary Search Trees - MASTERED
6. ✅ Hash Tables - MASTERED
7. ✅ Graphs - **Algorithms learned today!**

**ALL 7 DATA STRUCTURES COMPLETE + Graph Algorithms!** 🎊

---

## **Tomorrow's Goals (Day 23 - Oct 31):**

**Morning:**
- Typing practice
- **3-Part Warm-Up** - Random structure (maybe Hash Table or BST)
  - Part 1: Build all methods
  - Part 2: 3-5 use cases (2x each)
  - Part 3: Test everything

**Main Session:**
- Start Sorting Algorithms
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
- Understand time complexity
- Implement and test

**Goal:** Begin algorithms phase with sorting!

---

## **Reflections:**

Today was incredibly productive! The new 3-part warm-up routine proved its worth. Building the Queue class, then implementing 3 real-world applications (each twice!), and finally testing everything created a complete learning experience. This directly addresses the application skills weakness I identified on Day 21.

The graph algorithms session was enlightening. The key breakthrough was realizing that "breadth" and "depth" literally describe the exploration patterns. BFS explores wide (all neighbors at each level) while DFS explores deep (one complete path). This simple insight made everything click.

The step-by-step walkthroughs were invaluable. Seeing BFS iterate through the queue, adding nodes level by level, made the algorithm concrete. Similarly, watching DFS's call stack grow and shrink as it recursed and backtracked showed exactly how the algorithm works. These detailed walkthroughs build deep understanding that surface-level explanations can't provide.

The path-finding functions demonstrated the practical difference between BFS and DFS. On the same graph, DFS found a 6-node path while BFS found a 4-node path - 33% shorter! This concrete example shows why algorithm choice matters.

The lists and dictionaries refresher was necessary and helpful. When focused on advanced data structures, it's easy to get rusty on fundamentals. The practice exercises reinforced key patterns: using `enumerate()` for lists, `.items()` for dictionaries, and `.get()` with defaults for safety. The nested dictionary exercises were particularly valuable since that's where I was struggling.

The new warm-up routine is working exactly as intended. It builds implementation speed (Part 1), application skills (Part 2), and verification habits (Part 3). The gamification of requiring 2 correct attempts per function is motivating and ensures mastery. Tomorrow I'll continue this routine with a different structure.

Ready to start sorting algorithms tomorrow and continue building on this solid foundation!

---

## **Personal Notes:**

- Typing: 31.4 WPM (back to average)
- New warm-up routine working perfectly
- Graph algorithms make sense now
- "Breadth" and "depth" describe patterns
- BFS for shortest, DFS for any path
- Fundamentals need periodic refreshers
- Step-by-step walkthroughs are invaluable
- Feeling confident and ready for algorithms!

---

## **Resources Used:**

- New 3-part warm-up routine
- Queue implementation and applications
- Graph algorithm theory and examples
- Step-by-step BFS walkthrough
- Step-by-step DFS walkthrough
- Path finding implementations
- Lists and dictionaries refresher
- Practice exercises

---

## **Next Session Preview:**

- Random structure warm-up (3-part)
- Start sorting algorithms
- Bubble, Selection, Insertion sorts
- Time complexity analysis

---

**Total Days Completed:** 22/60 (Phase 1)  
**Progress:** Ahead of schedule ✓  
**Confidence Level:** Very High 💪  
**Data Structures:** 7/7 complete + algorithms!  
**New Warm-Up:** Working perfectly ✓  
**Application Skills:** Improving daily ✓  

---

End of Day 22 Summary
```

---
