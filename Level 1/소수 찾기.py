import math
def solution(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return len([ i for i in range(2, n+1) if array[i] ])

"""
에라토스테네스의 체 이용

다른사람의 코드를 보니 
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
이렇게 간단하게 사용한 경우도 있었다.
"""