# goit-algo-hw-06

Task on Graphs

## What I Did

I created a social network graph to model friendships between people. The graph has 8 people and their connections. 

### Task 1 - Creating and Analyzing the Graph

I built a social network with 8 people and their friendships using NetworkX. 

**File:** `task1.py`

**Graph characteristics:**
- 8 nodes (people)
- 11 edges (friendships)
- The graph shows who is friends with whom

**My analysis:**
- Some people have more friends than others
- The most connected person has the most friendships
- Everyone in the network can reach everyone else (the graph is connected)
- Average number of friends shows how social the network is overall

The visualization is saved as `social_network.png`.

### Task 2 - DFS and BFS Path Finding

I implemented both Depth-First Search and Breadth-First Search to find paths between people.

**File:** `task2.py`

**What I found:**
- DFS and BFS often find different paths between the same two people
- BFS always finds the shortest path (fewest connections)
- DFS goes deep into one direction first, so it might take a longer route

**Why this happens:**
- BFS explores all immediate neighbors first, then their neighbors, etc.  This guarantees the shortest path. 
- DFS picks one neighbor and goes as far as possible before backtracking.  It finds *a* path but not necessarily the shortest.

**Example from my tests:**
When searching from Anzhela to Andriy:
- BFS found the optimal shortest path
- DFS might have taken a longer route depending on which neighbor it explored first

This makes sense for a social network - BFS would find how you're connected to someone through the fewest mutual friends. 

### Task 3 - Dijkstra's Algorithm with Weights

I added weights to represent connection strength (how much two people interact). Higher weight = stronger friendship.

**File:** `task3.py`

**What Dijkstra does:**
- Finds the path with the highest total connection strength
- Different from just counting number of connections
- Considers quality of friendships, not just quantity

**My example:**
The shortest weighted path between two people might have more hops but stronger connections overall.  This is more realistic - in real life you'd reach out through close friends even if it's not the most direct path.

The weighted graph is saved as `weighted_social_network.png`.

## How to Run

First install requirements:
```bash
pip3 install networkx matplotlib
```

Then run each task:
```bash
python3 task1.py
python3 task2.py  
python3 task3.py
```

## Files
- `task1.py` - Graph creation and analysis
- `task2.py` - DFS and BFS comparison
- `task3.py` - Dijkstra's algorithm
- `social_network.png` - Visualization from task 1
- `weighted_social_network.png` - Weighted graph from task 3

## Conclusions

Working with graphs helped me understand how networks work. The different search algorithms (DFS vs BFS) have different use cases - BFS for shortest path, DFS for exploring all possibilities.  Dijkstra's algorithm is useful when connections have different "costs" or weights, which is very realistic for modeling real-world networks. 
