def solution(n):
    answer = 0
    for i in range(1,n + 1):
        if n % i == 0:
            answer += i
    return answer

"""
나누어지는 수를 모두 더하면 되었다.
"""