korea = ['K','O','R','E','A']
idx = 0
str = input()
for spelling in str:
    if korea[idx%5] == spelling:
        idx += 1
        
print(idx)