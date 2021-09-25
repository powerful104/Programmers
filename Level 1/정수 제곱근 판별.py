import math
def solution(n):
    a = math.sqrt(n)
    if a.is_integer():
        return (a+1)**2
    else:
        return -1

"""
간단한 문제였다.
"""