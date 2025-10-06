n = int(input())
p = [2, 1]
for i in range(1,n):
  a = p[0] + p[1]*2
  b = p[0] + p[1]
  p = [a, b]
  
print((p[0] + p[1])%9901)