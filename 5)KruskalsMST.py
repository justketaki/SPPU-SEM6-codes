# Kruskal's Algorithm for Minimum Spanning Tree

# Function to find the root of a set (with path compression)
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

# Function to union two sets
def union(parent, rank, u_root, v_root):
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
        parent[v_root] = u_root
    else:
        parent[v_root] = u_root
        rank[u_root] += 1

# Kruskal's MST function
def kruskal_mst(edges, n):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    for node in range(1, n+1):
        parent[node] = node
        rank[node] = 0

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        u_root = find(parent, u)
        v_root = find(parent, v)

        if u_root != v_root:
            mst.append((u, v, weight))
            total_weight += weight
            union(parent, rank, u_root, v_root)

    print("\nEdge \tWeight")
    for u, v, weight in mst:
        print(f"{u} - {v} \t{weight}")
    print("\nTotal weight of MST:", total_weight)

# User input
print("Enter number of nodes:")
n = int(input())

print("Enter number of edges:")
e = int(input())

edges = []

print("Enter each edge (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Run Kruskal's Algorithm
kruskal_mst(edges, n)



# Enter number of nodes:
# 5
# Enter number of edges:
# 6
# Enter each edge (u v weight):
# 1 2 2 
# 1 3 3 
# 2 3 1 
# 2 4 5
# 3 4 4 
# 4 5 6

# Edge 	Weight
# 2 - 3 	1
# 1 - 2 	2
# 3 - 4 	4
# 4 - 5 	6

# Total weight of MST: 13
