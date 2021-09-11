def solution(land):
    prvDP = [0]*4
    newDP = [0]*4
    for i in land:
        for j in range(4):
            mx = 0
            for k in range(4):
                if j != k and i[j] + prvDP[k] > mx:
                    mx = i[j] + prvDP[k]
            newDP[j] = mx
        prvDP = list(newDP)
    return max(newDP)

"""
DP를 이용하여 내려오면서 현재행의 어떤 열에서 얻을 수 있는 최고점을 기록하며 밑으로 내려갔다
예를들어 3행 1열에서의 최고점은 2행 2~4열까지의 최고점을 통해 알 수 있다

어려운 문제는 아니었다
다른사람의 풀이는 DP를 이용했지만 나와는 다른 코드를 사용하였다
리스트 슬라이싱을 통해 풀은것 같아보인다
def solution(land):
    
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

"""