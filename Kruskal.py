class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)

        if par_u != par_v:
            if self.rank[par_u] > self.rank[par_v]:
                self.parent[par_v] = par_u
            elif self.rank[par_u] < self.rank[par_v]:
                self.parent[par_u] = par_v
            else:
                self.parent[par_v] = par_u
                self.rank[par_u]+=1

def kruskals(graph):
    n = len(graph)
    dsu = DSU(n)
    mst = []

    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges.append((i,j,graph[i][j]))
    edges.sort(key = lambda x: x[2])

    c=0
    while c<n-1:
        for u,v,wt in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u,v)
                mst.append((u,v,wt))
                c+=1
    return mst

n = int(input("Enter the no. of edges : "))
print("Enter adjacency matrix of graph : ")
graph = [list(map(int,input().split())) for i in range(n)]

mst = kruskals(graph)

print("\nEdges\tWeight")
for x in mst:
    print(f"{x[0]+1}  {x[1]+1} \t  {x[2]}")