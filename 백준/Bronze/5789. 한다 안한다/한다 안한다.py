n = int(input())
for i in range(n):
    patels = input()
    result = "Do-it" if(patels[len(patels)//2 - 1]==patels[len(patels)//2]) else "Do-it-Not"
    print(result)
