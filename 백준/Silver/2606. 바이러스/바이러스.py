'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
from collections import deque

def bfs(s):
  q = deque()
  q.append(s)
  answer = 0
  while q:
    node = q.popleft()

    if visited[node]:
      continue
    
    answer += 1
    visited[node] = True
    for i in network[node]:
      if not visited[i]:
        q.append(i)

  return answer



N = int(input())
bridge_num = int(input())
network = [[] for _ in range(N)]
visited = [False] * N

for i in range(bridge_num):
  a, b = map(int,input().split())
  network[a-1].append(b-1)
  network[b-1].append(a-1)

print(bfs(0)-1)