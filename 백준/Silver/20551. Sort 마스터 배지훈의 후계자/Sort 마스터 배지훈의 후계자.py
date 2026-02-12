import sys

input = sys.stdin.readline

def find_first(target, data):
    start, end = 0, len(data)  # [start, end)
    while start < end:
        mid = (start + end) // 2
        if data[mid] >= target:
            end = mid
        else:
            start = mid + 1

    if start < len(data) and data[start] == target:
        return start
    return -1

N, M = map(int, input().split())
num_list = [int(input()) for _ in range(N)]
num_list.sort()

out = []
for _ in range(M):
    D = int(input())
    out.append(str(find_first(D, num_list)))

sys.stdout.write("\n".join(out))