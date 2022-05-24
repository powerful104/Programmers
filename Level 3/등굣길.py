def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    puddleMap = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for puddle in puddles:
        puddleMap[puddle[1]][puddle[0]] = 1
    
    dp[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            if puddleMap[j][i] == 1:
                continue
            dp[j][i] += (dp[j - 1][i] + dp[j][i - 1])%1000000007
    answer = dp[n][m]
    return answer

    """
    쉬운 dp 문제 였다.
    """