import networkx as nx
import matplotlib.pyplot as plt

# Create a social network graph
G = nx.Graph()

# Add people (nodes)
people = ["Anzhela", "Maria", "Ivan", "Petro", "Olena", "Sergiy", "Natalia", "Andriy"]
G.add_nodes_from(people)

# Add friendships (edges)
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

# Visualize the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=2000, font_size=12, font_weight='bold', 
        edge_color='gray', width=2)
plt.title("Social Network - Friend Connections", fontsize=16)
plt.savefig('social_network.png')
plt.show()

print("=== Social Network Analysis ===\n")

# Basic characteristics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Number of people (nodes): {num_nodes}")
print(f"Number of friendships (edges): {num_edges}")
print()

# Degree of each person (how many friends they have)
print("Friends count for each person:")
for person in people:
    degree = G.degree(person)
    print(f"  {person}: {degree} friends")

print()

# Find person with most friends
degrees = dict(G.degree())
most_connected = max(degrees, key=degrees.get)
print(f"Most connected person: {most_connected} with {degrees[most_connected]} friends")

# Find person with least friends
least_connected = min(degrees, key=degrees.get)
print(f"Least connected person: {least_connected} with {degrees[least_connected]} friends")

print()

# Average number of friends
avg_degree = sum(degrees.values()) / len(degrees)
print(f"Average number of friends: {avg_degree:.2f}")

# Check if graph is connected
if nx. is_connected(G):
    print("\nThe network is fully connected - everyone can reach everyone else")
else:
    print("\nThe network has isolated groups")

print("\nGraph visualization saved as 'social_network.png'")