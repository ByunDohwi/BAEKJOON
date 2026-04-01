import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,k,visited,citys):
  result = []
  q = deque()
  visited[s] = True
  q.append([s,0])

  while q:
    node, cnt = q.popleft()
    if cnt == k:
      result.append(node)

    for go in citys[node]:
      if not visited[go] and cnt+1 <= k:
        q.append([go,cnt+1])
        visited[go] = True
  
  return result

N, M, K, X = map(int,input().split())
citys = [[] for _ in range(N+1)]

for i in range(M):
  a, b = map(int,input().split()) # a -> b 가는 단방향 도로
  citys[a].append(b)

result = bfs(X,K,[False]*(N+1),citys)
if result:
  result.sort()
  for i in result:
    print(i)
else:
  print(-1)
