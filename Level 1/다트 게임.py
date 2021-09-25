def solution(dartResult):
    cur = 0
    num = 0
    scores = [0]
    while cur != len(dartResult):
        tmpcur = cur
        while dartResult[cur].isdigit():
            cur += 1
        score = int(dartResult[tmpcur:cur])
        num+=1
        if dartResult[cur] == 'D':
            score **= 2
        elif dartResult[cur] == 'T':
            score **=3
        cur+=1
        scores.append(score)
        if cur != len(dartResult):
            if dartResult[cur] == '*':
                scores[num-1] *= 2
                scores[num] *= 2
                cur += 1
            elif dartResult[cur] == '#':
                scores[num] *= -1
                cur += 1
    return sum(scores)

"""
C++의 방식처럼 풀어버렸다.
다른사람의 풀이를 보니 정규표현식을 이용하였다.
"""