def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer
"""
예산조사결과를 정렬하고 budget에서 하나씩 빼면서 개수를 체크하였다.
"""