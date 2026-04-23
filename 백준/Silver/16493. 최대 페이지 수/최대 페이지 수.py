def bound(idx, used_day, total_page):
    if used_day > N:
        return -1

    remain = N - used_day
    upper = total_page

    for i in range(idx, M):
        day, page = chapters[i]
        if day <= remain:
            remain -= day
            upper += page
        else:
            upper += page * (remain / day)
            break

    return upper


def dfs(idx, used_day, total_page):
    global max_page

    if used_day > N:
        return

    if idx == M:
        max_page = max(max_page, total_page)
        return

    if bound(idx, used_day, total_page) <= max_page:
        return

    day, page = chapters[idx]

    dfs(idx + 1, used_day + day, total_page + page)
    dfs(idx + 1, used_day, total_page)


N, M = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(M)]

# page/day 비율이 큰 순서대로 정렬해야 bound가 의미 있는 상한이 된다.
chapters.sort(key=lambda x: x[1] / x[0], reverse=True)

max_page = 0

dfs(0, 0, 0)
print(max_page)
