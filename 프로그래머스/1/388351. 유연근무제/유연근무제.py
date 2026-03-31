'''
* 하루도 늦지 않고 출근한 직원의 수
1. timeLog[0] 길이로 순회합니다.
2. i번째 사람이 지각한 경우 schedules[i]와 timelogs[i]를 딜리트합니다.
3. 순회가 끝난 후 schedules의 길이를 리턴합니다.
'''
def check_time(time_sc, time_log):
    if time_sc >= time_log:
        return False
    return True
    

def solution(schedules, timelogs, startday):
    answer = [True] * len(schedules)
    schedules = [i + 10 if i%100 < 50 else i + 50 for i in schedules]
    print(schedules)
    today = startday
    
    for i in range(len(timelogs[0])):
        for j in range(len(schedules)):
            if not (today%7 == 0 or today%7 == 6) and check_time(schedules[j],timelogs[j][i]):
                answer[j] = False
        today += 1
    
    return answer.count(True)