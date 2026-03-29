'''
1. 양방향 그래프 생성
2. 모든 간선 하나씩 절단 - 양 node에서 상대 간선 제거
3. bfs로 각 간선이 몇 개인지 확인
4. 두 차 값을 절대값으로 min해 return
'''
from collections import deque
import math

def bfs(s, graph, visited):
    node_cnt = 0
    
    visited[s] = True
    q = deque()
    q.append(s)
    while q: 
        node = q.popleft()
        node_cnt += 1
        for son_node in graph[node]:
            if not visited[son_node]:
                q.append(son_node)
                visited[son_node] = True
    return node_cnt

def solution(n, wires):
    answer = 9999999
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        a_cnt = bfs(a,graph,[False]*(n+1))
        b_cnt = bfs(b,graph,[False]*(n+1))
        answer = min(answer, abs(a_cnt-b_cnt))
        graph[a].append(b)
        graph[b].append(a)
    
    return answer