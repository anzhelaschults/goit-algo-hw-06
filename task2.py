import networkx as nx
from collections import deque

# Recreate the same social network from Task 1
G = nx. Graph()

people = ["Anzhela", "Maria", "Ivan", "Petro", "Olena", "Sergiy", "Natalia", "Andriy"]
G.add_nodes_from(people)

friendships = [
    ("Anzhela", "Maria"),
    ("Anzhela", "Ivan"),
    ("Anzhela", "Petro"),
    ("Maria", "Olena"),
    ("Maria", "Ivan"),
    ("Ivan", "Sergiy"),
    ("Petro", "Natalia"),
    ("Petro", "Andriy"),
    ("Olena", "Sergiy"),
    ("Sergiy", "Andriy"),
    ("Natalia", "Andriy")
]
G.add_edges_from(friendships)


def dfs_paths(graph, start, goal, path=None):
    """Depth-First Search to find a path"""
    if path is None: 
        path = []
    path = path + [start]
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:  
            new_path = dfs_paths(graph, neighbor, goal, path)
            if new_path: 
                return new_path
    
    return None


def bfs_paths(graph, start, goal):
    """Breadth-First Search to find a path"""
    queue = deque([(start, [start])])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        for neighbor in graph.neighbors(current):
            if neighbor not in path:  # Avoid cycles
                queue. append((neighbor, path + [neighbor]))
    
    return None


# Testing both algorithms
print("=== DFS vs BFS Path Finding ===\n")

start_person = "Anzhela"
end_person = "Andriy"

print(f"Finding path from {start_person} to {end_person}\n")

# DFS
dfs_path = dfs_paths(G, start_person, end_person)
print(f"DFS path: {' → '.join(dfs_path)}")
print(f"DFS path length: {len(dfs_path) - 1} connections\n")

# BFS
bfs_path = bfs_paths(G, start_person, end_person)
print(f"BFS path: {' → '. join(bfs_path)}")
print(f"BFS path length: {len(bfs_path) - 1} connections\n")

print("="*50)
print("\n### Analysis ###\n")

if len(dfs_path) == len(bfs_path):
    print("Both algorithms found paths of the same length.")
else:
    print(f"BFS found a shorter path ({len(bfs_path) - 1} vs {len(dfs_path) - 1} connections)")

print("\nWhy the difference?")
print("- DFS goes deep into one branch first, so it might find a longer path")
print("- BFS explores all neighbors level by level, guaranteeing the shortest path")
print(f"\nIn this case:")
print(f"  DFS explored: {' → '.join(dfs_path)}")
print(f"  BFS found optimal: {' → '.join(bfs_path)}")

# Test with another pair
print("\n" + "="*50)
print("\nTesting another pair:\n")

start_person2 = "Maria"
end_person2 = "Natalia"

print(f"Finding path from {start_person2} to {end_person2}\n")

dfs_path2 = dfs_paths(G, start_person2, end_person2)
bfs_path2 = bfs_paths(G, start_person2, end_person2)

print(f"DFS path:  {' → '.join(dfs_path2)}")
print(f"BFS path: {' → '.join(bfs_path2)}")

if dfs_path2 == bfs_path2:
    print("\nBoth algorithms found the same path!")
else:
    print(f"\nDifferent paths found:")
    print(f"  DFS length: {len(dfs_path2) - 1}")
    print(f"  BFS length: {len(bfs_path2) - 1}")