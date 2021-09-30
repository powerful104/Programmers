def move(n, start, to):
    result.append([start, to])
    return

def hanoi(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1,via, to, start)
    return

def solution(n):
    hanoi(n,1,3,2)
    return result

result = []

"""
쉽게 알고리즘이 생각이 나지않아 다른사람의 코드를 참고하였다.

나중에 보지않고 다시 풀것
"""