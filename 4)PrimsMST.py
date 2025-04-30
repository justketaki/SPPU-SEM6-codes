# Prim's Algorithm for Minimum Spanning Tree

# Function to find the node with minimum key value
def find_min_key(key, mst_set, n):
    min_value = float('inf')
    min_index = -1

    for v in range(1, n+1):
        if not mst_set[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    return min_index

# Function to perform Prim's Algorithm
def prim_mst(graph, n):
    key = {}
    parent = {}
    mst_set = {}

    for i in range(1, n+1):
        key[i] = float('inf')
        mst_set[i] = False
        parent[i] = -1

    key[1] = 0  # Starting node is 1

    for _ in range(n-1):
        u = find_min_key(key, mst_set, n)
        mst_set[u] = True

        for v in range(1, n+1):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print("\nEdge \tWeight")
    total_weight = 0
    for i in range(2, n+1):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]
    print("\nTotal weight of MST:", total_weight)

# User input
print("Enter number of nodes:")
n = int(input())

# Initialize the graph
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

print("Enter number of edges:")
e = int(input())

print("Enter each edge (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  # Since the graph is undirected

# Run Prim's Algorithm
prim_mst(graph, n)
