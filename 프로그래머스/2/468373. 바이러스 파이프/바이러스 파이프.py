import itertools
from collections import deque

def spread(visited, pipe_type, graph, n):
    q = deque()

    # 현재 감염된 모든 노드를 시작점으로
    for node in range(1, n + 1):
        if visited[node]:
            q.append(node)

    while q:
        node = q.popleft()
        for nxt in graph[node][pipe_type]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    return visited

def solution(n, infection, edges, k):
    graph = [[[] for _ in range(3)] for _ in range(n + 1)]

    for x, y, t in edges:
        graph[x][t - 1].append(y)
        graph[y][t - 1].append(x)

    answer = 1

    for route in itertools.product([0, 1, 2], repeat=k):
        visited = [False] * (n + 1)
        visited[infection] = True

        for pipe_type in route:
            visited = spread(visited, pipe_type, graph, n)

        answer = max(answer, sum(visited))

    return answer