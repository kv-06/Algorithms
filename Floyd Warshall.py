def FloydWarshall(graph):
    n = len(graph)
    dist = [[1000 for i in range(n)] for j in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = int(input("Enter the no. of edges : "))
print("Enter adjacency matrix of graph : ")
graph = [list(map(int,input().split())) for i in range(n)]

dist = FloydWarshall(graph)

print("\nDistance Matrix : ")
for row in dist:
    for x in row:
        print(x, end = ' ')
    print()
    