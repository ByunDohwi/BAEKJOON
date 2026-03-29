'''
1. for문과 popleft()을 통해 message 한 문자씩 탐색
2. word에 한글자씩 추가
 2-1. 현재의 idx가 spoiler_ranges에 포함되면 is_secret = True
 2-2. 현재의 idx가 spoiler_ranges[1]을 넘어서면 spoiler_idx += 1
 2-3. 나온 글자가 공백일 경우 word의 secret 값에 따라 set 또는 list에 추가 및 word, is_secret 초기화
3. 전체 탐색 후, secret_word list 순회하며 set에 존재하는지 탐색
4. 존재하지 않는 경우만 answer += 1
'''
def solution(message, spoiler_ranges):
    words = set()
    secret_words = []
    is_secret = False
    answer = 0
    spoiler_idx = 0
    word = ""
    
    for idx, alphabet in enumerate(message):
        if alphabet == ' ' or idx == len(message)-1:
            if idx == len(message)-1:
                word += alphabet
            if is_secret:
                secret_words.append(word)
            else:
                words.add(word)
            
            word = ""
            is_secret = False
            continue
        
        if spoiler_idx < len(spoiler_ranges) and spoiler_ranges[spoiler_idx][1] < idx:
            spoiler_idx += 1
        if spoiler_idx < len(spoiler_ranges) and spoiler_ranges[spoiler_idx][0] <= idx and idx <= spoiler_ranges[spoiler_idx][1]:
            is_secret = True
        word += alphabet
        
    for secret_word in secret_words:
        if secret_word in words:
            continue
        else:
            answer += 1
            words.add(secret_word)
        
    return answer