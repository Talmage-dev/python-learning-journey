""" Day 21: Graph's """

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

# Test the graph
g = Graph()

# Add edges (nodes are added automatically)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("=== Graph Structure ===")
g.display()

print("\n=== Neighbors ===")
print(f"A's neighbours: {g.get_neighbour('A')}")
print(f"D's neighbours: {g.get_neighbour('D')}")
print(f"E's neighbours: {g.get_neighbour('E')}")

print("\n=== Visual Representation ===")
print("""
    A --- B
    |     |
    |     |
    C --- D --- E
""")