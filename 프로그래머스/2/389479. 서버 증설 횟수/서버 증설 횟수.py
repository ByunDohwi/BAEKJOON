def solution(players, m, k):
    cm = [0] * 24 # [0] = 0~1시까지 이용
    for time in range(24):
        usable_cm = sum(cm[time:])
        print(cm)
        if players[time] > (usable_cm*m)+(m-1):
            more_py = players[time] - (usable_cm*m)
            end_time = time + k -1 if time+k -1 < 23 else 23
            cm[end_time] += more_py//m
    
            
    return sum(cm)