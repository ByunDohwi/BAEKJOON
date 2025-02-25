import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.extend(list(map(int,input().split())))
    nums.sort()
    nums = nums[-n:]

print(nums[-n])
