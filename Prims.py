def min_out(graph, visited, unvisited):
    minEdge = None
    for i in range(len(visited)):
            for j in range(len(unvisited)):
                if graph[visited[i]][unvisited[j]] != 0:
                    if minEdge == None:
                        minEdge = (visited[i], unvisited[j], graph[visited[i]][unvisited[j]])
                    elif graph[visited[i]][unvisited[j]] < minEdge[2]:
                        minEdge = (visited[i], unvisited[j], graph[visited[i]][unvisited[j]])
    return minEdge

def prims(graph):
    mst = []
    visited = []
    unvisited = []
    for i in range(1,len(graph)):
        unvisited.append(i)
    visited.append(0)
    while len(unvisited) > 0:
        minEdge = min_out(graph, visited, unvisited)
        mst.append(minEdge)
        visited.append(minEdge[1])
        unvisited.remove(minEdge[1])
    return mst


n = int(input("Enter the no. of edges : "))
print("Enter adjacency matrix of graph : ")
graph = [list(map(int,input().split())) for i in range(n)]

mst = prims(graph)

print("\nEdges\tWeight")
for x in mst:
    print(f"{x[0]+1}  {x[1]+1} \t  {x[2]}")
