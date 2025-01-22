
chgLi = input().split()
word = input()
answer = ""
phLi = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '']
numbers = [
    '2', '22', '222',
    '3', '33', '333',
    '4', '44', '444',
    '5', '55', '555',
    '6', '66', '666',
    '7', '77', '777','7777',
    '8', '88', '888',
    '9','99','999','9999'
    ]
numLi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0,9):
    num = str(i+1)
    if(chgLi[i] == '1'):
        continue
    idx = numbers.index(chgLi[i])
    if(chgLi[i] == '7' or chgLi[i] == '9'):
        phLi[idx+3] = num*4
    phLi[idx] = num
    phLi[idx+1] = num*2
    phLi[idx+2] = num*3

for i in range(len(word)):
    num = phLi[numLi.index(word[i])]
    if(i != 0 and answer[-1] == num[0]):
        answer += '#'
    answer += num

print(answer)