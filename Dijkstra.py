def min_dist(dist,visited):
    min_dist = 100000
    n = len(dist)
    for ver in range(n):
        if visited[ver] == 0 and dist[ver]<min_dist:
            min_dist = dist[ver]
            min_ver = ver
    return min_ver


def dijkstra(src, graph):
    n = len(graph)
    visited = [0] * n
    dist = [100000] * n

    dist[src] = 0

    for i in range(n):
        u = min_dist(dist,visited)
        visited[u] = 1

        for ver in range(n):
            if visited[ver] == 0 and graph[u][ver]!=0 and graph[u][ver] + dist[u] < dist[ver]:
                dist[ver] = graph[u][ver] + dist[u]
    
    return dist

n = int(input("Enter the no. of edges : "))
print("Enter adjacency matrix of graph : ")
graph = [list(map(int,input().split())) for i in range(n)]
src = int(input("\nEnter source vertex : ")) - 1
dist = dijkstra(src,graph)

print()
for i in range(n):
    print(f"Minimum distance from vertex {src+1} to vertex {i+1} = {dist[i]}")

