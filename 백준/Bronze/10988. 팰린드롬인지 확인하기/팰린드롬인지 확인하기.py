str = input()
answer = 1
for i in range(len(str)//2+len(str)%2):
    if(str[i] != str[(len(str)-1)-i]):
        answer = 0
print(answer)