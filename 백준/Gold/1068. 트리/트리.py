'''
1. list에 자식 노드를 현재 본인 index에 리스트로 저장한다. 
2. 재귀함수를 사용해 자식노드를 탐색하는 리스트를 만든다. 
2-1. 자식이 없는 노드라면 leaf_node 카운트 후 리턴. 있다면 자식을 탐색
3. leaf_node 출력
'''

n = int(input())
tree = [[] for _ in range(n+1)]
nodes = list(map(int,input().split()))
del_node = int(input())

for i in range(0,n):
    parents_node = nodes[i]
    tree[parents_node].append(i)

def dfs(child_node,leaf_node):
    have_not_child = 1
    while(child_node):
        have_not_child = 0
        leaf_node = dfs(tree[child_node[0]],leaf_node)
        del child_node[0]
    if have_not_child:
        leaf_node += 1
    return leaf_node

if del_node != tree[-1][0] :
    tree[nodes[del_node]].remove(del_node)
    leaf_nodes = dfs(tree[tree[-1][0]],0)
    print(leaf_nodes)
else:
    print(0)


