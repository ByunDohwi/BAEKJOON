def changeShape(pubao):
  return ''.join(pubao)

from itertools import combinations

X = input()
Y = input()
Z = input()
k = int(input())

MegaX = set(map(changeShape,list(combinations(X,k))))
MegaY = set(map(changeShape,list(combinations(Y,k))))
MegaZ = set(map(changeShape,list(combinations(Z,k))))

answer = (MegaX & MegaY) | (MegaX & MegaZ) | (MegaY & MegaZ)

answer = sorted(answer)
if not answer:
  print(-1)
else:
  for i in answer:
    print(i)