def solution(s):
    answer = 1
    
    # 홀수인 경우
    for i in range(1,len(s)-1):
        st = i-1
        ed = i+1
        s_len = 0
        while st >=0 and ed <len(s):
            if s[st] != s[ed]:
                break
            st -= 1
            ed += 1
            s_len += 1
        answer = max(s_len*2+1,answer)
    # 짝수인 경우
    for i in range(1,len(s)):
        st = i-1
        ed = i
        s_len = 0
        while st >=0 and ed <len(s):
            if s[st] != s[ed]:
                break
            st -= 1
            ed += 1
            s_len += 1
        answer = max(s_len*2,answer)

    return answer