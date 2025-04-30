# Dijkstra's Algorithm for Shortest Path

# Function to implement Dijkstra's algorithm
def dijkstra(graph, start, n):
    # Initialize the distance to all nodes as infinity
    dist = {node: float('inf') for node in range(1, n + 1)}
    dist[start] = 0  # Distance to the source node is 0
    
    # To track visited nodes
    visited = {node: False for node in range(1, n + 1)}
    
    # Dijkstra's algorithm
    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_node = -1
        min_dist = float('inf')
        
        for node in range(1, n + 1):
            if not visited[node] and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
        
        # Mark the node as visited
        visited[min_node] = True
        
        # Update distances to the neighbors of the current node
        for neighbor, weight in graph[min_node]:
            if dist[min_node] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_node] + weight

    return dist

# User Input
print("Enter number of nodes:")
n = int(input())

print("Enter number of edges:")
e = int(input())

# Initialize the graph as an adjacency list
graph = {i: [] for i in range(1, n + 1)}

print("Enter each edge (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Since the graph is undirected

# Source node for Dijkstra's Algorithm
print("Enter the start node:")
start_node = int(input())

# Running Dijkstra's Algorithm
distances = dijkstra(graph, start_node, n)

# Output
print("\nShortest distances from node", start_node)
for node in range(1, n + 1):
    print(f"Node {node}: {distances[node]}")



# Enter number of nodes:
# 5
# Enter number of edges:
# 6
# Enter each edge (u v weight):
# 1 2 2
# 1 3 4
# 2 3 1
# 2 4 7
# 3 5 3
# 4 5 1
# Enter the start node:
# 1
# Shortest distances from node 1
# Node 1: 0
# Node 2: 2
# Node 3: 3
# Node 4: 8
# Node 5: 6

