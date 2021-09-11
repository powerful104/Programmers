import itertools
import math
def is_prime_number(n):
    array = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

def solution(numbers):
    li = []
    answer = 0
    for i in range(len(numbers)):
        li += list((map(int,[''.join(i) for i in list(itertools.permutations(list(numbers),i+1))])))
    prime = is_prime_number(max(li))
    for i in set(li):
        if i in prime:
            answer += 1
    return answer

"""
소수 문제는 항상 시간초과가 뜰까 무섭다
다행히 이번에는 시간초과가 뜨진 않았다
하지만 내코드는 뭔가 비효율적이게 짜게 된것같다
"""