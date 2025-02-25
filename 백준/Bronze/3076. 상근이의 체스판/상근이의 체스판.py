R,C = map(int, input().split())
A,B = map(int, input().split())
fir_line = ''
next_line = ''

for i in range(C):
    if i%2:
        fir_line += 'X'*B
    else:
        fir_line += '.'*B

next_line = fir_line
next_line = next_line.replace('X','0')
next_line = next_line.replace('.','X')
next_line = next_line.replace('0','.')

for i in range(R):
    for j in range(A):
        if i%2:
            print(fir_line)
        else:
            print(next_line)
