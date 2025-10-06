miin = min

def solution(n, times):
    max = miin(times) * n
    min = 0
    
    while (max-1 != min):
        num = (min+max)//2
        sum = 0
        for t in times:
            sum += num//t 
        if sum >= n: 
            max = num
        else:
            min = num 
            
    return max