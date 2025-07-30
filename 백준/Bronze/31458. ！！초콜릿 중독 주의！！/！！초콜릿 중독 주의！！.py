'''
-> 팩토리얼과 논리반전을 한 계산 결과
1. 문자열을 뒤에서부터 읽기
2. 뒤에 문자열이 있으면 숫자 1로 만들기
3. 앞의 논리반전 횟수만큰 숫자 반전
'''
n = int(input())

for i in range(n):
  num = 0
  flag = False
  expr = input()
  for idx in range(len(expr)-1,-1,-1):
    ch = expr[idx]
    if (ch == '!'):
      if flag:
        num = 0 if num == 1 else 1
      else:
        num = 1
    else: 
      flag = True
      num = num if num else int(ch)
  print(num)



