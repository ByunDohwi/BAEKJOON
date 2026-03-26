import sys
input = sys.stdin.readline


def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]

    while parent[x] != x:
        next_x = parent[x]
        parent[x] = root
        x = next_x

    return root

def union(a,b):
  parent_a = find(a)
  parent_b = find(b)

  if parent_a == parent_b:
    return

  if rank[parent_a] < rank[parent_b]:
    parent[parent_a] = parent_b
  elif rank[parent_a] > rank[parent_b]:
    parent[parent_b] = parent_a
  else:
    parent[parent_b] = parent_a
    rank[parent_a] += 1

def is_connection(a,b):
  if find(a) == find(b):
    return True
  return False

N, M = map(int,input().split())
edges = []
parent = [i for i in range(N+1)]
money = 0
edge_num = 0
rank = [0]*(N+1)

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
    edge_num += 1

print(money)