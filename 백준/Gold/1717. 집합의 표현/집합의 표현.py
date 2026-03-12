import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

N, M = map(int,input().split())
parents = [i for i in range(N+1)]

for i in range(M):
  calculate, a, b = map(int,input().split())
  if calculate == 0 and a != b:
    b_parent = find(b)
    a_parent = find(a)
    if a_parent < b_parent:
      parents[a_parent] = b_parent
    else:
      parents[b_parent] = a_parent
  elif calculate == 1:
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
      print("yes")
    else:
      print("no")