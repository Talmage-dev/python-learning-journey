"""Day 23: BFS and DFS Practice"""

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
    
    def shortest_path(self, start, end):
        """Find shortest path using BFS"""
        if start == end:                    # If start node is only node
            return [start]                  # return
    
        if start not in self.graph:         # If there are no nodes in the graph
            return None                     # return None
    
        visited = {start}                   # Dict of visited nodes
        queue = deque([(start, [start])])   # (node, path to node)
    
        while queue:                            # While there are nodes in the queue
            node, path = queue.popleft()        # get node and path
            for neighbour in self.graph[node]:  # for each neighbour of the node
                if neighbour == end:            # neighbour is the last node
                    return path + [neighbour]   # return path and neighbour
                
                if neighbour not in visited:    # if neighbour hasn't been visited
                    visited.add(neighbour)      # add neighbour to visited
                    queue.append((neighbour, path + [neighbour]))     # add neighbour and path to queue

        return None 
        
# ===== TESTS =====

# Build graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("=== Graph ===")
print("""
    A --- B
    |     |
    C --- D --- E
""")

print("=== BFS from A ===")
bfs_result = g.bfs('A')
print(f"Order: {' → '.join(bfs_result)}")

print("\n=== DFS from A ===")
dfs_result = g.dfs('A')
print(f"Order: {' → '.join(dfs_result)}")

print("\n=== Shortest Path A to E ===")
path = g.shortest_path('A', 'E')
print(f"Path: {' → '.join(path)}")
print(f"Length: {len(path)} nodes")