'''
1. 안 쓰는 지름길 삭제 -> 검색 줄어들어서 기모찌 도착지를 넘거나 손해인거
2. 도착지 리스트 만들고
3. 1씩 더하면서 도착지 리스트에 있으면 추가요
'''

N, D = map(int, input().split())
jirmril = []
dochackji = set()
doro = [0 for _ in range(D+1)]
doro[1] = 1

for i in range(N):
  road = list(map(int,input().split()))
  if(road[1]<= D and road[1] - road[0]>= road[2]):
    jirmril.append(road)
    dochackji.add(jirmril[-1][1])

for i in range(2,D+1):
  최단거리 = doro[i-1]+1
  if i in dochackji:
    for j in jirmril:
      if i == j[1]:
        최단거리 = min(최단거리,doro[j[0]]+j[2])
  doro[i] = 최단거리

print(doro[D])