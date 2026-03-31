from collections import deque
def check(x,y):
  if 0 <= x and x < N and 0 <= y and y < M:
    return True
  return False

def bfs(s, tomatos):
  q = deque()
  cnt = 0
  for x,y in s:
    q.append([x,y,0])
  
  while q:
    x, y, cnt = q.popleft()
    for go in [[0,1],[0,-1],[1,0],[-1,0]]:
      if check(x+go[0],y+go[1]) and tomatos[x+go[0]][y+go[1]] == 0:
        q.append([x+go[0],y+go[1],cnt+1])
        tomatos[x+go[0]][y+go[1]] = 1
  
  return cnt, tomatos

# 가로, 세로
M, N = map(int,input().split())
tomatos = [list(map(int,input().split())) for _ in range(N)]

st_tt = []
for i in range(N):
  for j in range(M):
    if tomatos[i][j] == 1:
      st_tt.append([i,j])
  
cnt, tomatos = bfs(st_tt, tomatos)

for tomato_line in tomatos:
  if 0 in tomato_line:
    print(-1)
    exit()

print(cnt)