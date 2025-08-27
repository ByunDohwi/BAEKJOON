def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    
    print(citations)
    
    while citations: 
        if(citations.pop(0) <= answer):
            break;
        answer += 1
        
        
    return answer