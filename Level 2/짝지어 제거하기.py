def solution(s):
    LArr = []
    answer = -1

    for i in s:
        if len(LArr) != 0 and LArr[-1] == i:
            LArr.pop()
        else:
            LArr.append(i)

    if len(LArr) == 0:
        answer = 1
    else:
        answer = 0
    return answer

"""
처음엔 LArr만이 아닌 RArr도 같이 생성하여 풀었다
LArr과 RArr를 지금 확인중인 가상 커서의 왼쪽과 오른쪽으로 나눈 두 리스트라고 가정하고 문제를 풀이했다
두 리스트의 맨뒤와 맨앞을 확인하여 같을땐 두 요소를 지워주고 같지않을땐 커서를 넘어가는(오른쪽의 맨앞 요소를 왼쪽으로 넘기는)
작업을 수행하여 문자열의 끝까지 확인후 LArr가 비어있다면 1이 나오도록하고 아니라면 0이 나오게 하여 문제가 돌아가게끔 하였다

def solution(s):
    LArr = []
    RArr = list(s)
    answer = -1

    while len(RArr) != 0:
        if len(LArr) != 0 and LArr[-1] == RArr[0]:
            LArr.pop()
            RArr.pop(0)
        else:
            LArr.append(RArr.pop(0))

    if len(LArr) == 0:
        answer = 1
    else:
        answer = 0
    return answer

다음과 같이 작성하였는데 효율성 테스트를 계속 통과하지 못하였다
그래서 list(s)가 문제가 있을것 같아 RArr를 문자열을 그대로 사용하기로 결정, 하지만 기존의 방식대로 맨앞의 요소를 pop하지 않고도
하나씩 뒤로가며 확인만 해주면 된다고 판단하여 지금의 형태로 변형되었다
"""