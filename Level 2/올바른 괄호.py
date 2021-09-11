def solution(s):
    LArr = []
    answer = False
    for j in s:
        if len(LArr) != 0 and ((LArr[-1] == '(' and j == ')')):
            LArr.pop()
        else:
            LArr.append(j)

    if len(LArr) == 0:
        answer = True
    return answer

"""
괄호 회전하기를 미리 풀었어서 푸는데에 어려움이 있지는 않았다
"""