def a_star_search(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]  # (f = g+h, g, node, path)
    closed_list = set()
    
    while open_list:
        # Sort by total estimated cost (f = g + h)
        open_list.sort()
        f, g, current_node, path = open_list.pop(0)
        
        if current_node == goal:
            return path, g
        
        closed_list.add(current_node)
        
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in closed_list:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))
    
    return None, float('inf')

# --- User Input ---
graph = {}
num_edges = int(input("Enter number of edges: "))
print("Enter edges in the format: from_node to_node cost")

for _ in range(num_edges):
    u, v, cost = input().split()
    cost = int(cost)
    if u not in graph:
        graph[u] = []
    graph[u].append((v, cost))
    # If undirected graph, also add reverse edge
    # graph[v].append((u, cost))

heuristic = {}
num_nodes = int(input("Enter number of nodes: "))
print("Enter node and its heuristic value (format: node heuristic)")

for _ in range(num_nodes):
    node, h = input().split()
    heuristic[node] = int(h)

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

# --- Run A* Search ---
path, cost = a_star_search(graph, heuristic, start_node, goal_node)

if path:
    print("Minimum cost path:", path)
    print("Total cost:", cost)
else:
    print("No path found from", start_node, "to", goal_node)



# Enter number of edges: 4
# Enter edges in the format: from_node to_node cost
# a b 1
# a c 4
# b c 2
# c d 1
# Enter number of nodes: 4
# Enter node and its heuristic value (format: node heuristic)
# a 5
# b 2
# c 1
# d 0
# Enter start node: a
# Enter goal node: d
# Minimum cost path: ['a', 'b', 'c', 'd']
# Total cost: 4
