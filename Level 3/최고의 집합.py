def solution(n, s):
    answer = [s//n]*n
    s = s % n
    for i in range(s):
        answer[-1*(i+1)] += 1
    if answer.count(0) > 0:
        return [-1]
    return answer

"""
집합의 곱이 최대가 되는 조건은 집합의 원소끼리의 차이가 가장 적을때이다.
따라서 집합에 수를 똑같이 배분하고 남은수를 다시 하나씩 배분하여 차이를 줄인다.
"""