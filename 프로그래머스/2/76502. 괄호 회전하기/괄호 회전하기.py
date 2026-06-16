def is_opening(c):
    if c == '{' or c == '[' or c == '(':
        return True
def is_same(o,c):
    if (o == '{' and c == '}') or (o == '[' and c == ']') or (o == '(' and c == ')'):
        return True
    return False

def check_abl(s):
    if len(s)%2 == 1:
        return False
    
    q = []
    for c in s:
        if is_opening(c):
            q.append(c)
        elif q and is_same(q[-1],c):
            q.pop()
        else:
            return False
    if not q:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        if check_abl(s[i:]+s[:i]):
            answer += 1
    return answer