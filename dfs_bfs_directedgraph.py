class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]  # adjacency list

    def add_edge(self, u, v):
        self.adj[u].append(v)  # only u -> v (directed)

    def bfs(self, start):
        visited = [False] * self.V
        queue = []
        visited[start] = True
        queue.append(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.V
        print("DFS Traversal:", end=" ")
        self.dfs_util(start, visited)
        print()

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    g = Graph(V)

    print("Enter each directed edge (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex for BFS and DFS: "))

    g.bfs(start_vertex)
    g.dfs(start_vertex)
#Enter the number of vertices: 5
#Enter the number of edges: 5
#Enter each directed edge (u v):
#0 1
#0 2
#1 2
#2 3
#3 4
#Enter the starting vertex for BFS and DFS: 0
