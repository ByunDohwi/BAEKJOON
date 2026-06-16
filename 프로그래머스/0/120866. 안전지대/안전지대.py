def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for r,c in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]:
                    if 0<=i+r<len(board) and 0<=j+c<len(board[0]) and board[i+r][j+c] == 0:
                        board[i+r][j+c] = 2
    
    for i in board:
        answer += i.count(0)
    
    return answer