'''
* n이 16?
1. 완탐완탐
'''
import itertools

# stage, 현재 가진 티켓 수, 살 수 있는 티켓 수, cost

def check_cost(cost,stage,ticket_cnt):
    if ticket_cnt >= len(cost):
        return cost[stage-1][-1]
    else:
        return cost[stage-1][ticket_cnt]

def go_stage(cost, hint, buy_bd):
    money = 0
    # 힌트권
    ticket = []
    
    for stage in range(1,len(cost)+1):
        money += check_cost(cost,stage,ticket.count(stage))
        if stage != len(cost) and buy_bd[stage-1]:
            bd_money = hint[stage-1][0]
            ticket = ticket + hint[stage-1][1:]
            money += bd_money
    return money


def solution(cost, hint):
    answer = 99999999
    # 힌트권
    ticket = []
    for buy_bd in itertools.product([True, False], repeat = len(cost)-1):
        answer = min(answer,go_stage(cost,hint,buy_bd))

    return answer