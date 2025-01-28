a, b = map(int,input().split())
li = []
data = [
    ['.', 'O', '-', '|', '/', '\\', '^', '<', 'v', '>'],
    ['.', 'O', '|', '-', '\\', '/', '<', 'v', '>', '^']
]
answerList = []
for i in range(a):
    li.append(input())

for i in range(b):
    answer = ""
    for j in range(a):
        answer += data[1][data[0].index(li[j][i])]
    answerList.insert(0,answer)

for i in range(b):
    print(answerList[i])
