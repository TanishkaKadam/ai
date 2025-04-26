#Practical No. 1
#Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
#graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
#structure.

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set() # TO keep track of DFS visited nodes
    visited2 = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)

    print("The following is DFS")
    dfs(visited1, graph, 1)
    print()
    print("The following is BFS")
    bfs(visited2, graph, 1, queue)

if __name__=="__main__":
    main()


    # graph = {
    #     '1' : ['2','3'],
    #     '2' : ['4', '5'],
    #     '3' : ['6','7'],
    #     '4' : [],
    #     '5' : [],
    #     '6' : [],
    #     '7' : []
    #     DFS : 1 2 4 5 3 6 7 
    #     BFS : 1 2 3 4 5 6 7 
    # }




to run in terminal : python3 BFS1.py
output eg: tanishka@tanishka-Latitude-5490:~$ python3 BFS1.py
Enter number of nodes : 5
Enter number of edges for node 1 : 2
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3
Enter number of edges for node 2 : 1
Enter edge 1 for node 2 : 4
Enter number of edges for node 3 : 0
Enter number of edges for node 4 : 0
Enter number of edges for node 5 : 0
The following is DFS
1 2 4 3 
The following is BFS
1 2 3 4 
