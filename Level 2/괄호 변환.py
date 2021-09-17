def isCorrect(s):
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

def makeCorrect(s):
    if s == "":
        return s
    i = 2
    while i != len(s):
        if s[:i].count("(") == s[:i].count(")"):
            break
        else:
            i += 2
    u = s[:i]
    v = s[i:]
    if isCorrect(u):
        return u + makeCorrect(v)
    else:
        return "(" + makeCorrect(v) + ")" + u[1:-1].replace("(",".").replace(")","(").replace(".",")")

def solution(p):
    return makeCorrect(p)

"""
괄호 회전하기와 올바른 괄호를 풀고나서 풀었다.
그러니 올바른 괄호 판별과 문제의 설명의 지시에 따라서만 코드를 짜면 되는 간단한 문제였다.
"""