'''
!! 가장 많이 선물 받는 친구가 받는 선물의 수
* 선물 지수 = 이번달 자신이 친구들에게 준 선물 - 받은 선물의 수
* 선물 지수가 같다면 주고받지 않음
* 아무것도 주고받지 않았어도 선물지수로 비교

1. 모든 friends도 dict로 추가 key = "사람 이름" | value = [선물 지수, 받은 선물 횟수]
2. 모든 gifts를 dict로 추가 - key = "준사람 받은사람" | value = 준 횟수
3. gifts를 순회하며 dict 추가 및 선물 지수 측정
4. gifts dict 순회
 4-1. 해당 dict의 준 횟수와 상대가 준 횟수 비교
 4-2. 더 많은 쪽의 받은 선물 횟수 +1
'''
def solution(friends, gifts):
    answer = 0
    fr_dt = dict()
    gi_dt = dict()
    
    for friend in friends:
        fr_dt[friend] = [0,0]
        
    for gift in gifts:
        a, b = gift.split()
        fr_dt[a][0] += 1
        fr_dt[b][0] -= 1
        if gift in gi_dt:
            gi_dt[gift] += 1
        else:
            gi_dt[gift] = 1
        
    for idx, a in enumerate(friends):
        for b in friends[idx:]:
            if a == b:
                continue
            a_gift = gi_dt.get(f"{a} {b}",0) # a가 준 선물
            b_gift = gi_dt.get(f"{b} {a}",0) # b가 준 선물
            if a_gift > b_gift:
                fr_dt[a][1] += 1
            elif b_gift > a_gift:
                fr_dt[b][1] += 1
            # 같은 경우
            else:
                if fr_dt[a][0] > fr_dt[b][0]:
                    fr_dt[a][1] += 1
                elif fr_dt[a][0] < fr_dt[b][0]:
                    fr_dt[b][1] += 1
    for friend in fr_dt.values():
        answer = max(answer,friend[1])
    return answer