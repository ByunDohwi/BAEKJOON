from collections import deque

def check(r,c):
  if 0 <= r < N and 0 <= c < N and not visited[r][c] :
    return True
  return False

def dfs(r,c,rain_height):
  q = deque()
  q.append([r,c])
  while q:
    node = q.pop()
    nr = node[0]
    nc = node[1]
    if visited[nr][nc]:
      continue
    visited[nr][nc] = True
    for go in [[0,1],[0,-1],[1,0],[-1,0]]:
      if check(nr+go[0], nc+go[1]) and maps[nr+go[0]][nc+go[1]] > rain_height:
        q.append([nr+go[0], nc+go[1]])



N = int(input())
maps = []

max_safe = 0
max_height = 0
for i in range(N):
  maps.append(list(map(int,input().split())))
  max_height = max(max(maps[i]),max_height)


for i in range(0,max_height+2):
  visited = [[False] * N for _ in range(N)]
  result = 0
  for j in range(N):
    for k in range(N):
      if not visited[j][k] and maps[j][k] > i:
        dfs(j,k,i)
        result += 1
  max_safe = max(max_safe, result)

print(max_safe)


