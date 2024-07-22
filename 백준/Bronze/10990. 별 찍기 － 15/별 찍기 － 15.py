n = int(input())
for i in range(n):
    print(' '*(n - 1 - i), end="")
    print('*', end="")
    if i:
        print(' '*(i*2-1), end="")
        print('*', end="")
    print()
