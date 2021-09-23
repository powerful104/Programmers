def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer += i*j
    return answer

"""
zip을 이용하여 순서대로 짝지어지게 한 후에 값을 곱해주었다.
"""