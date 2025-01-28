import sys
input = sys.stdin.readline

n = int(input())
li = [] 
m = 0
time = 0
idx = 0
ex_time = 0


for i in range(n):
    asdf = list(map(int,input().split()))
    if(asdf[1] == 0):
        continue
    elif(asdf[0] == 0):
        ex_time += asdf[1]
        continue
    li.append(asdf)
    idx+=1

# print(max_b)

def f(x):
    v = (x[1] / x[0])
    # print(x, v)
    return v
li.sort(key=lambda x: f(x))

# from pprint import pprint
# pprint(li)

for i in li:
    time += (i[0] * time + i[1])%40000

print((time + ex_time)%40000)
