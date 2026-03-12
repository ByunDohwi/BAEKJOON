from collections import deque

def check(r,c):
  if 0 <= r < R and 0 <= c < C and maps[r][c] != 1:
    return True
  return False

def bfs(r,c, move, k):
  q = deque()
  q.append([r,c,move,k])
  visited[r][c][k] = True

  while q:
    node = q.popleft()

    nr = node[0]
    nc = node[1]
    nmove = node[2]
    nk = node[3]

    if nr == R-1 and nc == C-1:
      return nmove

    if nk > 0:
      for go in [[-2,1],[-1,2],[1,2],[2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]:
        if check(nr+go[0],nc+go[1]) and not visited[nr+go[0]][nc+go[1]][nk-1]:
          q.append([nr+go[0],nc+go[1],nmove+1,nk-1])
          visited[nr+go[0]][nc+go[1]][nk-1] = True
    for go in [[0,1],[0,-1],[1,0],[-1,0]]:
      if check(nr+go[0],nc+go[1]) and not visited[nr+go[0]][nc+go[1]][nk]:
        q.append([nr+go[0],nc+go[1],nmove+1,nk])
        visited[nr+go[0]][nc+go[1]][nk] = True
  return -1




K = int(input())
C, R = map(int,input().split())
visited = [[[False] * (K + 1) for _ in range(C)] for _ in range(R)]

maps = []
for i in range(R):
  maps.append(list(map(int,input().split())))

print(bfs(0,0,0,K))