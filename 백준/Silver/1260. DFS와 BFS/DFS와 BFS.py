def dfs(graph, v):
    if visited[v]:
        return
    print(v,end=" ")
    visited[v] = 1
    while graph[v]:
        dfs(graph,graph[v][0])
        visited[graph[v][0]] = 1
        del graph[v][0]

    


def bfs(graph, v):
    visited = [0] * (n+1)
    q = []
    q.append(v)
    print(v,end=" ")
    visited[v] = 1
    while(len(q)):
        node = q[0]
        del q[0]
        for i in graph[node]:
            if not visited[i]:
                print(i,end=" ")
                q.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int,input().split())
    graph[v1] += [v2]
    graph[v2] += [v1]

for i in range(1,n+1):
    graph[i].sort()

visited = [0] * (n+1)
import copy

graph2 = copy.deepcopy(graph)
dfs(graph, v)
print("")
bfs(graph2,v)