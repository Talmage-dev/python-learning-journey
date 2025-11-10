"""Day 32: Intensive Practice - Graphs"""

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import Graph

# Problem 1:
# Start: 17:34

def bfs(self, start):
    visited = set()
    visited.add(start)
    queue = [start]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return result

# Finished: 17:41

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

print(g.bfs('A'))  # Should give: ['A', 'B', 'C', 'D'] (or similar order)

# Problem 2:
# Start: 17:46

def dfs(self, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return result

# Finished: 17:49

g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'C')
g2.add_edge('B', 'D')

print(g2.dfs('A'))  # Should give: ['A', B, D, C] or similar (deep first!)

# Problem 3:
# Start: 17:55
def has_path(self, start, end):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return False
# Finished: 18:03

g3 = Graph()
g3.add_edge('A', 'B')
g3.add_edge('A', 'C')
g3.add_edge('B', 'D')
g3.add_node('E')  # Isolated node

print(g3.has_path('A', 'D'))  # → True
print(g3.has_path('A', 'E'))  # → False
print(g3.has_path('B', 'C'))  # → True