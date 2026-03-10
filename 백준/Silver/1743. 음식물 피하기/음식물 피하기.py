from collections import deque

def check(r, c):
    return 0 <= r < R and 0 <= c < C and not visited[r][c] and maps[r][c]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    answer = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if check(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                answer += 1
    return answer

R, C, K = map(int,input().split())
maps = [[False]*C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
result = 0

for i in range(K):
  r,c = map(int,input().split())
  maps[r-1][c-1] = True


for r in range(R):
    for c in range(C):
        if maps[r][c] and not visited[r][c]:
            result = max(result, bfs(r, c))

print(result)