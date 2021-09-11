def solution(n):
    for i in range(n+1,1000001):
        if bin(i).count('1') == bin(n).count('1'):
            break
    return i

"""
n보다 큰 숫자 부터 하나씩 올려가며 1의 개수를 확인하면 되는 간단한 문제였다
"""