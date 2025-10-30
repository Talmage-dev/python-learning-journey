""" Day 21: Graph's """

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}         # {node: [list of neighbours]}
    
    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        """Add an edge between two nodes (undirected)"""
        # Add node if they don't exist
        self.add_node(node1)
        self.add_node(node2)

        # Add edge both ways
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
        if node1 not in self.graph[node2]:
            self.graph[node2].append(node1)
    
    def display(self):
        for node, neighbours in self.graph.items():         # for key, value in dict.items():
            print(f"{node}: {neighbours}")

    def get_neighbour(self, node):
        """Get all neighbours of node"""
        return self.graph.get(node, [])
    
    # BFS (Breadth-First Search)
    def bfs(self, start):
        """Breadth-First search"""
        visited = set()             # Track visited nodes
        queue = deque([start])      # Queue for BFS
        visited.add(start)
        result = []                 # Order of visits
    
        while queue:
            node = queue.popleft()  # Get front of queue
            result.append(node)     # Add to result(order of visits)

            # Visit all unvisited neighbours
            for neighbour in self.graph[node]:       # for every neighbour of node
                if neighbour not in visited:    # if not in set
                    visited.add(neighbour)      # add to set
                    queue.append(neighbour)     # add to queue
    
        return result               # return order of visits
    
    # DFS (Depth-First Search)
    def dfs(self, start, visited=None):
        """Depth-first search (recursive)"""
        if visited is None:
            visited = set()
    
        visited.add(start)
        result = [start]

        #Visit each unvisited neighbour
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                result.extend(self.dfs(neighbour, visited))
    
        return result

    # Implimentation:
    # Find path using DFS
    def find_path(self, start, end, path=[]):
        """Find a path from start to end using DFS"""
        path = path + [start]                   # Add current node to path
        if start == end:                        # Reached destination
            return path
        if start not in self.graph:             # Node doesn't exist
            return None
        # Try each neighbour
        for neighbour in self.graph[start]:
            if neighbour not in path:           # Avoid cycles
                new_path = self.find_path(neighbour, end, path)
                if new_path:                    # Found a path
                    return new_path
        return None                             # No path found
    
    # Shortest Path using BFS
    def shortest_path(self, start, end):
        """Finds shortest path usin BFS"""
        if start == end:
            return [start]
        if start not in self.graph:
            return None
        visited = {start}
        queue = deque([(start, [start])])       # (node, path to node)
        while queue:
            node, path = queue.popleft()
            for neighbour in self.graph[node]:
                if neighbour == end:
                    return path + [neighbour]   # Found it
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [neighbour]))
        return None                             # No path found

# # Test the graph
# g = Graph()

# # Add edges (nodes are added automatically)
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# g.add_edge('D', 'E')

# print("=== Graph Structure ===")
# g.display()

# print("\n=== Neighbors ===")
# print(f"A's neighbours: {g.get_neighbour('A')}")
# print(f"D's neighbours: {g.get_neighbour('D')}")
# print(f"E's neighbours: {g.get_neighbour('E')}")

# print("\n=== Visual Representation ===")
# print("""
#     A --- B
#     |     |
#     |     |
#     C --- D --- E
# """)

# # Test BFS and DFS
# g = Graph()

# # Build the graph
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# g.add_edge('D', 'E')

# print("=== Graph Structure ===")
# g.display()

# print("\n=== BFS from A ===")
# bfs_result = g.bfs('A')
# print(f"Order: {' → '.join(bfs_result)}")

# print("\n=== DFS from A ===")
# dfs_result = g.dfs('A')
# print(f"Order: {' → '.join(dfs_result)}")

# print("\n=== Visual ===")
# print("""
#     A --- B
#     |     |
#     C --- D --- E
# """)

# print("\nBFS (level by level): A → B, C → D → E")
# print("DFS (deep first): A → B → D → C → E (or similar)")

# Test path finding
g = Graph()

# Build a more complex graph
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.add_edge('C', 'F')
g.add_edge('F', 'E')

print("=== Graph Structure ===")
g.display()

print("\n=== Visual ===")
print("""
    A --- B
    |     |
    C --- D --- E
    |           |
    F -----------
""")

print("\n=== Find ANY Path (DFS) ===")
path1 = g.find_path('A', 'E')
print(f"A to E: {' → '.join(path1) if path1 else 'No path'}")

print("\n=== Find SHORTEST Path (BFS) ===")
path2 = g.shortest_path('A', 'E')
print(f"A to E: {' → '.join(path2) if path2 else 'No path'}")

print("\n=== Compare ===")
if path1 and path2:
    print(f"DFS path length: {len(path1)} nodes")
    print(f"BFS path length: {len(path2)} nodes")
    if len(path2) < len(path1):
        print("✓ BFS found shorter path!")
    elif len(path2) == len(path1):
        print("✓ Both found same length path!")