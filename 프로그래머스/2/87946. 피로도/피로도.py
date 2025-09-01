def solution(k, dungeons):
    n = len(dungeons)

    def dfs(energy, visited, cleared):
        # 현재까지 깬 수를 기준으로 최대치 갱신 (리턴)
        best = cleared
        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and energy >= need:
                visited[i] = True                  # 선택
                best = max(best, dfs(energy - cost, visited, cleared + 1))
                visited[i] = False                 # 원상복구(백트래킹)
        return best

    return dfs(k, [False]*n, 0)