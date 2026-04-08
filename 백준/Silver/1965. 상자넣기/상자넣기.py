from bisect import bisect_left

N = int(input())
nums = list(map(int, input().split()))
q = []

for num in nums:
    idx = bisect_left(q, num)
    if idx == len(q):
        q.append(num)
    else:
        q[idx] = num

print(len(q))