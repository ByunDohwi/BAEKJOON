n = int(input())
li = []
ans = []
dic = {}
idx =0
isSame = 1
for i in range(n):
    li.append(input().split()[:-1])
    ans.append(li[i][0])

max_len = len(max(li, key=lambda x:len(x)))

for i in range(n):
    if(len(li[i]) < max_len):
        li[i] += ['0'] * (max_len-len(li[i]))

while(isSame):
    isSame = 0
    idx+=1
    for i in range(n):
        if(ans[i] in dic):
            isSame=1
        else:
            dic[ans[i]] = 0
        if(idx != max_len):
            ans[i] = ans[i]+li[i][idx]

print(idx)