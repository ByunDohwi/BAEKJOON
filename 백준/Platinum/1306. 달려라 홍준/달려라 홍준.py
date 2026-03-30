import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
nums = list(map(int,input().split()))
q = deque()

k = k*2-1

if n < k:
  print(" ")
  exit()

for i in range(n):
  while q and nums[q[-1]] <= nums[i]:
    q.pop()
  q.append(i)

  if q[0] <= i-k:
    q.popleft()

  if i >= k-1:
    print(nums[q[0]],end=" ")