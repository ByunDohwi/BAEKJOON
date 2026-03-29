'''
* grage[node][0] = 해당 노드를 이긴 노드
* grage[node][1] = 해당 노드를 진 노드
1. 그래프 구성
2. 선수대로 순차 탐색
3. 해당 선수의 노드부터 이긴 노드 진 노드를 각각 탐색 
4. 이긴 노드와 진 노드의 수가 n-1라면 answer += 1
'''
def bfs(s, graph, visited,type):
    visited[s] = True
    q = [s]
    node_cnt = 0
    
    while q:
        node = q.pop()
        node_cnt += 1
        
        for son in graph[node][type]:
            if not visited[son]:
                q.append(son)
                visited[son] = True
    return node_cnt - 1

def solution(n, results):
    answer = 0
    graph = [[[] for _ in range(2)] for _ in range(n+1)]
    
    for winner, loser in results:
        graph[loser][0].append(winner)
        graph[winner][1].append(loser)
        
    for i in range(1,n+1):
        lose_cnt = bfs(i, graph, [False]*(n+1),1)
        win_cnt = bfs(i, graph, [False]*(n+1),0)
        print(i,lose_cnt + win_cnt)
        if lose_cnt + win_cnt == n-1:
            answer += 1
    return answer