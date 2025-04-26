#this algorithm is also called as I. Minimum Spanning Tree (Prim's Algorithm)



import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
            total_weight += self.graph[parent[i]][i]
        print("Total weight of MST:", total_weight)

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
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
    V = int(input("Enter number of vertices: "))
    g = Graph(V)
    print("Enter adjacency matrix (row by row):")
    for i in range(V):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != V:
            print("Invalid input! Each row must have", V, "elements.")
            sys.exit(1)
        g.graph[i] = row

    print("\nMinimum Spanning Tree:")
    g.primMST()


output:

tanishka@tanishka-Latitude-5490:~$ python3 prim3.py
Enter number of vertices: 5
Enter adjacency matrix (row by row):
Row 1: 0 7 2 3 4
Row 2: 5 0 4 2 1
Row 3: 6 0 3 0 1
Row 4: 5 0 3 2 0
Row 5: 1 0 5 2 1

Minimum Spanning Tree:
Edge 	Weight
0 - 1 	 7
0 - 2 	 2
4 - 3 	 2
2 - 4 	 1
Total weight of MST: 12
tanishka@tanishka-Latitude-5490:~$ 


