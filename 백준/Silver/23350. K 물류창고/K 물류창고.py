'''
1. n, m 우선순위, 무게 입력받기
2. 각 컨테이너를 무게,우선순위 컨테이너 데큐에 넣기
3. 우선순위를 정렬시킨 ulist만들기
4. 컨테이너를 꺼내 현재 들어와야할 우선순위인지 확인하기 
    4-1. 아니라면 answer에 컨테이너 무게 더하고 각 컨테이너에 append
    4-2. 맞다면 같은 우선순위에서 가장 가벼운지 확인하기 맞다면 그대로 적재
    4-3. 아니라면 우선순위가 같고 나보다 가벼운 화물 찾기, 가벼운 화물들 무게 *2 answer에 더하기
5. 모든 컨테이너가 사라질 때까지 4번 반복
6. answer 출력하기 
'''
from collections import deque
n,m = map(int,input().split())

UContainer = deque()
MContainer = deque()
MList = []
UList = []

answer = 0

for i in range(n):
    U, M = map(int, input().split())
    MContainer.append(M)
    UContainer.append(U)

USortedList = deque(sorted(UContainer, reverse=True))

while(len(MContainer) > 0):
    m = MContainer.popleft()
    u = UContainer.popleft()
    cU = USortedList.popleft()

    if(cU != u):
        answer += m
        MContainer.append(m)
        UContainer.append(u)
        USortedList.appendleft(cU)
    elif(len(MList) == 0 or MList[len(MList)-1] >= m):
        MList.append(m)
        UList.append(u)
    else:
        for i in range((len(MList)-1),-2,-1):
            if(i != -1 and UList[i]==u and MList[i] < m):
                answer += MList[i]*2
            else:
                UList.insert(i+1,u)
                MList.insert(i+1,m)
                break
answer += sum(MList)
print(answer)
