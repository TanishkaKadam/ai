import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # For undirected graph

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[u] != sys.maxsize and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

    def min_distance(self, dist, spt_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if not spt_set[v] and dist[v] < min_val:
                min_val = dist[v]
                min_index = v
        return min_index

    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for i in range(self.V):
            print(f"{i} \t{dist[i]}")

if __name__ == '__main__':
    V = int(input("Enter the number of vertices: "))
    g = Graph(V)
    E = int(input("Enter the number of edges: "))
    print("Enter edges (u v w) for each edge:")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    source = int(input("Enter the source vertex: "))
    g.dijkstra(source)



output :

tanishka@tanishka-Latitude-5490:~$ python3 dijkstra3.py
Enter the number of vertices: 5
Enter the number of edges: 6
Enter edges (u v w) for each edge:
0 1 10
0 2 5
1 2 2
1 3 1
2 3 9
3 4 4
Enter the source vertex: 0
Vertex 	Distance from Source
0 	0
1 	7
2 	5
3 	8
4 	12
tanishka@tanishka-Latitude-5490:~$
