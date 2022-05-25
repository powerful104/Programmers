from math import factorial
def solution(n):
    return factorial(2*n)/(factorial(n)*factorial(n+1))

    """
    카탈란 수를 이용하여 풀었다.
    
    다른사람의 풀이중에는 다음과 같은것도 있었다.
    
        
    memo = [1, 1, 2, 5]
    def solution(n):
        return N_Bracket(n)

    def N_Bracket(n):
        if n < len(memo):
            return memo[n]
        else:
            temp = 0
            for i in range(n):
                temp += N_Bracket(i) * N_Bracket(n - 1 - i)
            memo.append(temp)
            return memo[n]
            
            
    또는 다음과 같다.
    
    def solution(n):
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                # n=2 -> dp[2] = (dp[1] * dp[0]) + (dp[0] * dp[1])
                # n=3 -> dp[3] = (dp[1] * dp[0]) + (dp[0] * dp[1]) + (dp[2] * dp[0]) + (dp[1] * dp[1]) + (dp[0] * dp[2])
                dp[i] += dp[i-j] * dp[j-1]
        return dp[n]
        
    """