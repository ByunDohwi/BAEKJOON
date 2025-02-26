import sys
input = sys.stdin.readline
from collections import deque


def bfs(v):
    visited = [0] * (len(graph)+1)
    q = deque([v])
    cnt = 1
    visited[v] = 1
    while(len(q)):
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = 1
    return cnt

computer, edge = map(int, input().split())
graph = [[]for _ in range(computer+1)]
for i in range(edge):
    a, b = map(int,input().split())
    graph[b].append(a)

max_list = []
max_len = 0

for i in range(1,computer+1):
    n = bfs(i)
    if n > max_len:
        max_list.clear()
        max_list.append(i)
        max_len = n
    elif n == max_len:
        max_list.append(i)

print(*max_list)