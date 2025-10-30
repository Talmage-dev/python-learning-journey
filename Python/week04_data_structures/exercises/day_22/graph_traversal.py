"""Day 22: Graph Traversal Algorithms - BFS & DFS"""

# BFS (Breadth-First Search)
from collections import deque

def bfs(graph, start):
    """Breadth-First search"""
    visited = set()             # Track visited nodes
    queue = deque([start])      # Queue for BFS
    visited.add(start)
    result = []                 # Order of visits
    
    while queue:
        node = queue.popleft()  # Get front of queue
        result.append(node)     # Add to result(order of visits)

        # Visit all unvisited neighbours
        for neighbour in graph[node]:       # for every neighbour of node
            if neighbour not in visited:    # if not in set
                visited.add(neighbour)      # add to set
                queue.append(neighbour)     # add to queue
    
    return result               # return order of visits

# DFS (Depth-First Search)
def dfs(graph, start, visited=None):
    """Depth-first search (recursive)"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]

    #Visit each unvisited neighbour
    for neighbour in graph[start]:
        if neighbour not in visited:
            result.extend(dfs(graph, neighbour, visited))
    
    return result