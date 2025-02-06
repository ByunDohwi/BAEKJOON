def findTime(str_num,i,time_num = -1):
    for j in str_num:
        time_num += 1
        is_rignt_num = 1
        for k in range(15):
            if(i[k]=='#' and j[k] == '.'):
                is_rignt_num = 0
                break
        if(is_rignt_num):
            break
    return time_num

list = ['','','','']
answer = ''
str_num = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####"
]
for i in range(5):
    timeList = input().split()
    list[0] += timeList[0]
    list[1] += timeList[1]
    list[2] += timeList[2]
    list[3] += timeList[3]

from pprint import pprint

answer += str(findTime(str_num[:3],list[0]))
if(answer != '2'):
    answer += str(findTime(str_num[:],list[1]))
else:
    answer += str(findTime(str_num[:4],list[1]))
answer += str(findTime(str_num[:6],list[2]))
answer += str(findTime(str_num[:],list[3]))

answer = answer[:2]+':'+answer[2:]

print(answer)
        
