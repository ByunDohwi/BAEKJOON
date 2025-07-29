n = int(input())
nlist = [i+1 for i in range(n)]

while len(nlist) > 1:
    nlist = [nlist[i] for i in range(len(nlist)) if i % 2 == 1]

print(nlist[0])