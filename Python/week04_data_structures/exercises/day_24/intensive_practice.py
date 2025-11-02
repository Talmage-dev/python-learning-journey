""" Day 24: Intensive Practice """

# Bubble sort
def bubble_sort(ar):
    n = len(ar)
    for i in range(n):
        swapped = False
        for j in range(n - i -1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar [j]
                swapped = True
        if not swapped:
            break
    return ar

# Hash Tables
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Get index
        index = self._hash(key)

        # Check if key exists, update if so update key's values
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
            
        # Otherwise append new key value pair
        self.table[index].append((key, value))

    def get(self, key):
        # Get index
        index = self._hash(key)
        
        # look for key
        for k, v in self.table[index]:
            if k == key:    # When key found
                return v    # Return value
        
        return None         # Key not found

def first_unique(array):
    ht = HashTable(len(array))
    # Count Occurrances
    for num in array:
        count = ht.get(num)         # get element
        if count is None:           # if it doesn't have a count
            count = 0               # count starts at 0
        ht.insert(num, count + 1)   # if it has a count, a 1 to the count
    # Find unique first element
    for num in array:
        if ht.get(num) == 1:
            return num
    return None

# Test
ar = [4, 5, 1, 2, 3, 1]
f_u = first_unique(ar)
print(f_u)

def character_frequency(text):
    ht = HashTable(len(text))
    # Count Ocuurances
    for char in text:
        count = ht.get(char)
        if count is None:
            count = 0
        ht.insert(char, count + 1)
    result = {}
    for bucket in ht.table:
        for key, value in bucket:
            result[key] = value
    return result

# Test
text = "hello"
char_freq = character_frequency(text)
print(char_freq)

def has_duplicates(array):
    ht = HashTable(len(array))
    for num in array:
        if ht.get(num) is not None:
            return True
        ht.insert(num, True)
    return False

# ===== TEST ALL =====

print("=== Test 1: first_unique ===")
arr1 = [4, 5, 1, 2, 3, 1]
result1 = first_unique(arr1)
print(f"Array: {arr1}")
print(f"First unique: {result1}")
print(f"Expected: 4\n")

print("=== Test 2: character_frequency ===")
text = "hello"
result2 = character_frequency(text)
print(f"Text: '{text}'")
print(f"Frequencies: {result2}")
print(f"Expected: {{'h': 1, 'e': 1, 'l': 2, 'o': 1}}\n")

print("=== Test 3: has_duplicates ===")
arr2 = [1, 2, 3, 4, 5]
arr3 = [1, 2, 3, 1]
result3 = has_duplicates(arr2)
result4 = has_duplicates(arr3)
print(f"Array: {arr2} → {result3} (Expected: False)")
print(f"Array: {arr3} → {result4} (Expected: True)")

# Graphs
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node1, node2):
        # Add nodes if they don't exist
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        
        # Add edge both ways (undirected)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
        if node1 not in self.graph[node2]:
            self.graph[node2].append(node1)
    
    def bfs(self, start):
        """Breadth-first search from start node"""
        visited = set()             # Track visited nodes
        queue = deque([start])      # Queue for BFS
        visited.add(start)          # Add node to visited
        result = []                 # empty list for results

        while queue:
            node = queue.popleft()  # Get the front of the queue
            result.append(node)     # Add it to the results

            # Visit all unvisited neighbours
            for neighbour in self.graph[node]:  # for each neighbour of the node 
                if neighbour not in visited:    # if the neighbour has not been visited
                    visited.add(neighbour)      # add neighbour to the visited set
                    queue.append(neighbour)     # add neighbour to the queue
            
        return result
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        #Visit each unvisited neighbour
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                result.extend(self.dfs(neighbour, visited))
        
        return result
    
    def is_connected(self, start, end):
        """Check if path exists between start and end"""
        if start == end:
            return True
        if start not in self.graph:
            return False
        
        visited = set()
        visited.add(start)
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False
    
    def find_all_paths(self, start, end, path=[]):
        """Find all paths from start to end"""
        path = path + [start]       # Add current node to path
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for neighbour in self.graph[start]:
            if neighbour not in path:
                new_path = self.find_all_paths(neighbour, end, path)
                paths.extend(new_path)
        return paths
    
# ===== GRAPH TESTS =====

# Build graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.add_edge('C', 'F')
g.add_edge('F', 'E')

print("=== Graph ===")
print("""
    A --- B
    |     |
    C --- D --- E
    |           |
    F -----------
""")

print("=== Test 1: is_connected ===")
print(f"A to E: {g.is_connected('A', 'E')}")  # Should be True
print(f"A to Z: {g.is_connected('A', 'Z')}")  # Should be False

print("\n=== Test 2: find_all_paths ===")
all_paths = g.find_all_paths('A', 'E')
print(f"All paths from A to E:")
for i, path in enumerate(all_paths, 1):
    print(f"  Path {i}: {' → '.join(path)}")