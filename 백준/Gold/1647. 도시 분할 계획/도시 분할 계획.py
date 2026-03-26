import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
  parent_a = find(a)
  parent_b = find(b)
  if a > b:
    parent[parent_a] = parent_b
  else:
    parent[parent_b] = parent_a

def is_connection(a,b):
  if find(a) == find(b):
    return True
  return False

N, M = map(int,input().split())
edges = []
parent = [i for i in range(N+1)]
money = 0
max_c = 0
edge_num = 0
for i in range(M):
  a,b,c = map(int,input().split())
  if a == b:
    continue
  edges.append([a,b,c])
edges.sort(key= lambda x: x[2])

for edge in edges:
  a,b,c = edge
  if edge_num > N -1:
    break
  if not is_connection(a,b):
    union(a,b)
    money += c
    max_c = max(max_c,c)
    edge_num += 1

print(money-max_c)