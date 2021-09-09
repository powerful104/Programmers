import itertools
def solution(numbers, target):
    answer = 0
    pd = list(itertools.product([1,-1],repeat = len(numbers)))
    for i in pd:
        sum = 0
        for j in range(len(numbers)):
            sum += numbers[j]*i[j]
        if sum == target:
            answer += 1
    return answer
"""
itertools를 사용하여 가능한 양수 음수의 조합을 만들고
해당 조합을 직접 숫자들에 대입해보면서 target과 같은지 확인하였다.

다른사람의 풀이를 보니 재귀를 이용한 사람도 있었다
"""