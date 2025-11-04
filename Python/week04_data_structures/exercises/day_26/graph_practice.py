"""Day 26: Graph Practice"""

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary: node -> list of neighbors
    
    def add_node(self, node):
        """Add a node to the graph"""
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        """Add a DIRECTED edge: from_node -> to_node"""
        # Add nodes if they don't exist
        self.add_node(node1)
        self.add_node(node2)
        
        # Add edge both ways (undirected)
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2)
    
    def out_degree(self, node):
        """Return number of edges going OUT from node"""
        if node not in self.graph:
            return 0
        return len(self.graph[node])
    
    def in_degree(self, node):
        """Return number of edge cases coming IN to node"""
        count = 0
        for vertex in self.graph:
            if node in self.graph[vertex]:
                count += 1
        return count
    
    def degree(self, node):
        """Return total degree (in + out)"""
        return self.out_degree(node) + self.in_degree(node)

    def has_cycle(self):
        """Check if graph has a cycle using DFS with 3 States"""
        # States:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # Initialize all nodes as UNVISITED
        state = {}
        for node in self.graph:
            state[node] = UNVISITED
        
        # Helper function for DFS
        def dfs(node):
            # Mark current node as VISITING (on current path)
            state[node] = VISITING
            # Check all neighbours
            for neighbour in self.graph[node]:
                if state[neighbour] == VISITING:
                    return True # Neighbour is on current path
                if state[neighbour] == UNVISITED: # Explore this neighbour
                    if dfs(neighbour):
                        return True # Cycle found in recursion
            state[node] = VISITED # Finished visiting this node and all its descendants
            return False
        
        for node in self.graph: # Try DFS from each unvisited node
            if state[node] == UNVISITED:
                if dfs(node):
                    return True # Cycle found
        
        return False # No cycle found

# Test 1: Graph with cycle
g1 = Graph()
g1.add_edge('A', 'B')
g1.add_edge('B', 'C')
g1.add_edge('C', 'D')
g1.add_edge('D', 'A')  # Cycle back to A!

print(g1.has_cycle())  # True

# Test 2: Graph without cycle (tree)
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'C')
g2.add_edge('B', 'D')

print(g2.has_cycle())  # False

# Test 3: Self-loop (simplest cycle)
g3 = Graph()
g3.add_edge('A', 'A')  # Points to itself!

print(g3.has_cycle())  # True

# Test 4: Disconnected graph with cycle in one component
g4 = Graph()
g4.add_edge('A', 'B')
g4.add_edge('C', 'D')
g4.add_edge('D', 'C')  # Cycle in C-D component

print(g4.has_cycle())  # True