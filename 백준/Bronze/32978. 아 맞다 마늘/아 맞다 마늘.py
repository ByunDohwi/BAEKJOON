n = int(input())
d = input().split()
r = input().split() 

for i in range(n-1):
    d.remove(r[i])

print(d[0])