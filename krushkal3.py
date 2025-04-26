class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def kruskal_mst(self):
        self.edges.sort(key=lambda x: x[2])  # Sort edges by weight
        ds = DisjointSet(self.V)
        mst_weight = 0
        mst_edges = []

        for u, v, w in self.edges:
            if ds.find(u) != ds.find(v):  # No cycle
                ds.union(u, v)
                mst_edges.append((u, v, w))
                mst_weight += w

        print("Kruskal's MST edges and weights:")
        for u, v, w in mst_edges:
            print(f"{u} - {v}: {w}")
        print("Total weight of MST:", mst_weight)

if __name__ == '__main__':
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    g = Graph(V)
    print("Enter edges (u v w) for each edge:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.kruskal_mst()



output :
tanishka@tanishka-Latitude-5490:~$ python3 kruskal3.py
Enter the number of vertices: 4
Enter the number of edges: 5
Enter edges (u v w) for each edge:
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
Kruskal's MST edges and weights:
2 - 3: 4
0 - 3: 5
0 - 1: 10
Total weight of MST: 19
tanishka@tanishka-Latitude-5490:~$ 


