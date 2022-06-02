def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price - coin]
    return dp[n] % 1000000007

    """
    처음 거스름돈을 보고 간단하게 생각했다.
    하지만 내가 간단하게 생각한문제는 최소 거스름돈 개수를 찾는 문제 였고
    해당 문제는 접근법이 달랐다.
    
    다른사람의 풀이를 참고하여 작성하였다.
    """