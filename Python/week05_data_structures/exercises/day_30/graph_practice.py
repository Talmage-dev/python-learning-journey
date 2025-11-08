"""Day 30: Intensive Practice - Graphs"""

class Graph:
    def __init__(self):
        self.graph = {}   
        
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        """Add an edge between two nodes (directed)"""
        # Add nodes if they don't exist
        self.add_node(node1)
        self.add_node(node2)
        
        # Add edge (directed)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")
    
    # Problem 1:
    def get_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        if start not in self.graph:
            return []
        
        paths = []
        for neighbour in self.graph[start]:
            if neighbour not in path:
                newpaths = self.get_all_paths(neighbour, end, path)
                paths.extend(newpaths)
        
        return paths

# Test:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print(g.get_all_paths('A', 'D'))
# Should show: [['A', 'B', 'D'], ['A', 'C', 'D']]