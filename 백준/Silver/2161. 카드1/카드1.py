from collections import deque

num = int(input())
q = deque()
list = []

for i in range(1,num+1):
    q.append(i)

while(len(q) >= 1):
    list.append(q.popleft())
    if(len(q) >= 1):
        q.append(q.popleft())

print(*list)