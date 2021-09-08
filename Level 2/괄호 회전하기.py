def solution(s):
    answer = 0
    for i in range(len(s)-1):
        tmpS = s[i:]+s[:i]
        LArr = []
        for j in tmpS:
            if len(LArr) != 0 and ((LArr[-1] == '(' and j == ')') or (LArr[-1] == '{' and j == '}') or (LArr[-1] == '[' and j == ']')):
                LArr.pop()
            else:
                LArr.append(j)

        if len(LArr) == 0:
            answer += 1
    return answer

"""
처음 문제를 보자마자 짝지어 제거하기와 같이 올바른 괄호 문자열을 판별하면 되겠다는 생각이 들었다
시간초과가 뜨지 않을까 걱정했지만 문자열의 길이가 1000이하여서 시간초과 걱정을 하지 않고 풀었다
"""