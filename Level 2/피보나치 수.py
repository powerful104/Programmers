def solution(n):
    fn = 0
    fn1 = 1
    answer = fn1
    for _ in range(n - 1):
        answer = fn + fn1
        fn = fn1
        fn1 = answer
    return answer%1234567

"""
간단한 문제였다.
"""