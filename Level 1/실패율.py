def solution(N, stages):
    fail = [[i+1, 0] for i in range(N)]

    for i in range(N):
        cnt0 = 0
        cnt1 = 0
        for j in stages:
            if j == i + 1:
                cnt0 += 1
            if not j < i + 1:
                cnt1 += 1
        cnt1 = max(cnt1, 1)
        fail[i][1] = cnt0/cnt1
    fail = sorted(fail, key = lambda x : -x[1])
    return [i[0] for i in fail]

"""
스테이지와 사용자를 비교해가며 진행하였는데 시간복잡도가 너무 큰것 같다.
더 줄일수 있을것 같다.
"""