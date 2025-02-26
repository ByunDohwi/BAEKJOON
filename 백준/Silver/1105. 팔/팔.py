def find_eight(num):
    eight = 0
    for i in num:
        if i == '8':
            eight += 1
    return eight


start, end = map(str,input().split())
same_num_index = 0
front_eight = 0
if len(start) == len(end):
    if start == end:
        print(find_eight(start))
        exit(0)
    for i in range(len(start)):
        if start[i] == end[i]:
            same_num_index += 1
        else:
            break

if same_num_index:
    front_eight = find_eight(start[:same_num_index])
    #start = start[same_num_index:]
    #end = end[same_num_index:]

print(front_eight)
'''
answer = 11
for num in range(int(start),int(end)+1):
    str_num = str(num)
    eight = find_eight(str_num)
    if eight < answer:
        answer = eight
        if answer == 0:
            break

print(answer+front_eight)
'''