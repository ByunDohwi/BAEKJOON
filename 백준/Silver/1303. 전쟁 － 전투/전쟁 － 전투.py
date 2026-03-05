def check(i, j):
  return 0 <= i < M and 0 <= j < N

def dfs(i,j):
  visited[i][j] = False
  q = [[i,j]]
  answer = 0
  while q:
    answer += 1
    agun = q.pop(0)
    가로 = agun[0]
    세로 = agun[1]
    if visited[가로][세로]:
      visited[가로][세로] = False
    for A in [[0,1],[0,-1],[1,0],[-1,0]]:
      nx, ny = 가로 + A[0], 세로 + A[1]
      if check(nx, ny) and visited[nx][ny] and colors[nx][ny] == colors[i][j]:
        visited[nx][ny] = False
        q.append([nx, ny])
  return answer

N, M = map(int, input().split())
colors = []
for i in range(M):
  colors.append(input())

visited = [[True]*N for _ in range(M)]

B = 0
W = 0



for i in range(M):
  for j in range(N):
    if visited[i][j]:
      agun_num = dfs(i,j)
      if colors[i][j] == 'B':
        B += agun_num * agun_num
      else:
        W += agun_num * agun_num

print(W, B)
