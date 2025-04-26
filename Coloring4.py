def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    def solve(node):
        if node == n:
            return True

        for c in range(1, m+1):
            if is_safe(node, graph, color, c):
                color[node] = c
                if solve(node + 1):
                    return True
                color[node] = 0  # Backtrack

        return False

    if solve(0):
        print("Colors assigned to vertices:")
        for i in range(n):
            print(f"Vertex {i+1} ---> Color {color[i]}")
    else:
        print("No solution exists using", m, "colors")


# ===== MAIN CODE =====
n = int(input("\nEnter number of vertices for Graph Coloring: "))
e = int(input("Enter number of edges: "))

graph = [[0 for _ in range(n)] for _ in range(n)]
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

m = int(input("Enter number of colors: "))
graph_coloring(graph, m)



output :
tanishka@tanishka-Latitude-5490:~$ python3 coloring4.py

Enter number of vertices for Graph Coloring: 4
Enter number of edges: 5
Enter edges (u v):
1 2
2 3
3 4
4 1 
1 3
Enter number of colors: 3
Colors assigned to vertices:
Vertex 1 ---> Color 1
Vertex 2 ---> Color 2
Vertex 3 ---> Color 3
Vertex 4 ---> Color 2
tanishka@tanishka-Latitude-
