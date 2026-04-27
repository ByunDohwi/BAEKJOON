
  
        
def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]
    
    for level in range(1,len(triangle)-1):
        for i in range(level+1):
            dp[level+1][i] = max(dp[level+1][i], dp[level][i] + triangle[level+1][i])
            dp[level+1][i+1] = max(dp[level+1][i+1], dp[level][i] + triangle[level+1][i+1])

    return max(dp[len(triangle)-1])
