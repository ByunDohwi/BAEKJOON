import sys
input = sys.stdin.readline

def merge(a, b):
    if arr[a] >= arr[b]:
        return a
    return b

def buildSegmentTree(node, start, end):
    if start == end:
        segmentTree[node] = start
        return segmentTree[node]
    
    mid = (start + end) // 2;
    left = buildSegmentTree(node*2, start, mid)
    right = buildSegmentTree(node*2 + 1, mid + 1, end)

    segmentTree[node] = merge(left, right)
    return segmentTree[node]

def checkSection(targetStart, targetEnd, node, start, end):
    if targetStart > targetEnd:
        return 0
    
    if targetEnd < start or targetStart > end:
        return 0
    
    if targetStart <= start and end <= targetEnd:
        return node
    
    mid = (start + end) // 2
    left = checkSection(targetStart, targetEnd, node*2, start, mid)
    right = checkSection(targetStart, targetEnd, node*2 +1, mid +1, end)

    if arr[segmentTree[left]] < arr[segmentTree[right]]:
        return right
    return left
    

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.append(0)
    segmentTree = [-1] * (4 * N)
    buildSegmentTree(1, 0, N-1)
    segmentTree[0] = N

    numberIndex = [-1] * (N+1)
    flag = True
    for i in range(N):
        num = arr[i]
        if numberIndex[num] == -1:
            numberIndex[num] = i
        else:
            node = checkSection(numberIndex[num]+1, i-1, 1, 0, N-1)
            if arr[segmentTree[node]] > num:
                flag = False
                break
            numberIndex[num] = i
    
    if flag == True:
        print("Yes")
    else:
        print("No")