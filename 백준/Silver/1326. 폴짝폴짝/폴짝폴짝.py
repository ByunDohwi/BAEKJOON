from collections import deque

def bfs(idx):
  q = deque()
  q.append(idx)
  min_bridge[idx] = 0
  visited[idx] = True
  while q:
    node = q.popleft()

    for i in range(node+bridge[node],N,bridge[node]):
      if not visited[i]:
        q.append(i)
        min_bridge[i] = min_bridge[node]+1
        visited[i] = True
        if i == B-1:
          return
    for i in range(node-bridge[node],-1,-bridge[node]):
      if not visited[i]:
        q.append(i)
        min_bridge[i] = min_bridge[node]+1
        visited[i] = True
        if i == B-1:
          break

  


N = int(input())
bridge = list(map(int,input().split()))
min_bridge = [-1] * N
visited = [False] * N
A,B = map(int,input().split())
min_num = 99999

bfs(A-1)

print(min_bridge[B-1])