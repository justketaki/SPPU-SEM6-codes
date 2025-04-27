class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # store edges as (weight, u, v)

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, xroot, yroot):
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        self.edges.sort()
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        mst = []

        for edge in self.edges:
            w, u, v = edge
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, w))
                self.union(parent, rank, x, y)

        print("Edges in Kruskal's MST:")
        for u, v, weight in mst:
            print(f"{u} - {v} : {weight}")

if __name__ == "__main__":
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    g = Graph(V)

    print("Enter each edge in format (u v w):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.kruskalMST()

#Enter number of vertices: 5
#Enter number of edges: 7
#Edges (u v w):
#0 1 2
#0 3 6
#1 2 3
#1 4 5
#2 4 7
#3 4 9
#2 3 0

