def solution(num):
    cnt = 0
    for _ in range(500):
        if num == 1:
            break
        if num % 2 == 0:
            num //= 2
        else:
            num = 3*num + 1
        cnt += 1
    else:
        return -1
    return cnt

"""
조건에 맞게 나누고 곱하는과정을 해주면서 count하면 되는 문제였다.
"""