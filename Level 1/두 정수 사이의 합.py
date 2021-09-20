def solution(a, b):
    answer = 0
    if a > b:
        a,b = b,a
    for i in range(a,b+1):
        answer += i
    return answer

"""
사이의 값을 다 더해주는 간단한 문제였다.
"""