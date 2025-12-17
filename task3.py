import networkx as nx
import matplotlib.pyplot as plt

# Create the same social network but with weighted edges
G = nx. Graph()

people = ["Anzhela", "Maria", "Ivan", "Petro", "Olena", "Sergiy", "Natalia", "Andriy"]
G.add_nodes_from(people)

# Add friendships with weights (interaction strength/frequency)
# Higher weight = stronger connection/more interaction
weighted_friendships = [
    ("Anzhela", "Maria", 8),
    ("Anzhela", "Ivan", 5),
    ("Anzhela", "Petro", 3),
    ("Maria", "Olena", 7),
    ("Maria", "Ivan", 6),
    ("Ivan", "Sergiy", 4),
    ("Petro", "Natalia", 5),
    ("Petro", "Andriy", 2),
    ("Olena", "Sergiy", 9),
    ("Sergiy", "Andriy", 6),
    ("Natalia", "Andriy", 7)
]

for person1, person2, weight in weighted_friendships:
    G.add_edge(person1, person2, weight=weight)

# Visualize weighted graph
plt.figure(figsize=(12, 9))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
        node_size=2000, font_size=12, font_weight='bold', 
        edge_color='gray', width=2)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

plt.title("Social Network with Connection Strength", fontsize=16)
plt.savefig('weighted_social_network.png')
plt.show()

print("=== Dijkstra's Algorithm - Shortest Paths ===\n")
print("Weights represent connection strength (higher = stronger connection)\n")

# Find shortest paths between all pairs using Dijkstra
print("Shortest paths from Anzhela to everyone:\n")

start = "Anzhela"

for person in people:
    if person != start:
        # Find shortest path
        path = nx.dijkstra_path(G, start, person, weight='weight')
        # Get total weight
        path_weight = nx.dijkstra_path_length(G, start, person, weight='weight')
        
        print(f"{start} → {person}:")
        print(f"  Path: {' → '.join(path)}")
        print(f"  Total connection strength: {path_weight}")
        print()

# Find the shortest path between two specific people
print("="*60)
print("\nExample:  Best connection path from Anzhela to Andriy\n")

path = nx.dijkstra_path(G, "Anzhela", "Andriy", weight='weight')
length = nx.dijkstra_path_length(G, "Anzhela", "Andriy", weight='weight')

print(f"Path: {' → '.join(path)}")
print(f"Total strength: {length}")

print("\nThis path was chosen because it maximizes connection strength")
print("(in real terms:  these people interact most frequently)")

# Compare with unweighted shortest path
simple_path = nx.shortest_path(G, "Anzhela", "Andriy")
print(f"\nCompare with unweighted shortest path: {' → '.join(simple_path)}")
print(f"Number of hops: {len(simple_path) - 1}")

if path != simple_path:
    print("\nDifferent from unweighted!  Dijkstra considers connection strength,")
    print("not just number of connections.")
else:
    print("\nSame as unweighted path in this case.")

# All pairs shortest paths
print("\n" + "="*60)
print("\nShortest path distances between ALL people:\n")

all_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Show as a table
print(f"{'From':<10}", end="")
for person in people:
    print(f"{person:<10}", end="")
print()

for person1 in people:
    print(f"{person1:<10}", end="")
    for person2 in people:
        if person1 == person2:
            print(f"{'-':<10}", end="")
        else:
            distance = all_paths[person1][person2]
            print(f"{distance: <10.0f}", end="")
    print()

print("\nGraph visualization saved as 'weighted_social_network.png'")