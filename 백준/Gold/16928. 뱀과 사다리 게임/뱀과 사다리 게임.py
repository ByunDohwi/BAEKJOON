from collections import deque

def bfs(s, board, visited):
  visited[s] = True
  q = deque()
  q.append([s,0]) # 위치, 주사위 cnt
  while q:
    node, cnt = q.popleft()
    if node == 100:
      return cnt

    for i in range(1,7):
      if node + i > 100:
        continue
      nxt = node + i if board[node + i] == -1 else board[node + i]
      if not visited[nxt]:
        q.append([nxt,cnt+1])
        visited[nxt] = True


N, M = map(int,input().split())
board = [-1] * 101

for i in range(N+M):
  st, ed = map(int,input().split())
  board[st] = ed

print(bfs(1, board,[False]*101))

