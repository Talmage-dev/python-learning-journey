
---

# **DAY 21 REFERENCE - GRAPHS**

```markdown
# Day 21: Graphs Reference

## Date: October 29, 2025 (Wednesday)

---

## What is a Graph?

A **graph** is a collection of **nodes (vertices)** connected by **edges (connections)**.

**Real-world examples:**
- Social networks (people connected by friendships)
- Maps (cities connected by roads)
- Websites (pages connected by links)
- Computer networks (devices connected by cables)
- Task dependencies (tasks connected by requirements)

---

## Graph vs Tree

### **Tree:**
- Hierarchical structure
- Parent-child relationships
- One path between any two nodes
- No cycles (loops)
- Has a root node

```
    A
   / \
  B   C
 /
D
```

### **Graph:**
- Non-hierarchical structure
- Any connections possible
- Multiple paths between nodes
- Can have cycles
- No root node

```
    A --- B
    |     |
    |     |
    C --- D --- E
```

---

## Graph Terminology

### **Nodes (Vertices)**
The points in the graph.

### **Edges**
The connections between nodes.
- Think of as: connection, path, relationship, reference

### **Neighbors (Adjacent Nodes)**
Nodes directly connected by an edge.

### **Degree**
Number of edges connected to a node.

### **Path**
Sequence of edges connecting nodes.

### **Cycle**
Path that starts and ends at the same node.

---

## Types of Graphs

### **1. Directed vs Undirected**

**Undirected Graph:**
- Edges go both ways
- If A connects to B, then B connects to A
- Example: Facebook friends (mutual)

```
A --- B  (A ↔ B)
```

**Directed Graph (Digraph):**
- Edges have direction
- A → B doesn't mean B → A
- Example: Twitter follows (one-way)

```
A --> B  (A → B, but not B → A)
```

### **2. Weighted vs Unweighted**

**Unweighted Graph:**
- All edges are equal
- Just connected or not

```
A --- B  (just connected)
```

**Weighted Graph:**
- Edges have values (weight)
- Represents distance, cost, time, etc.

```
A --5-- B  (distance = 5)
A --10- C  (distance = 10)
```

### **3. Cyclic vs Acyclic**

**Cyclic:**
- Contains cycles (loops)

```
A --- B
|     |
C --- D  (A → B → D → C → A is a cycle)
```

**Acyclic:**
- No cycles
- Trees are acyclic graphs!

```
A --- B
|
C --- D  (no way to return to start)
```

---

## Graph Representations

### **Method 1: Adjacency List (Most Common)**

Store each node's neighbors in a list/dictionary.

**Python Implementation:**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
```

**Visual:**
```
A connects to: B, C
B connects to: A, D
C connects to: A, D
D connects to: B, C, E
E connects to: D
```

**Advantages:**
- Space efficient: O(V + E)
- Fast to iterate neighbors
- Easy to add/remove edges

**Disadvantages:**
- Slower to check if edge exists: O(degree)

---

### **Method 2: Adjacency Matrix**

2D array where `matrix[i][j] = 1` if edge exists.

```python
#   A  B  C  D  E
A [[0, 1, 1, 0, 0],
B  [1, 0, 0, 1, 0],
C  [1, 0, 0, 1, 0],
D  [0, 1, 1, 0, 1],
E  [0, 0, 0, 1, 0]]
```

**Advantages:**
- Fast edge lookup: O(1)
- Simple to implement

**Disadvantages:**
- Space inefficient: O(V²)
- Slow to iterate neighbors

---

## Basic Graph Implementation

```python
class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary: node -> list of neighbors
    
    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        """Add an edge between two nodes (undirected)"""
        # Add nodes if they don't exist
        self.add_node(node1)
        self.add_node(node2)
        
        # Add edge both ways (undirected)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
        if node1 not in self.graph[node2]:
            self.graph[node2].append(node1)
    
    def get_neighbors(self, node):
        """Get all neighbors of a node"""
        return self.graph.get(node, [])
    
    def display(self):
        """Show all connections"""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")
```

---

## Common Graph Operations

### **1. Add Node**
```python
def add_node(self, node):
    if node not in self.graph:
        self.graph[node] = []
```

### **2. Add Edge (Undirected)**
```python
def add_edge(self, node1, node2):
    self.add_node(node1)
    self.add_node(node2)
    
    if node2 not in self.graph[node1]:
        self.graph[node1].append(node2)
    if node1 not in self.graph[node2]:
        self.graph[node2].append(node1)
```

### **3. Add Edge (Directed)**
```python
def add_directed_edge(self, from_node, to_node):
    self.add_node(from_node)
    self.add_node(to_node)
    
    if to_node not in self.graph[from_node]:
        self.graph[from_node].append(to_node)
```

### **4. Remove Node**
```python
def remove_node(self, node):
    if node in self.graph:
        # Remove all edges to this node
        for neighbors in self.graph.values():
            if node in neighbors:
                neighbors.remove(node)
        # Remove the node itself
        del self.graph[node]
```

### **5. Remove Edge**
```python
def remove_edge(self, node1, node2):
    if node1 in self.graph and node2 in self.graph[node1]:
        self.graph[node1].remove(node2)
    if node2 in self.graph and node1 in self.graph[node2]:
        self.graph[node2].remove(node1)
```

### **6. Check if Edge Exists**
```python
def has_edge(self, node1, node2):
    return node1 in self.graph and node2 in self.graph[node1]
```

---

## Graph Traversal Algorithms

### **Breadth-First Search (BFS)**

Explore level by level (like ripples in water).

**Uses:**
- Shortest path (unweighted)
- Level-order traversal
- Connected components

**Implementation:**
```python
from collections import deque

def bfs(self, start):
    """Breadth-first search from start node"""
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

**Example:**
```
    A --- B
    |     |
    C --- D --- E

BFS from A: A, B, C, D, E
(Level 0: A, Level 1: B,C, Level 2: D, Level 3: E)
```

---

### **Depth-First Search (DFS)**

Explore as deep as possible before backtracking.

**Uses:**
- Cycle detection
- Topological sorting
- Path finding

**Implementation (Recursive):**
```python
def dfs(self, start, visited=None):
    """Depth-first search from start node"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in self.graph[start]:
        if neighbor not in visited:
            result.extend(self.dfs(neighbor, visited))
    
    return result
```

**Example:**
```
    A --- B
    |     |
    C --- D --- E

DFS from A: A, B, D, C, E
(Go deep: A→B→D→E, backtrack, then C)
```

---

## Common Graph Problems

### **1. Find Path Between Nodes**

```python
def find_path(self, start, end, path=[]):
    """Find a path from start to end"""
    path = path + [start]
    
    if start == end:
        return path
    
    if start not in self.graph:
        return None
    
    for node in self.graph[start]:
        if node not in path:  # Avoid cycles
            newpath = self.find_path(node, end, path)
            if newpath:
                return newpath
    
    return None
```

### **2. Check if Connected**

```python
def is_connected(self, node1, node2):
    """Check if two nodes are connected"""
    return self.find_path(node1, node2) is not None
```

### **3. Find All Paths**

```python
def find_all_paths(self, start, end, path=[]):
    """Find all paths from start to end"""
    path = path + [start]
    
    if start == end:
        return [path]
    
    if start not in self.graph:
        return []
    
    paths = []
    for node in self.graph[start]:
        if node not in path:
            newpaths = self.find_all_paths(node, end, path)
            paths.extend(newpaths)
    
    return paths
```

### **4. Shortest Path (Unweighted)**

```python
def shortest_path(self, start, end):
    """Find shortest path using BFS"""
    if start == end:
        return [start]
    
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
    
    return None  # No path found
```

---

## When to Use Graphs

✅ **Social Networks**
- Friends, followers, connections
- Recommendation systems

✅ **Maps and Navigation**
- Cities and roads
- GPS routing
- Flight connections

✅ **Networks**
- Computer networks
- Internet routing
- Phone networks

✅ **Dependencies**
- Task scheduling
- Package dependencies
- Build systems

✅ **Games**
- Pathfinding (A*)
- Game state trees
- AI decision making

✅ **Recommendation Systems**
- "People who bought X also bought Y"
- Similar items/users

---

## Graph vs Other Structures

### **Graph vs Tree**

**Use Graph when:**
- Multiple paths between nodes
- Cycles are allowed/needed
- No hierarchical relationship

**Use Tree when:**
- Hierarchical data
- One path between nodes
- No cycles

### **Graph vs Hash Table**

**Use Graph when:**
- Relationships between items matter
- Need to traverse connections
- Network/connection problems

**Use Hash Table when:**
- Just need fast lookup
- No relationships to track
- Key-value associations

---

## Time Complexity

| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| Add node | O(1) | O(V²) |
| Add edge | O(1) | O(1) |
| Remove node | O(V + E) | O(V²) |
| Remove edge | O(E) | O(1) |
| Check edge | O(degree) | O(1) |
| Get neighbors | O(1) | O(V) |
| Space | O(V + E) | O(V²) |

**V = vertices (nodes), E = edges**

---

## Common Patterns

### **Pattern 1: Build Graph from Edges**

```python
def build_graph(edges):
    graph = Graph()
    for node1, node2 in edges:
        graph.add_edge(node1, node2)
    return graph

# Example
edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
g = build_graph(edges)
```

### **Pattern 2: Count Connected Components**

```python
def count_components(self):
    visited = set()
    count = 0
    
    for node in self.graph:
        if node not in visited:
            self._dfs_visit(node, visited)
            count += 1
    
    return count
```

### **Pattern 3: Detect Cycle**

```python
def has_cycle(self):
    visited = set()
    rec_stack = set()
    
    for node in self.graph:
        if node not in visited:
            if self._has_cycle_util(node, visited, rec_stack):
                return True
    
    return False
```

---

## Key Insights

### **Why Graphs are Powerful:**

1. **Model Real Relationships** - Represent any connection
2. **Flexible** - No rigid structure like trees
3. **Algorithms** - Rich set of graph algorithms
4. **Universal** - Many problems reduce to graphs

### **Edge as Connection:**

Think of edge as:
- ✅ Connection between nodes
- ✅ Relationship (friendship, road, link)
- ✅ Path you can travel
- ✅ Reference (node's list contains neighbor)
- ❌ Not quite a pointer (like in trees)

### **Adjacency List vs Matrix:**

**Use Adjacency List when:**
- Sparse graph (few edges)
- Need to iterate neighbors often
- Memory is a concern

**Use Adjacency Matrix when:**
- Dense graph (many edges)
- Need fast edge lookup
- Simple implementation preferred

---

## Summary

**Graph:**
- Collection of nodes connected by edges
- Non-hierarchical (unlike trees)
- Can have cycles
- Multiple paths between nodes

**Key Operations:**
- Add/remove nodes and edges
- Get neighbors
- Traverse (BFS, DFS)
- Find paths

**When to use:**
- Relationships matter
- Network problems
- Connection/path problems
- Social networks, maps, dependencies

---

End of Day 21 Reference
```

---
