'''

3 4 6
....
.T..
....

'''
'''
dfs(r,c,map,cnt)
'''
def check(r,c):
  if 0 <= r < R and 0 <= c < C and 지도[r][c] != 'T':
    return True
  return False

def dfs(r,c,cnt):
  answer = 0
  if cnt == K and r == 0 and c == C-1:
    return 1
  elif cnt >= K:
    return 0
  for go in [[-1,0],[1,0],[0,-1],[0,1]]:
    if check(r+go[0],c+go[1]) and not 다녀갔니[r+go[0]][c+go[1]]:
      다녀갔니[r+go[0]][c+go[1]] = True
      answer += dfs(r+go[0],c+go[1],cnt+1)
      다녀갔니[r+go[0]][c+go[1]] = False
      
  return answer


R, C, K = map(int, input().split())
# R = 세로/ C = 가로
지도 = []
다녀갔니 = [[False]*C for _ in range(R)]

for i in range(R):
  지도.append(input())

다녀갔니[R-1][0] = True
print(dfs(R-1, 0,1))