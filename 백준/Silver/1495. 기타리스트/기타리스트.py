N, S, M = map(int,input().split())
volumes = list(map(int,input().split()))

play_volumes = [set() for _ in range(N)]

if(S+volumes[0] <= M):
  play_volumes[0].add(S+volumes[0])
if(S-volumes[0] >= 0):
  play_volumes[0].add(S-volumes[0])

for i in range(1,N): # 0 ~ N-1
  for value in play_volumes[i-1]:
    if(value+volumes[i] <= M):
      play_volumes[i].add(value+volumes[i])
    if(value-volumes[i] >= 0):
      play_volumes[i].add(value-volumes[i])

print(max(play_volumes[N-1]) if play_volumes[N-1] else -1)