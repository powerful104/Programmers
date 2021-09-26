import math
def solution(n, k):
    answer = []
    li = [i + 1 for i in range(n)]
    idx= k-1
    for i in range(n,1,-1):
        fact = math.factorial(i-1)
        answer.append(li[idx//fact])
        del li[idx//fact]
        idx = idx % fact
    answer.append(li[0])
    return answer

"""
모음 사전과 비슷하게 앞에 나와야만 하는 숫자를 찾으며 뒤에 배열을 붙이는 방식으로 진행하였다.
"""