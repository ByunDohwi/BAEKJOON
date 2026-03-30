import sys
from collections import deque
input = sys.stdin.readline

N, k = map(int,input().split())
nums = list(map(int,input().split()))
max_num = -1
q = deque()

for i in range(len(nums)):
  while q and nums[q[-1]] > nums[i]:
    q.pop()
  q.append(i)

  if q[0] <= i-k:
    q.popleft()

  if i >= k-1:
    max_num = max(max_num,nums[q[0]])

print(max_num)