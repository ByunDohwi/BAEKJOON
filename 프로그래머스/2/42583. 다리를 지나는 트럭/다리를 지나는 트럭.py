'''
1. 큐에 트럭 무게 * 10000 + 들어온 시각 으로 저장
2. 1초 씩 경과하며 현재 시각 - 들어온 시각 = bridge_length 되는 경우 제거하고, 대기 트럭이 들어올 수 있는지 확인

'''

def solution(bridge_length, weight, truck_weights):
    time = 0
    doro_time = []
    doro_weight = []
    while truck_weights:
        time += 1
        
        if doro_time and time - doro_time[0] == bridge_length:
            doro_time.pop(0)
            doro_weight.pop(0)
        if sum(doro_weight)+truck_weights[0] <= weight:
            doro_time.append(time)
            doro_weight.append(truck_weights.pop(0))
        
    return time + bridge_length