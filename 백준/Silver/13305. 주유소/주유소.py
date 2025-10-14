n = int(input())-1
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

answer = 0
idx = 0
oil = 0

while(idx < n):
  oil_dis = 0
  p = price[idx] 
  while(oil < n-1):
    if(p > price[oil+1]):
      break
    oil += 1
    
  for i in range(idx, oil+1):
    oil_dis += distance[i]
  answer += oil_dis * p
  idx = oil+1

print(answer)
