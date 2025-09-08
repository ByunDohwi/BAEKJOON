def solution(name):
    n = len(name)
    # 세로 이동 합
    vertical = sum(min(ord(c)-65, 26-(ord(c)-65)) for c in name)

    # 수평 이동 최소
    horizontal = n - 1
    for i in range(n):
        j = i + 1
        # i 다음부터 연속된 'A' 구간의 끝 j 찾기
        while j < n and name[j] == 'A':
            j += 1
        # 좌→우→좌 패턴, 우→좌→우 패턴을 고려한 최소치
        horizontal = min(horizontal,
                         2*i + (n - j),    # 오른쪽 갔다가 왼쪽으로 돌아오기
                         i + 2*(n - j))    # 왼쪽으로 먼저 갔다가 오른쪽으로
    return vertical + horizontal