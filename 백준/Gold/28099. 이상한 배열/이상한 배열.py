import sys
input = sys.stdin.readline

n = int(input())

def segment(left, right, node):
    if left==right:
        tree[node] = left
        return tree[node]
    mid = (left+right)//2
    tree[node] = merge(segment(left,mid,node*2),segment(mid+1,right,node*2+1))
    return tree[node]

def merge(a,b):
    if nodes[a] >= nodes[b]:
        return a
    return b

def query(target_start, target_end, node, start, end):#target start,end - 탐색 범위| start, end - 전체 범위| node - 현재 노드(인덱스)
    if target_end < start or target_start > end:# 말이 안되는 상황 : 꺼져라
        return -1
    if target_start <= start and end <= target_end:#target범위가 맞을때
        return node
    
    mid = (start+end)//2
    left = query(target_start,target_end,2*node,start,mid)
    right = query(target_start,target_end,2*node+1,mid+1,end)

    if nodes[tree[left]] < nodes[tree[right]]:
        return right
    return left

for i in range(n):
    node_len = int(input())
    nodes = list(map(int,input().split()))
    nodes.append(0)
    tree = [-1] * (node_len * 4)
    tree[0] = node_len
    final_idx = [-1]* (node_len+1)

    segment(0,node_len-1,1)

    is_strange = 1
    for right in range(node_len):
        left = final_idx[nodes[right]]
        if left != -1:
            panel_max_num_idx = query(left,right,1,0,node_len-1)
            if nodes[tree[panel_max_num_idx]] > nodes[left]:
                is_strange = 0
                break
        final_idx[nodes[right]] = right
    print("Yes" if is_strange else "No")

