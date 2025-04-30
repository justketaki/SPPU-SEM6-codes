def greedy_search(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start, [start])]  # (heuristic, node, path)
    closed_list = set()

    while open_list:
        # Sort by heuristic value (lowest first)
        open_list.sort()
        h, current_node, path = open_list.pop(0)

        if current_node == goal:
            return path
        
        closed_list.add(current_node)

        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in closed_list:
                open_list.append((heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None

# --- Input Section ---
graph = {}
num_edges = int(input("Enter number of edges: "))
print("Enter edges in the format: from_node to_node cost")

for _ in range(num_edges):
    u, v, cost = input().split()
    cost = int(cost)
    if u not in graph:
        graph[u] = []
    graph[u].append((v, cost))
    # If undirected graph, add reverse edge also
    # graph[v].append((u, cost))

heuristic = {}
num_nodes = int(input("Enter number of nodes: "))
print("Enter node and its heuristic value (format: node heuristic)")

for _ in range(num_nodes):
    node, h = input().split()
    heuristic[node.strip()] = int(h)

start_node = input("Enter start node: ").strip()
goal_node = input("Enter goal node: ").strip()

# --- Run Greedy Search ---
path = greedy_search(graph, heuristic, start_node, goal_node)

if path:
    print("Path found:", path)
else:
    print(f"No path found from {start_node} to {goal_node}")


# Enter number of edges: 5
# Enter edges in the format: from_node to_node cost
# a b 2
# a c 4
# b d 7
# c d 1
# d e 3
# Enter number of nodes: 5
# Enter node and its heuristic value (format: node heuristic)
# a 1 
# b 4
# c 9
# d 4
# e 0
# Enter start node: a 
# Enter goal node: e
# Path found: ['a', 'b', 'd', 'e']
