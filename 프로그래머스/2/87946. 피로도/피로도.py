from itertools import permutations 

def goto_dungeon(k,dungeon_johab):
    answer = 0
    for d in dungeon_johab:
        if k >= d[0]:
            k -= d[1]
            answer += 1
    return answer

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons):
        answer = max(goto_dungeon(k,i), answer)
    
    return answer

    
    
