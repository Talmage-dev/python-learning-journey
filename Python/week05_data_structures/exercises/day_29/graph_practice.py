"""Day 29: Intensive Practice - Graphs"""

class Graph:
    def __init__(self):
        self.graph = {}   
        
    def add_node(self, node):
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

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

# Problem 1:
# Start: 18:00
    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)
        if node2 in self.graph and node1 in self.graph[node2]:
            self.graph[node2].remove(node1)
# Finished: 18:13

# Problem 2:
# Start: 18:15
    def remove_vertex(self, node):
        if node in self.graph:
            # Remove all edges to node
            for neighbors in self.graph.values():
                if node in neighbors:
                    neighbors.remove(node)
            # Remove node
            del self.graph[node]
# Finished: 18:20

# Test P1:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.display()  # Should show: A-B, B-C, B-D

g.remove_edge('B', 'D')
g.display()  # Should show: A-B, B-C (D isolated)
        
# Test P2:
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('B', 'C')
g2.add_edge('B', 'D')
g2.display()  # Should show: A-B, B-C, B-D

g2.remove_vertex('B')
g2.display()  # Should show: A, C, D (all isolated)