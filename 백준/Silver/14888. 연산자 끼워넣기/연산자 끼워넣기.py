import itertools
from pprint import pprint

def opereition(a, b, op):
  ll = 1

  if op == 0:
    return a+b
  elif op == 1:
    return a - b
  elif op == 2:
    return a * b
  else:
    if a < 0:
      ll = -1
    a = a * ll
    return (a // b)*ll



n = int(input())

nums = list(map(int,input().split()))
ops = list(map(int,input().split())) # 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
ops_num = sum(ops)
op_sunso = []
max_num = -99999999999
min_num = 999999999999

op_num = 0
for i in ops:
  for j in range(i):
    op_sunso.append(op_num)
  op_num += 1

nOPr = list(itertools.permutations(op_sunso,ops_num))

for i in nOPr:
  idx = 1
  result = nums[0]
  for j in i:
    result = opereition(result, nums[idx], j)
    idx += 1
  if result > max_num:
    max_num = result
  if result < min_num:
    min_num = result

print(max_num)
print(min_num)