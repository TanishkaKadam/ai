#Practical No. 1
#Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
#graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
#structure.

#BFS
graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[]
}
visited=[]
queue=[]

def bfs(visited,graph,node):
        visited.append(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            print(s,end=" ")
            
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    
print("following path is Breadth-First Algorithm")
bfs(visited,graph,'A')


#DFS
graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':['F'],
'F':[]
}
visited = set()

def dfs(visited,graph,node):
        if node not in visited:
                print(node,end=" \n")
                visited.add(node)

                for neighbour in graph[node]:
                        dfs (visited,graph,neighbour)
                        
print("\nfollowing path is Depth-First Algorithm")
dfs(visited,graph,'A')


to run in terminal : python3 BFS1.py
