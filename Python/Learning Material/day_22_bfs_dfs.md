
---

```markdown
# Day 22: Graph Algorithms & Lists/Dictionaries Refresher

## Date: October 30, 2025 (Thursday)

---

## PART 1: GRAPH TRAVERSAL ALGORITHMS

### Overview

Graph traversal algorithms are methods for visiting all nodes in a graph systematically. The two fundamental algorithms are:

1. **BFS (Breadth-First Search)** - Explore level by level
2. **DFS (Depth-First Search)** - Explore as deep as possible first

---

## BFS (Breadth-First Search)

### Concept

**"Breadth" = Width**

Explores the graph **level by level**, like ripples spreading in water.

**Visual:**
```
Level 0:     A
Level 1:   B   C
Level 2:  D E F G
```

Visits all nodes at level N before visiting any node at level N+1.

---

### How BFS Works

1. Start at a node
2. Visit all its neighbors (level 1)
3. Then visit their neighbors (level 2)
4. Continue until all nodes visited

**Key Data Structure:** Queue (FIFO - First In, First Out)

---

### Implementation

```python
from collections import deque

def bfs(self, start):
    """Breadth-first search"""
    visited = set()           # Track visited nodes
    queue = deque([start])    # Queue for BFS
    visited.add(start)
    result = []               # Order of visits
    
    while queue:
        node = queue.popleft()    # Get front of queue
        result.append(node)
        
        # Visit all unvisited neighbors
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

---

### Step-by-Step Example

**Graph:**
```
    A --- B
    |     |
    C --- D --- E
```

**BFS from A:**

**Setup:**
- visited: `{'A'}`
- queue: `['A']`
- result: `[]`

**Iteration 1:**
- Process A
- Add neighbors B, C to queue
- visited: `{'A', 'B', 'C'}`
- queue: `['B', 'C']`
- result: `['A']`

**Iteration 2:**
- Process B
- Add neighbor D to queue
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
- Add neighbor E to queue
- visited: `{'A', 'B', 'C', 'D', 'E'}`
- queue: `['E']`
- result: `['A', 'B', 'C', 'D']`

**Iteration 5:**
- Process E
- All neighbors already visited
- queue: `[]` (empty - done!)
- result: `['A', 'B', 'C', 'D', 'E']`

**Final Order:** A → B → C → D → E (level by level!)

---

### Key Points

1. **Queue ensures level-by-level exploration**
   - FIFO means we process all level N before level N+1

2. **Mark visited when adding to queue**
   - Prevents duplicates in queue
   - More efficient than marking when processing

3. **Guarantees shortest path (unweighted graphs)**
   - First time we reach a node = shortest path to it

---

### Time & Space Complexity

- **Time:** O(V + E) where V = vertices, E = edges
- **Space:** O(V) for visited set and queue

---

### When to Use BFS

✅ Finding **shortest path** (unweighted graphs)  
✅ Finding **closest** nodes  
✅ **Level-order** traversal  
✅ When solution is likely **close to start**  
✅ Social networks (degrees of separation)  
✅ Web crawling  

---

## DFS (Depth-First Search)

### Concept

**"Depth" = Deep**

Explores the graph by going **as deep as possible** before backtracking.

**Visual:**
```
A
↓
B (go deep)
↓
D (keep going)
↓
E (as far as possible)
↓
(backtrack and try other paths)
```

---

### How DFS Works

1. Start at a node
2. Go as deep as possible down one path
3. When stuck, backtrack
4. Try another path
5. Continue until all nodes visited

**Key Data Structure:** Recursion (uses call stack) or explicit Stack

---

### Implementation (Recursive)

```python
def dfs(self, start, visited=None):
    """Depth-first search (recursive)"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    # Visit each unvisited neighbor
    for neighbor in self.graph[start]:
        if neighbor not in visited:
            result.extend(self.dfs(neighbor, visited))
    
    return result
```

---

### Step-by-Step Example

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
- Neighbors: B, C
- Recurse on B (first neighbor)

**Call 2: dfs('B')**
- visited: `{'A', 'B'}`
- result: `['B']`
- Neighbors: A (visited), D
- Recurse on D

**Call 3: dfs('D')**
- visited: `{'A', 'B', 'D'}`
- result: `['D']`
- Neighbors: B (visited), C, E
- Recurse on C

**Call 4: dfs('C')**
- visited: `{'A', 'B', 'D', 'C'}`
- result: `['C']`
- Neighbors: A (visited), D (visited)
- No more recursion
- Return `['C']` to dfs('D')

**Back to Call 3:**
- result: `['D', 'C']`
- Continue with E
- Recurse on E

**Call 5: dfs('E')**
- visited: `{'A', 'B', 'D', 'C', 'E'}`
- result: `['E']`
- Neighbors: D (visited)
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

---

### Key Points

1. **Recursion handles backtracking automatically**
   - Call stack tracks where to return
   - No need to manually manage backtracking

2. **Visited set is shared across all calls**
   - Prevents infinite loops
   - All recursive calls see same visited set

3. **Explores one complete path before trying others**
   - Goes as deep as possible
   - Then backtracks to try alternatives

---

### Time & Space Complexity

- **Time:** O(V + E) where V = vertices, E = edges
- **Space:** O(V) for visited set + O(h) for call stack (h = height)

---

### When to Use DFS

✅ Exploring **all paths**  
✅ Detecting **cycles**  
✅ **Topological sorting**  
✅ When solution is likely **far from start**  
✅ Maze solving  
✅ File system traversal  
✅ Decision trees  

---

## BFS vs DFS Comparison

### Exploration Pattern

**BFS (Breadth):**
```
A → B, C → D, E → F, G
(All of level 1, then all of level 2, etc.)
```

**DFS (Depth):**
```
A → B → D → F (deep) → backtrack → E → G
(One path completely, then try others)
```

---

### Data Structure

| Algorithm | Data Structure | Order |
|-----------|---------------|-------|
| BFS | Queue | FIFO (First In, First Out) |
| DFS | Recursion/Stack | LIFO (Last In, First Out) |

---

### Memory Usage

**BFS:**
- Stores entire level in queue
- **Wide graphs** = lots of memory
- Example: Social network (100 friends each)
  - Level 1: 100 nodes
  - Level 2: 10,000 nodes!

**DFS:**
- Stores only current path in call stack
- **Deep graphs** = lots of memory
- Example: Linked list (1 → 2 → ... → 1000)
  - Call stack depth: 1000

---

### Use Cases

| Need | Use |
|------|-----|
| Shortest path (unweighted) | BFS |
| Any path | DFS |
| All paths | DFS |
| Closest nodes | BFS |
| Cycle detection | DFS |
| Level-order | BFS |
| Topological sort | DFS |

---

### Graph Shape Matters

**Wide Graph (many neighbors):**
```
        A
    /   |   \
   B    C    D
  /|\  /|\  /|\
```
- BFS queue gets huge
- DFS better for memory

**Deep Graph (long chains):**
```
A → B → C → D → E → F
```
- DFS call stack gets deep
- BFS better for memory

---

## Path Finding Algorithms

### find_path() - Any Path (DFS)

Finds **any** path from start to end using DFS.

```python
def find_path(self, start, end, path=[]):
    """Find a path from start to end using DFS"""
    path = path + [start]    # Add current node to path
    
    if start == end:         # Reached destination!
        return path
    
    if start not in self.graph:    # Node doesn't exist
        return None
    
    # Try each neighbor
    for neighbor in self.graph[start]:
        if neighbor not in path:    # Avoid cycles
            newpath = self.find_path(neighbor, end, path)
            if newpath:    # Found a path!
                return newpath
    
    return None    # No path found
```

**How it works:**
1. Add current node to path
2. If reached end, return path
3. Try each neighbor recursively
4. If any neighbor finds path, return it
5. If no path found, return None

**Key feature:** Returns **first** path found (may not be shortest)

---

### shortest_path() - Shortest Path (BFS)

Finds **shortest** path from start to end using BFS.

```python
def shortest_path(self, start, end):
    """Find shortest path using BFS"""
    if start == end:
        return [start]
    
    if start not in self.graph:
        return None
    
    visited = {start}
    queue = deque([(start, [start])])    # (node, path to node)
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in self.graph[node]:
            if neighbor == end:
                return path + [neighbor]    # Found it!
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None    # No path found
```

**How it works:**
1. Store (node, path) tuples in queue
2. Process nodes level by level
3. When we reach end, return the path
4. First path found = shortest (BFS guarantee!)

**Key feature:** Guaranteed to find **shortest** path

---

### Comparison

**Example Graph:**
```
    A --- B
    |     |
    C --- D --- E
    |           |
    F -----------
```

**find_path('A', 'E'):**
- Result: `A → B → D → C → F → E` (6 nodes)
- Goes deep first, explores one complete path

**shortest_path('A', 'E'):**
- Result: `A → B → D → E` (4 nodes)
- Level by level, finds shortest

**BFS found 33% shorter path!**

---

## PART 2: LISTS & DICTIONARIES REFRESHER

### Lists

#### Basic Operations

```python
fruits = ["apple", "banana", "cherry"]

# Access
first = fruits[0]        # "apple"
last = fruits[-1]        # "cherry"

# Slice
first_two = fruits[0:2]  # ["apple", "banana"]
last_two = fruits[-2:]   # ["banana", "cherry"]

# Modify
fruits.append("date")    # Add to end
fruits.pop()             # Remove from end
fruits.insert(1, "blueberry")  # Insert at index
```

---

#### Looping

```python
# Simple loop
for fruit in fruits:
    print(fruit)

# With index (enumerate)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

#### Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
row = matrix[0]          # [1, 2, 3]
element = matrix[0][1]   # 2

# Loop
for row in matrix:
    for num in row:
        print(num, end=" ")
# Output: 1 2 3 4 5 6 7 8 9
```

---

#### List Comprehensions

```python
# Create new list
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
# [2, 4, 6, 8, 10]

# With condition
evens = [n for n in numbers if n % 2 == 0]
# [2, 4]

# From nested list
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4]
```

---

### Dictionaries

#### Basic Operations

```python
person = {"name": "Alice", "age": 25}

# Access
name = person["name"]              # "Alice" (crashes if missing!)
name = person.get("name")          # "Alice" (safe)
name = person.get("name", "Unknown")  # With default

# Modify
person["city"] = "NYC"             # Add new key
person["age"] = 26                 # Update existing
person.update({"country": "USA"})  # Update multiple

# Remove
age = person.pop("age")            # Remove and return
del person["city"]                 # Delete key

# Check
if "name" in person:               # Check if key exists
    print(person["name"])
```

---

#### Looping

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Loop through keys (default)
for key in person:
    print(key)

# Loop through keys explicitly
for key in person.keys():
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs (MOST COMMON!)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

#### Nested Dictionaries

```python
users = {
    "user1": {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "coding"]
    },
    "user2": {
        "name": "Bob",
        "age": 30,
        "hobbies": ["gaming", "music"]
    }
}

# Access nested values
name = users["user1"]["name"]              # "Alice"
hobby = users["user1"]["hobbies"][0]       # "reading"

# Safe access
name = users.get("user1", {}).get("name")  # "Alice"
name = users.get("user3", {}).get("name")  # None (no crash!)

# Loop through nested
for user_id, user_data in users.items():
    print(f"User: {user_data['name']}")
    print(f"Age: {user_data['age']}")
    print(f"Hobbies: {', '.join(user_data['hobbies'])}")
```

---

#### Dictionary Comprehensions

```python
# Create from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# Transform
prices = {"apple": 1.0, "banana": 0.5}
doubled = {k: v * 2 for k, v in prices.items()}
# {'apple': 2.0, 'banana': 1.0}

# Filter
expensive = {k: v for k, v in prices.items() if v > 0.7}
# {'apple': 1.0}
```

---

### Common Patterns

#### Pattern 1: Graph (Dictionary of Lists)

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D']
}

# Loop
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

# Access
neighbors = graph['A']  # ['B', 'C']
```

---

#### Pattern 2: Counting (Dictionary of Values)

```python
word_counts = {
    'the': 5,
    'cat': 2,
    'dog': 3
}

# Update count
word = "cat"
word_counts[word] = word_counts.get(word, 0) + 1
```

---

#### Pattern 3: Nested Data (Dictionary of Dictionaries)

```python
students = {
    'Alice': {'age': 20, 'grade': 'A'},
    'Bob': {'age': 21, 'grade': 'B'}
}

# Loop
for name, info in students.items():
    print(f"{name}: Age {info['age']}, Grade {info['grade']}")

# Safe access
age = students.get('Alice', {}).get('age', 0)
```

---

## Quick Reference

### Lists

```python
for item in list:                    # Loop
for i, item in enumerate(list):      # Loop with index
item = list[0]                       # Access
sublist = list[1:3]                  # Slice
list.append(item)                    # Add
list.pop()                           # Remove
```

### Dictionaries

```python
for key, value in dict.items():      # Loop (most common!)
value = dict.get(key, default)       # Safe access
dict[key] = value                    # Add/update
if key in dict:                      # Check exists
```

### Nested Dictionaries

```python
# Access
value = nested[key1][key2]
value = nested.get(key1, {}).get(key2, default)

# Loop
for outer_key, inner_dict in nested.items():
    for inner_key, value in inner_dict.items():
        print(f"{outer_key}.{inner_key} = {value}")
```

---

## Summary

### Graph Algorithms

**BFS (Breadth-First):**
- Level by level exploration
- Uses Queue (FIFO)
- Finds shortest path
- Good for: closest nodes, level-order, shortest path

**DFS (Depth-First):**
- Deep-first exploration
- Uses Recursion/Stack (LIFO)
- Explores all paths
- Good for: any path, cycles, topological sort

**Path Finding:**
- `find_path()` - Any path using DFS
- `shortest_path()` - Shortest path using BFS

### Lists & Dictionaries

**Lists:**
- Use `enumerate()` for index + value
- Nested lists need nested loops
- List comprehensions for transformations

**Dictionaries:**
- Use `.items()` for key-value pairs
- Use `.get(key, default)` for safe access
- Nested dictionaries: `dict[key1][key2]`

---

End of Day 22 Reference
```
