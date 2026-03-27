'''
1. 신호등 중 가장 긴 주기의 신호등 선택
2. 모든 주기의 공배수 시간까지 탐색
3. 긴 주기의 신호등이 노란불인 시간에 다른 신호등도 노란불인지 탐색
    
3-1. 모든 신호등이 노란불일 경우 해당 시간 반환
3-2. 공배수 시간 전체 탐색해도 없는 경우 -1 반환
'''
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcmm(arr):
    result = arr[0]
    for x in arr[1:]:
        result = lcm(result, x)
    return result


def solution(signals):
    answer = -1
    periods = [s[0] + s[1] + s[2] for s in signals]

    max_p = 0
    p_idx = -1
    for idx, s in enumerate(signals):
        p = s[0] + s[1] + s[2]
        if p > max_p:
            max_p = p
            p_idx = idx

    for i in range(signals[p_idx][0], lcmm(periods) + 1, max_p):
        for j in range(signals[p_idx][1]):
            yellow_s = 0
            for s in signals:
                if (i + j - s[0]) % (s[0] + s[1] + s[2]) < s[1]:
                    yellow_s += 1
            if yellow_s == len(signals):
                return i + j + 1

    return answer