n = int(input())
candy_list = list(map(int,input().split()))
candies = 0
odd_num = 0
min_odd = 9999

for num in candy_list:
  if(num %2 ==1):
    odd_num +=1
    if(min_odd>num):
      min_odd = num
  candies += num


print(candies if odd_num %2 == 0 else candies-min_odd)
