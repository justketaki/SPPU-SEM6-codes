def is_safe(graph, color, vertex, c, V):
    for i in range(V):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True

def solve_graph_coloring(graph, m, color, vertex, V):
    if vertex == V:
        return True

    for c in range(1, m+1):
        if is_safe(graph, color, vertex, c, V):
            color[vertex] = c
            if solve_graph_coloring(graph, m, color, vertex + 1, V):
                return True
            color[vertex] = 0  # Backtrack

    return False

def graph_coloring(graph, m, V):
    color = [0] * V

    if not solve_graph_coloring(graph, m, color, 0, V):
        print("No solution exists.")
        return

    print("Assigned Colors to Vertices:")
    for i in range(V):
        print(f"Vertex {i} --> Color {color[i]}")

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    print(f"Enter the adjacency matrix ({V}x{V}) row by row:")
    graph = []
    for _ in range(V):
        row = list(map(int, input().split()))
        graph.append(row)

    m = int(input("Enter the number of colors available: "))

    graph_coloring(graph, m, V)


#Enter the number of vertices: 4
#Enter the adjacency matrix (4x4) row by row:
#0 1 1 1 
#0 1 0 1
#1 0 1 0
#0 0 1 1 
# Enter the number of colors available: 3
# Assigned Colors to Vertices:
# Vertex 0 --> Color 1
# Vertex 1 --> Color 1
# Vertex 2 --> Color 2
# Vertex 3 --> Color 1
