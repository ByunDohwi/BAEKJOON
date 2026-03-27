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