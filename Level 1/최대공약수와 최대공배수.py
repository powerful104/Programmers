from math import gcd
def solution(n, m):
    return [gcd(n,m),n*m//gcd(n,m)]

"""
간단한 문제였다.
"""