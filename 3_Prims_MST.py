import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__ == '__main__':
    V = int(input("Enter the number of vertices: "))
    g = Graph(V)
    print("Enter the adjacency matrix row by row (space separated):")
    for i in range(V):
        row = list(map(int, input().split()))
        if len(row) != V:
            print(f"Please enter exactly {V} numbers for row {i+1}")
            sys.exit(1)
        g.graph[i] = row

    g.primMST()

  #Enter number of vertices: 5
#Enter adjacency matrix:
#0 2 0 6 0
#2 0 3 8 5
#0 3 0 0 7
#6 8 0 0 9
#0 5 7 9 0
