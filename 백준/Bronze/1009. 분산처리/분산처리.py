n = int(input())
list = [0,1,4,4,2,1,1,4,4,2]
for i in range(n):
    a, b = map(int,input().split())
    if a % 10 ==0:
        print("10")
        continue
    print((a**((b%list[(a%10)])if(b%list[(a%10)])!=0 else list[a%10]))%10)