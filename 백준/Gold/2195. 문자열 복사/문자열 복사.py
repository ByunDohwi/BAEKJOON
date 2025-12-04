s = input()
p = list(input())
if len(p) == 1:
  print(1)
  exit(0)

p1 = p.pop(0)

  

answer = 0

while(p):
  while(1):
    if p and p1+p[0] in s:
      p1 = p1+p.pop(0)
    else:
      break
  answer += 1
  if p:
    p1 = p.pop(0)
    if not p:
      answer += 1


print(answer)