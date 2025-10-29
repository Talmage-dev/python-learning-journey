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
    
    def display(self):
        """Show all connections"""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")