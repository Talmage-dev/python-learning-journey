"""Day 27: Intensive Practice - Graphs"""

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        """DIRECTED egdes"""
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        # Add BOTH directions for undirected
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

# Case 1:
# Time Started: 12:35
# Time Fininshed: 1:00
    def count_components(self):
        # Track visited nodes
        visited = set()
        count = 0

        # Use BFS and DFS to explore each component
        def bfs(start_node):
            queue = [start_node]
            visited.add(start_node)
            while queue:
                node = queue.pop(0)
                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        # Count how many times you start a new exploation
        for node in self.graph:
            if node not in visited:
                bfs(node)
                count += 1
        
        return count
    
    # Case 2:
    # Time started: 1:15pm
    # Time finished: 1:16pm
    def is_connected(self):
        return self.count_components() == 1

# Test count_components()
# Test 1: Two components
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
print(g.count_components())  # Should be 2

# Test 2: One component
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('B', 'C')
g2.add_edge('C', 'D')
print(g2.count_components())  # Should be 1

# Test 3: Three isolated nodes
g3 = Graph()
g3.add_node('A')
g3.add_node('B')
g3.add_node('C')
print(g3.count_components())  # Should be 3

# Test is_connected()
# Test 1: Two components
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
print(g.is_connected())  # False

# Test 2: One component
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('B', 'C')
g2.add_edge('C', 'D')
print(g2.is_connected())  # True

# Test 3: Isolated nodes
g3 = Graph()
g3.add_node('A')
g3.add_node('B')
print(g3.is_connected())  # False