from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    rains = [[INF] * n for _ in range(m)]
    for t, (r, c) in enumerate(drops, start=1):
        rains[r][c] = t

    width_cnt = n - w + 1
    row_min = [[0] * width_cnt for _ in range(m)]

    for i in range(m):
        dq = deque()
        for j in range(n):
            while dq and rains[i][dq[-1]] >= rains[i][j]:
                dq.pop()
            dq.append(j)

            if dq[0] <= j - w:
                dq.popleft()

            if j >= w - 1:
                row_min[i][j - w + 1] = rains[i][dq[0]]

    best_val = -1
    answer = [10**9, 10**9]

    for j in range(width_cnt):
        dq = deque()
        for i in range(m):
            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - h:
                dq.popleft()

            if i >= h - 1:
                top = i - h + 1
                val = row_min[dq[0]][j]

                if val > best_val or (val == best_val and [top, j] < answer):
                    best_val = val
                    answer = [top, j]

    return answer